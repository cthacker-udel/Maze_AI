from __future__ import annotations


class MapNode:
    """
        Represents a node in the map
    """

    def __init__(self: MapNode, row: int, col: int, cost: int = 1) -> None:
        """
        Initializes the MapNode

        Args:
            self (MapNode): The MapNode instance
            x (int): The x coordinate
            y (int): The y coordinate
            cost (int): The cost of the map node
        """
        self.row = row
        self.col = col
        self.cost = cost
        self.heuristic: int = 0

    def __str__(self: MapNode) -> str:
        """
        Overrides the stringified version of the node

        Returns:
            str: The stringified version of the node
        """
        return f"({self.row}, {self.col})"

    def __unicode__(self: MapNode) -> str:
        """
        Overrides the stringified version of the node

        Returns:
            str: The stringified version of the node
        """
        return f"({self.row}, {self.col})"

    def __repr__(self: MapNode) -> str:
        """
        Overrides the stringified version of the node

        Returns:
            str: The stringified version of the node
        """
        return f"({self.row}, {self.col})"
