
def depthFirstSearch(matrix):
    stack=[]
    visited=[]


    visited.append(0)
    stack.append(0)

    while len(stack)!=0:

        k=stack[-1]

        for i in range(len(matrix[k])):
            if matrix[k][i]!=0 and (i not in visited):
                stack.append(i)
                visited.append(i)
                break
        else:
            stack.pop(-1)
        
        #print(stack)
        

    return visited



matrix=[[0,1,0,1,1,1],
        [1,0,1,0,0,0],
        [0,1,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0]]

print(depthFirstSearch(matrix))





        
    