# submitted.py
# ---------------
# Licensing Information:
# This HW is inspired by previous work by University of Illinois at Urbana-Champaign


"""
This is the main entry point for MP5. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
# submitted should return the path.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,astar,astar_multi)

from collections import deque
import heapq


def bfs(maze):
    start = maze.start
    goal = maze.waypoints[0]

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for neighbor in maze.neighbors(*current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []

def astar_single(maze):
    start = maze.start
    goal = maze.waypoints[0]

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    priority_queue = [(0, start, [start])]
    visited = set()
    g_cost = {start: 0}

    while priority_queue:
        _, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for neighbor in maze.neighbors(*current):
            tentative_g_cost = g_cost[current] + 1

            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor, goal)
                heapq.heappush(priority_queue, (f_cost, neighbor, path + [neighbor]))

    return []


def dfs(maze):
    start = maze.start
    goal = maze.waypoints[0]

    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for neighbor in maze.neighbors(*current):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return []