import read_maze as rm

class Node:
    def __init__(self,pos,side_values):
        self.pos=pos
        self.side_values=side_values

    def get_pos(self):
        return self.pos
    
    def get_side_values(self):
        return self.side_values


class Graph:
    
    
    def __init__(self,pic):
        self.arr= rm.maze_to_array(pic)         
        self.height=len(self.arr)
        self.breadth=len(self.arr[0])
        self.nodes=[]

    def check_for_node(self,sv,y,x):
        if y==0 or y==self.height-1:
            return True

        c=sv.count(255)
        if c>=3 or c==1:
            return True

        fi=sv.index(255)
        if sv[fi-1]==255 or sv[fi+1]==255:
            return True

        return False



    def side_values(self,y,x):
        if y==0:
            top=-1
        else:
            top=self.arr[y-1][x]
        
        if x==0:
            left=-1
        else:
            left=self.arr[y][x-1]

        if y==self.height-1:
            bottom=-1
        else:
            bottom=self.arr[y+1][x]
        
        if x==self.breadth-1:
            right=-1
        else:
            right=self.arr[y][x+1]

        return [top, right, bottom, left]

    def make_graph((y,x),sv):
        top,right,bottom,left=sv 
        if top!=255 and left!=255:
            pass





    def detect_nodes(self):  


        for y in range(self.height):
            for x in range(self.breadth):
                if self.arr[y][x]==255:
                    sv=self.side_values(y,x)
                    if self.check_for_node(sv,y,x):
                        self.nodes.append(Node((y,x),sv))

        
        return self.nodes


pic='demo_maze.jpg'
gr=Graph(pic)
k=gr.detect_nodes()
for ki in k:
    print(ki.get_pos(),end=",")

print()
print(len(k))