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
        self.costs = []
        for i in range(n):
            for j in range(m):
                node_row.append(MapNode(i, j, generate_cost()))
            nodes.append(node_row[:])
            node_row = []
        self.nodes: List[List[MapNode]] = nodes
        self.current_coord: Tuple[int, int] = (-1, -1)
        self.goal_coord: Tuple[int, int] = (-1, -1)

        for each_row in self.nodes:
            sub_costs = []
            for each_node in each_row:
                sub_costs.append(each_node.cost)
            self.costs.append(sub_costs[:])

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
            stringified_costs += f'{i + 1}\t '
        stringified_costs += '\n'
        for each_row in self.nodes:
            stringified_costs += f'Row {row}\t'
            row += 1
            for each_node in each_row:
                stringified_costs += f'{each_node.cost}\t'
            stringified_costs += '\n'
        print(stringified_costs)

    def get_cost(self: Map, row: int, col: int) -> int:
        return self.nodes[row][col].cost

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
