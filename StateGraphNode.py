from __future__ import annotations
from typing import List, Tuple


class StateGraphNode:
    """
    Represents a single state in the maze
    """

    def __init__(self: StateGraphNode) -> None:
        """
        Initializes a state graph node

        Args:
            self (StateGraphNode): The internal instance of the state graph node
        """
        self.state_row: int = 0
        self.state_col: int = 0
        self.visited_coords: List[Tuple[int, int]]

    def move_up(self: StateGraphNode) -> None:
        """
        Moves the node up one

        Args:
            self (StateGraphNode): The internal graph node
        """
        self.state_row -= 1

    def move_down(self: StateGraphNode) -> None:
        """
        Moves the node down one

        Args:
            self (StateGraphNode): The internal graph node
        """
        self.state_row += 1

    def move_right(self: StateGraphNode) -> None:
        """
        Moves the node to the right

        Args:
            self (StateGraphNode): The internal graph node
        """
        self.state_col += 1

    def move_left(self: StateGraphNode) -> None:
        """
        Moves the node to the left

        Args:
            self (StateGraphNode): The internal graph node
        """
        self.state_col -= 1

    def already_visited(self: StateGraphNode) -> bool:
        """
        Determines if the coordinate has already been visited

        Args:
            self (StateGraphNode): The internal graph node state
        """
        return (self.state_row, self.state_col) in self.visited_coords
