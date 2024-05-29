import maze
maze1 = maze.Maze('data/part-1/small')
print(maze1[0, 0] == maze1.legend.wall)
print(maze1[1, 1] == maze1.legend.wall)
print(maze1[3, 11] == maze1.legend.start)
print(maze1[8, 1] == maze1.legend.waypoint)

# Coordinate of the starting position
print(maze1.start)

# Coordinate of the waypoint position
print(maze1.waypoints)

print(list(maze1.indices()))

# Takes (i, j) coordinates (as separate arguments), and returns a bool indicating 
# if the corresponding cell is navigable (meaning the agent can move into it). 
# All cells except for wall cells are navigable.
print(maze1.navigable(1, 1))

# Takes (i, j) coordinates (as separate arguments), and returns a tuple containing a sequence 
# of the coordinates of all the navigable neighbors of the given cell. A cell can have at most 4 neighbors.
print(maze1.neighbors(3, 11))

# Keeps track of the number of cells visited in this maze. Each call to neighbors(_:_:) 
# increments this value by 1. We will utilize this value to test if you are expanding 
#the correct number of states, so do not call neighbors(_:_:) any more than necessary.
print(maze1.states_explored)
print(maze1.neighbors(3, 12))
print(maze1.states_explored)

# Validates a path through the maze. This method returns None if the path is valid, 
# and an error message of type str otherwise.

path = [(3,11), (3,12), (3,13)]
print(maze1.validate_path(path))


