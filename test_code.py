from tile_solve import *

def print_actions(path):
    """Given a path (a sequence of Edge objects), prints the actions
    (edge labels) that need to be taken and the total cost of those
    actions. The path is usually a solution (a path from the starting
    node to a goal node."""

    if path:
        print("Actions:")
        print("\n".join("  {}".format(arc.label) for arc in path[1:]) + "\n")
        print("Total cost:", sum(arc.cost for arc in path), "moves.")
    else:
        print("There is no solution!")

# 25 moves to solve
# start = ((5, 7, 8),
#          (0, 2, 6),
#          (4, 1, 3))

# No solution
# start = ((0, 4, 2),
#          (6, 3, 7),
#          (8, 5, 1))

# 10 moves to solve
start = ((1, 4, 2),
         (6, 3, 7),
         (8, 5, 0))

tilegraph = TileGraph(start)
frontier = AStarFrontier(tilegraph)

solution = next(graph_search(tilegraph, frontier), None)
print_actions(solution)

# We can even fetch the next solution.
# solution = next(graph_search(tilegraph, frontier), None)
# print_actions(solution)
