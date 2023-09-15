from __future__ import annotations
from typing import List, Tuple, Optional
from MapNode import MapNode
from MovementType import MovementType


class StateGraphNode:
    """
    Represents a single state in the maze
    """

    def __init__(self: StateGraphNode, node: Optional[Tuple[int, int]], visited: Optional[List[Tuple[int, int]]] = None) -> None:
        """
        Initializes a state graph node

        Args:
            self (StateGraphNode): The internal instance of the state graph node
        """
        if visited is not None:
            print('visited = ', len(visited))
        self.row: int = node[0] if node is not None else 0
        self.col: int = node[1] if node is not None else 0
        self.visited_coords: List[Tuple[int, int]] = [
            (self.row, self.col)] if visited is None else visited + [(self.row, self.col)]
        self.total_cost = 0

    def move_up(self: StateGraphNode) -> StateGraphNode:
        """
        Moves the node up one

        Args:
            self (StateGraphNode): The internal graph node
        """
        up_node = StateGraphNode((self.row - 1, self.col), self.visited_coords)
        return up_node

    def move_down(self: StateGraphNode) -> StateGraphNode:
        """
        Moves the node down one

        Args:
            self (StateGraphNode): The internal graph node
        """
        down_node = StateGraphNode(
            (self.row + 1, self.col), self.visited_coords)
        return down_node

    def move_right(self: StateGraphNode) -> StateGraphNode:
        """
        Moves the node to the right

        Args:
            self (StateGraphNode): The internal graph node
        """
        right_node = StateGraphNode(
            (self.row, self.col + 1), self.visited_coords)
        return right_node

    def move_left(self: StateGraphNode) -> StateGraphNode:
        """
        Moves the node to the left

        Args:
            self (StateGraphNode): The internal graph node
        """
        left_node = StateGraphNode(
            (self.row, self.col - 1), self.visited_coords)
        return left_node

    def is_move_in_bounds(self: StateGraphNode, rows: int, cols: int) -> bool:
        """
        Computes whether this is a valid move

        Args:
            self (StateGraphNode): The internal state
            rows (int): The # of rows in the maze
            cols (int): The # of cols in the maze

        Returns:
            bool: Whether this is a valid move
        """
        return self.is_in_bounds(rows, cols)

    def already_visited(self: StateGraphNode) -> bool:
        """
        Determines if the coordinate has already been visited

        Args:
            self (StateGraphNode): The internal graph node state
        """
        return (self.row, self.col) in self.visited_coords

    def already_visited_node(self: StateGraphNode, node: StateGraphNode) -> bool:
        """
        Checks if a node that is passed in, contains coordinates that this node has already visited

        Args:
            self (StateGraphNode): The internal state
            node (StateGraphNode): The node we are checking if it has already been visited

        Returns:
            bool: Whether the node has already been visited
        """
        return (node.row, node.col) in self.visited_coords

    def is_in_bounds(self: StateGraphNode, rows: int, cols: int) -> bool:
        """
        Determines if this node is in bounds

        Args:
            self (StateGraphNode): The internal graph node state
            rows (int): The # of rows in the map
            cols (int): The # of columns in the map

        Returns:
            bool: Whether the node is in bounds
        """
        if self.row >= rows:
            return False

        if self.col >= cols:
            return False

        if self.row < 0:
            return False

        if self.col < 0:
            return False
        return True

    def __str__(self: StateGraphNode) -> str:
        return f'({self.row}, {self.col})'

    def __unicode__(self: StateGraphNode) -> str:
        return f'({self.row}, {self.col})'

    def __repr__(self: StateGraphNode) -> str:
        return f'({self.row}, {self.col})'

    def is_move_valid(self: StateGraphNode, move_type: MovementType) -> bool:
        """
        Determines if a movement type is valid

        Args:
            self (StateGraphNode): The internal state
            move_type (int): The type of movement being requested

        Returns:
            bool: Whether the movement is valid
        """
        if move_type == MovementType.UP:
            return (self.row - 1, self.col) not in self.visited_coords
        elif move_type == MovementType.DOWN:
            return (self.row + 1, self.col) not in self.visited_coords
        elif move_type == MovementType.LEFT:
            return (self.row, self.col - 1) not in self.visited_coords
        else:
            return (self.row, self.col + 1) not in self.visited_coords
