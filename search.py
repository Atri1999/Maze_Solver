class Search:

    def __init__(self,start,end,graph):
        self.start=start
        self.end=end
        self.graph=graph
        self.nodes=len(graph)
        self.result=[]

    def dfs(self):
        stack=[]
        visited=[]

        stack.append(self.start)
        visited.append(self.start)

        while stack[-1]!=self.end:

            temp=stack[-1]

            for k in range(1,len(self.graph[temp])):
                if self.graph[temp][k] not in visited:
                    stack.append(self.graph[temp][k])
                    visited.append(self.graph[temp][k])
                    break
            else:
                stack.pop(-1)

        
        return stack


"""graph=[[0,1,2],
        [1,3],
        [2,4],
        [3,5],
        [4,2],
        [5,3]]

se=Search(0,4,graph)

print(se.dfs())"""

