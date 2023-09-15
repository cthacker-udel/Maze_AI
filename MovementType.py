from enum import Enum


class MovementType(Enum):
    """
    The type of movement the node can execute

    Args:
        Enum (int): The type of movement (Left, Right, Down, Up)
    """
    LEFT = 0,
    RIGHT = 1,
    UP = 2,
    DOWN = 3
