import cv2 as cv
import numpy as np


def maze_to_array(pic):
    image=cv.imread(pic)
    #cv.imshow("Image",image)

    image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    #cv.imshow("Image_Gray",image)
    res,image=cv.threshold(image,199,255,cv.THRESH_BINARY)

    image_arr=np.array(image)
    return image_arr



#pic='demo_maze.jpg'
#print(maze_to_array(pic))