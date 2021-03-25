import read_maze as rm
import search 
import graphing as g


pic='demo_maze.jpg'
maze=rm.Maze(pic)
graph =g.Graph(maze.maze_to_array())

graph.detect_nodes()

srh=search.Search(graph.start_node,graph.end_node,graph.graph)
result=graph.decode_node(srh.dfs())
maze.write_on_maze(result)