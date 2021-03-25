import cv2 as cv
import numpy as np

class Maze:
    def __init__(self,pic):
        self.pic=pic
        self.image=cv.imread(pic)

    def maze_to_array(self):
        #image=cv.imread(pic)
        #cv.imshow("Image",image)

        img=cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
        #cv.imshow("Image_Gray",image)
        _,img=cv.threshold(img,199,255,cv.THRESH_BINARY)

        image_arr=np.array(img)
        return image_arr


    def write_on_maze(self,arr):
        for ind in range(1,len(arr)):
            cv.line(self.image,(arr[ind-1][1],arr[ind-1][0]),(arr[ind][1],arr[ind][0]),(111,111,111),thickness=1)
        
        cv.imwrite("maze_result.jpg",self.image)


#pic='demo_maze.jpg'
#print(maze_to_array(pic))