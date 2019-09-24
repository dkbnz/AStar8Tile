from queue import *
import math
from collections import namedtuple

def graph_search(graph, frontier):
    """Generic algorithm used to search a graph.
    The search behaviour is determined based on the frontier provided"""

    # Add starting node to the frontier
    frontier.add((Edge(None, graph.start_node(), "No action", 0),))

    for path in frontier:
        nodeToExpand = path[-1].head # Head of last edge in current path

        if graph.is_goal(nodeToExpand):
            yield path # Have reached goal, yield path

        for edge in graph.outgoing_edges(nodeToExpand):
            # Add all outgoing edges from current node being expanded
            frontier.add(path + (edge,))


class Edge(namedtuple('Edge', 'tail, head, label, cost')):
    """Used to represent an edge in a state graph

    Arguments:
    tail - Source node (state)
    head -- Destination node (state)
    label -- String representing action to get from tail state to head state
    cost -- Number that specifies the cost of the action
    """

class AStarFrontier():
    """Implements a frontier container appropriate for A* Search"""

    def __init__(self, graph):
        """"Initialise an instance the frontier"""
        self.container = PriorityQueue()
        self.graph = graph
        self.visited = set()
        self.count = 0

    def add(self, path):
        """Add a path to the frontier if the end node has not been visited"""
        node = path[-1].head
        if node not in self.visited:
            fcost = sum(edge.cost for edge in path) + self.graph.estimated_cost_to_goal(node)
            self.count += 1
            self.container.put((fcost, self.count, path))

    def __iter__(self):
        """Iterates through the frontier and yields each path
        if the end node has not already been visited
        """
        while not self.container.empty():
            _, _, path = self.container.get()
            node = path[-1].head
            if node not in self.visited:
                yield path
                self.visited |= {node}


class TileGraph():
    """This class takes a state of a tile game and implicitly generates possible moves"""

    def __init__(self, start):

        # Find the location of the 'empty' tile.
        for i, row in enumerate(start):
            for j, char in enumerate(row):
                if char == 0:
                    break
            if char == 0:
                break

        self.startnode = (start, j, i)
        self.goalnode = ((
                        (0, 1, 2),
                        (3, 4, 5),
                        (6, 7, 8)
                        ), 0, 0)

        self.perfect = {
        0 : (0, 0), 1 : (1, 0), 2 : (2, 0),
        3 : (0, 1), 4 : (1, 1), 5 : (2, 1),
        6 : (0, 2), 7 : (1, 2), 8 : (2, 2)
        }

    def outgoing_edges(self, node):
        """Implicitly generates outgoing edges based on the
        given nodes location on the map"""

        # Movements given as move x, move y
        movements = ((0, 1), (0, -1), (1, 0), (-1, 0))

        tilestate, blankx, blanky = node

        for movex, movey in movements:
            if (0 <= blankx + movex <= 2) and (0 <= blanky + movey <= 2):
                outnode = self.move(tilestate, blankx, blanky, movex, movey)
                yield Edge(node, outnode, self.movestr(tilestate, outnode[0]), 1)

    def movestr(self, tilestate, newstate):
        chars = "(),"
        template = "\n  {0}    {3}\n  {1} -> {4}\n  {2}    {5}"
        template = template.format(*tilestate, *newstate)

        for char in chars:
            template = template.replace(char, '')

        return template.replace('0', ' ')


    def move(self, tilestate, blankx, blanky, movex, movey):
        """Generates a new tile state given parameters
        Arguments:
        tilestate - Tile state to be altered depending on movex, movey
        blankx, blanky - current coordinate of the blank tile in the tilestate
        movex, movey - amount to move the blank tile in the tilestate
        """
        newx, newy = blankx + movex, blanky + movey
        newstate = (list(tilestate[0]), list(tilestate[1]), list(tilestate[2]))
        newstate[newy][newx], newstate[blanky][blankx] = tilestate[blanky][blankx], tilestate[newy][newx]
        newstate = (tuple(newstate[0]), tuple(newstate[1]), tuple(newstate[2]))

        return (newstate, newx, newy)

    def start_node(self):
        """Return the starting node of the graph"""
        return self.startnode

    def is_goal(self, node):
        """Checks if the node is a goal node"""
        return node == self.goalnode

    def estimated_cost_to_goal(self, node):
        """Return an estimate to get to the goal node
        This returns the total manhattan distance required to get each tile
        into its respective final position
        """
        mincost = 0
        state, _, _ = node

        for i, row in enumerate(state):
            for j, tile in enumerate(row):
                mincost += abs(j - self.perfect[tile][0]) + abs(i - self.perfect[tile][1])

        return mincost
