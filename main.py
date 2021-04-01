import read_maze as rm
import search 
import graphing as g
import time

pic='Maze_4.png'

start=time.perf_counter()
maze=rm.Maze(pic)
graph =g.Graph(maze.maze_to_array())


graph.detect_nodes()

#print(graph.no_of_nodes)
srh=search.Search(graph.start_node,graph.end_node,graph.graph)
result=graph.decode_node(srh.dfs())
maze.write_on_maze(result)

end=time.perf_counter()

print("The time required is :",(end-start))
