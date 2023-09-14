from Map import Map
from helpers import generate_starting_point, generate_goal_point

if __name__ == '__main__':
    rows = 10
    cols = 10
    mp = Map(rows, cols)
    starting_coord = generate_starting_point(rows, cols)
    goal_coord = generate_goal_point(rows, cols, starting_coord)
    mp.assign_heuristics()
