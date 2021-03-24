def breadthFirstSearch(matrix):
    queue=[]
    visited=[]

    queue.append(0)

    while len(queue)>0:

        k=queue.pop(0)
        if k not in visited:
            visited.append(k)

            for i in range(len(matrix[k])):
                if matrix[k][i]==1 and (i not in visited):
                    queue.append(i)
                    #print(queue)
        
        
    return visited

matrix=[[0,0,0,0,1,1],
        [0,0,1,0,0,0],
        [0,1,0,0,0,1],
        [0,0,0,0,1,1],
        [1,0,0,1,0,0],
        [1,0,1,1,1,0]]

print(breadthFirstSearch(matrix))
