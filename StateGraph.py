from __future__ import annotations


class StateGraph:
    """
    Represents the graph of the states
    """

    def __init__(self: StateGraph, num_rows: int, num_cols: int) -> None:
        """
        Initializes the StateGraph

        Args:
            self (StateGraph): The graph containing all the states that are possible from a initial state
            num_rows (int): The number of rows in the maze
            num_cols (int): The number of columns in the maze
        """
        self.rows = num_rows
        self.cols = num_cols

    def is_node_in_bounds(self: StateGraph)
