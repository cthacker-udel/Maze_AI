from __future__ import annotations
from MapNode import MapNode
from helpers import generate_cost, compute_manhattan_distance
from typing import Tuple, Optional, List


class Map:
    """
    Represents a map instance
    """

    def __init__(self: Map, n: int, m: int) -> None:
        """
        Initializes the map instance

        Args:
            self (Map): The map instance
            n (int): The # of rows
            m (int): The # of columns
        """
        self.rows = n
        self.cols = m
        nodes = []
        node_row = []
        for i in range(n):
            for j in range(m):
                node_row.append(MapNode(i, j, generate_cost()))
            nodes.append(node_row[:])
            node_row = []
        self.nodes: List[List[MapNode]] = nodes
        self.current_coord: Optional[Tuple[int, int]] = None
        self.goal_coord: Optional[Tuple[int, int]] = None

    def update_coords(self: Map, start_coord: Tuple[int, int], goal_coord: Tuple[int, int]) -> None:
        """
        Updates the starting and ending coordinates of the Map

        Args:
            self (Map): The map instance
            start_coord (Tuple[int, int]): The starting coordinate
            goal_coord (Tuple[int, int]): The ending coordinate
        """
        self.current_coord = start_coord
        self.goal_coord = goal_coord

    def print_out_costs(self: Map) -> None:
        """
        Prints out all the costs in the map

        Args:
            self (Map): The internal map state
        """
        row = 1
        cols = self.cols
        stringified_costs = '\t Col 1'
        for i in range(1, cols):
            stringified_costs += f'Col {i + 1}\t'
        stringified_costs += '\n'
        for each_row in self.nodes:
            stringified_costs += f'Row {row}\t'
            row += 1
            for each_node in each_row:
                stringified_costs += f'{each_node.cost}\t'
            stringified_costs += '\n'
        print(stringified_costs)

    def __str__(self: Map) -> str:
        """
        Returns a stringified version of the map

        Args:
            self (Map): The map to stringify

        Returns:
            str: The string version of the map
        """
        row = 1
        stringified_map = '\t'
        for j in range(self.cols):
            stringified_map += f'Col {row}\t'
            row += 1
        stringified_map += '\n'
        row = 1
        for i in range(self.rows):
            stringified_map += f'Row {row}\t'
            for j in range(self.cols):
                stringified_map += f'{self.nodes[i][j]}\t'
            stringified_map += '\n'
            row += 1
        return stringified_map

    def __repr__(self: Map) -> str:
        """
        Returns a stringified version of the map

        Args:
            self (Map): The map to stringify

        Returns:
            str: The string version of the map
        """
        row = 1
        stringified_map = ''
        for i in range(self.rows):
            stringified_map += f'Row {row}\t'
            for j in range(self.cols):
                stringified_map += f'{self.nodes[i][j]}\t'
            stringified_map += '\n'
        return stringified_map

    def __unicode__(self: Map) -> str:
        """
        Returns a stringified version of the map

        Args:
            self (Map): The map to stringify

        Returns:
            str: The string version of the map
        """
        row = 1
        stringified_map = ''
        for i in range(self.rows):
            stringified_map += f'Row {row}\t'
            for j in range(self.cols):
                stringified_map += f'{self.nodes[i][j]}\t'
            stringified_map += '\n'
        return stringified_map

    def assign_heuristics(self: Map) -> None:
        """
        Assigns the heuristics to each node

        Args:
            self (Map): The map instance
        """
        if self.goal_coord is None:
            return None

        for each_row in self.nodes:
            for each_node in each_row:
                dist = compute_manhattan_distance(
                    (each_node.row, each_node.col), (self.goal_coord[0], self.goal_coord[1]))
                each_node.heuristic = dist
