from __future__ import annotations
from Map import Map
from typing import List, Optional, Tuple
from helpers import move_node
from MapNode import MapNode
from MovementType import MovementType


class StateGraph:
    """
    Represents the graph of the states
    """

    def __init__(self: StateGraph, state: Map) -> None:
        self.rows = state.rows
        self.cols = state.cols
        self.map = state
        self.current_node = MapNode(
            state.current_coord[0], state.current_coord[1])
        self.left_move: Optional[StateGraph] = None
        self.right_move: Optional[StateGraph] = None
        self.down_move: Optional[StateGraph] = None
        self.up_move: Optional[StateGraph] = None

    def clone(self: StateGraph) -> StateGraph:

        if self.current_node is None:
            return self

        cloned_node = MapNode(self.current_node.row, self.current_node.col)
        sm = StateGraph(self.map)
        sm.current_node = cloned_node

        return sm

    def move(self: StateGraph, movement: MovementType) -> StateGraph:
        cloned_graph = self.clone()
        moved_coordinates = move_node(cloned_graph.current_node, movement)
        cloned_graph.current_node.row = moved_coordinates[0]
        cloned_graph.current_node.col = moved_coordinates[1]
        cloned_graph.current_node.cost += self.map.get_cost(
            cloned_graph.current_node.row, cloned_graph.current_node.col)
        return cloned_graph
