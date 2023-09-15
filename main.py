from Map import Map
from helpers import generate_starting_point, generate_goal_point
from StateGraph import StateGraph

if __name__ == '__main__':
    rows = 5
    cols = 5
    mp = Map(rows, cols)
    starting_coord = generate_starting_point(rows, cols)
    goal_coord = generate_goal_point(rows, cols, starting_coord)
    mp.current_coord = starting_coord
    mp.goal_coord = goal_coord
    print('curr = ', mp.current_coord)
    mp.assign_heuristics()
    state = StateGraph(mp)
    state.compute_possible_states()
    print(state.current_node)
    print(state.goal_coord)
    if state.map is not None:
        state.map.print_out_costs()
