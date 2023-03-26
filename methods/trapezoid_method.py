from typing import Callable
from methods.abstract_method import solve_abstract_method, find_intervals_without_break_points
from equation import Equation

def _calculate(equation: Callable[[float], float], a: float, b: float, partition_value: int):
    h: float = (b - a) / partition_value
    
    sum: float = (equation(a) + equation(b)) / 2
    
    for step in range(1, partition_value):
        sum += equation(a + step * h)
    
    return sum * h


def solve_integral(equation: Equation, a: float, b: float, accuracy: float, partition_value: int):
    intervals_without_break_points = find_intervals_without_break_points(equation, a, b)
    
    integral_result: float = 0
    partition_value_result: int = -1

    for i in range(len(intervals_without_break_points) // 2):
        method_function: Callable[[int], float] = lambda partition_value: _calculate(equation.itself, intervals_without_break_points[i * 2], intervals_without_break_points[i * 2 + 1], partition_value)
        current_result, current_partition_value = solve_abstract_method(method_function, partition_value, accuracy, 2)

        integral_result += current_result
        partition_value_result = max(partition_value_result, current_partition_value)
    
    return integral_result, partition_value_result
