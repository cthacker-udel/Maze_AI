from random import randint
from typing import Tuple, Optional


def generate_cost(min: int = 1, max: int = 10):
    """
    Generates what cost should be placed on the spot
    """
    return randint(min, max)


def generate_starting_point(rows: int, cols: int) -> Tuple[int, int]:
    """
    Generates a starting point for the maze solver to spawn in

    Args:
        rows (int): The # of rows in the maze
        cols (int): The # of columns in the maze
    """
    return (randint(0, rows), randint(0, cols))


def points_equal(point_one: Tuple[int, int], point_two: Tuple[int, int]) -> bool:
    """
    Determines if two points are equal, by comparing

    Args:
        point_one (Tuple[int, int]): The source point
        point_two (Tuple[int, int]): The target point

    Returns:
        bool: Whether the two points are equal
    """
    return point_one[0] == point_two[0] and point_one[1] == point_two[1]


def generate_goal_point(rows: int, cols: int, point: Tuple[int, int]) -> Tuple[int, int]:
    """
    Generates a goal point for the maze solver to reach

    Args:
        rows (int): The # of rows in the maze
        cols (int): The # of columns in the maze
        point (Tuple[int, int]): The point to avoid when placing the goal point

    Returns:
        Tuple[int, int]: The goal point
    """
    generated_point = generate_starting_point(rows, cols)
    while points_equal(point, generated_point):
        generated_point = generate_starting_point(rows, cols)
    return generated_point


def compute_manhattan_distance(source_point: Tuple[int, int], goal_point: Tuple[int, int]) -> int:
    """
    Computes the manhattan distance between 2 points

    Args:
        source_point (Tuple[int, int]): The source point
        goal_point (Tuple[int, int]): The goal point
    """
    return abs(source_point[0] - goal_point[0]) + abs(source_point[1] - goal_point[1])
