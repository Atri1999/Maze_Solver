

class Node:
    def __init__(self,pos,side_values):
        self.pos=pos
        self.side_values=side_values

    def get_pos(self):
        return self.pos
    
    def get_side_values(self):
        return self.side_values


class Graph:
    
    nodes=[]
    graph=[]
    start_node=None
    end_node=None

    def __init__(self,arr):
        self.arr=arr          
        self.height=len(self.arr)
        self.breadth=len(self.arr[0])
        self.no_of_nodes=0
        

    def check_for_node(self,sv,y,x):
        if y==0 or y==self.height-1:
            return True

        c=sv.count(255)
        if c==3 or c==1:
            return True
        
        if c==4:
            return False

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


    def make_graph(self,node):
        ind=self.nodes.index(node)
        y,x=node.get_pos()
        
        top,_,_,left=node.get_side_values() 
        self.graph.append([ind])
        if top!=255 and left!=255:
            pass
        else:
            temp=0
            if top==255:
                k=y-1
                while k>=0:
                    
                    for n in range(ind):
                        if (k,x)==self.nodes[n].get_pos():
                            self.graph[n].append(ind)
                            self.graph[-1].append(n)
                            
                            temp=1
                            break
                    if temp==1:
                        break
                    k-=1
                            
                
                        
                

            temp=0
            if left==255:
                k=x-1
                while k>=0:
                    
                    for n in range(ind):
                        if (y,k)==self.nodes[n].get_pos():
                            self.graph[n].append(ind)
                            self.graph[-1].append(n)
                            
                            temp=1
                            break
                    if temp==1:
                        break
                    k-=1

                            


            





    def detect_nodes(self):  


        for y in range(self.height):
            for x in range(self.breadth):
                if self.arr[y][x]==255:
                    sv=self.side_values(y,x)
                    if self.check_for_node(sv,y,x):
                        self.nodes.append(Node((y,x),sv))
                        if y==0:
                            self.start_node=len(self.nodes)-1
                        if y==self.height-1:
                            self.end_node=len(self.nodes)-1
                        self.make_graph(self.nodes[-1])
                        self.no_of_nodes+=1


    def decode_node(self,directions):
        nodes_direction=[]
        for i in directions:
            nodes_direction.append(self.nodes[i].pos)
        
        return nodes_direction
        
        




