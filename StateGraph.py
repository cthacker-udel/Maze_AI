from __future__ import annotations
from Map import Map
from typing import List, Optional, Tuple
from StateGraphNode import StateGraphNode
from MapNode import MapNode
from MovementType import MovementType


class StateGraph:
    """
    Represents the graph of the states
    """

    def __init__(self: StateGraph, state: Optional[Map] = None, current_node: Optional[StateGraphNode] = None, rows=0, cols=0) -> None:
        """
        Initializes the StateGraph

        Args:
            self (StateGraph): The graph containing all the states that are possible from a initial state
            num_rows (int): The number of rows in the maze
            num_cols (int): The number of columns in the maze
        """
        self.rows = state.rows if state is not None else rows
        self.cols = state.cols if state is not None else cols
        self.map: Optional[Map] = state if state is not None else None
        self.current_node: Optional[StateGraphNode] = StateGraphNode(
            state.current_coord) if state is not None else current_node if current_node is not None else None
        self.states: List[StateGraph] = []
        self.goal_coord: Optional[Tuple[int, int]
                                  ] = state.goal_coord if state is not None else None

    def is_node_in_bounds(self: StateGraph) -> bool:
        """
        Determines if the node the map solver is currently on is in bounds

        Args:
            self (StateGraph): The current state

        Returns:
            bool: Whether the current node the map solver is on is in bounds
        """
        if self.current_node is None:
            return False

        if self.current_node.row >= self.rows or self.current_node.col >= self.cols:
            return False

        if self.current_node.row < 0 or self.current_node.col < 0:
            return False

        return True

    def is_at_goal(self: StateGraph) -> bool:
        """
        Computes if the current node is at the goal

        Args:
            self (StateGraph): The internal graph state
        """
        if self.goal_coord is None or self.current_node is None:
            return False

        return self.current_node.row == self.goal_coord[0] and self.current_node.col == self.goal_coord[1]

    def add_cost_to_node(self: StateGraph) -> None:
        """
        Attempts to add the cost to the current node in the graph

        Args:
            self (StateGraph): The internal graph state
        """
        if self.map is None or self.current_node is None:
            return None

        self.current_node.total_cost += self.map.nodes[self.current_node.row][self.current_node.col].cost

    def compute_possible_states(self: StateGraph) -> None:
        """
        Computes all the possible states that can be achieved from a singular node

        Args:
            self (StateGraph): The state graph
        """
        if self.current_node is None:
            return None

        is_left_valid = self.current_node.is_move_valid(MovementType.LEFT)
        is_right_valid = self.current_node.is_move_valid(MovementType.RIGHT)
        is_down_valid = self.current_node.is_move_valid(MovementType.DOWN)
        is_up_valid = self.current_node.is_move_valid(MovementType.UP)

        left_movement = self.current_node.move_left()
        right_movement = self.current_node.move_right()
        down_movement = self.current_node.move_down()
        up_movement = self.current_node.move_up()

        if is_left_valid and not self.current_node.already_visited_node(left_movement) and left_movement.is_move_in_bounds(self.rows, self.cols):
            # add left movement to state
            left_state = StateGraph(
                None, left_movement, self.rows, self.cols)

            left_state.add_cost_to_node()
            self.states.append(left_state)
            if self.map is not None:
                self.map.nodes[left_movement.row][left_movement.col].cost = min(
                    left_movement.total_cost, self.map.nodes[left_movement.row][left_movement.col].cost)

            if not left_state.is_at_goal():
                left_state.compute_possible_states()

        if is_right_valid and not self.current_node.already_visited_node(right_movement) and right_movement.is_move_in_bounds(self.rows, self.cols):
            # add right movement to state
            right_state = StateGraph(
                None, right_movement, self.rows, self.cols)

            right_state.add_cost_to_node()
            self.states.append(right_state)
            if self.map is not None:
                self.map.nodes[right_movement.row][right_movement.col].cost = min(
                    right_movement.total_cost, self.map.nodes[right_movement.row][right_movement.col].cost)

            if not right_state.is_at_goal():
                right_state.compute_possible_states()

        if is_down_valid and not self.current_node.already_visited_node(down_movement) and down_movement.is_move_in_bounds(self.rows, self.cols):
            # add down movement to state
            down_state = StateGraph(
                None, down_movement, self.rows, self.cols)

            self.states.append(down_state)
            down_state.add_cost_to_node()
            if self.map is not None:
                self.map.nodes[down_movement.row][down_movement.col].cost = min(
                    down_movement.total_cost, self.map.nodes[down_movement.row][down_movement.col].cost)

            if not down_state.is_at_goal():
                down_state.compute_possible_states()

        if is_up_valid and not self.current_node.already_visited_node(up_movement) and up_movement.is_move_in_bounds(self.rows, self.cols):
            # add up movement to state
            up_state = StateGraph(
                None, up_movement, self.rows, self.cols)

            self.states.append(up_state)
            up_state.add_cost_to_node()
            if self.map is not None:
                self.map.nodes[up_movement.row][up_movement.col].cost = min(
                    up_movement.total_cost, self.map.nodes[up_movement.row][up_movement.col].cost)

            if not up_state.is_at_goal():
                up_state.compute_possible_states()
