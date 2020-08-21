import numpy as np
import cv2 as cv
import time
from Helmet_detection_YOLOV3 import dock
#调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
cap=cv.VideoCapture(0)

while True:
    #从摄像头调取图片
    sucess,img=cap.read()
    #调用封装函数处理图像
    img = dock(img)
    #显示图像
    cv.imshow("img",img)
    #保持画面的持续。
    k=cv.waitKey(100)
    # print(k)
    if k == 27: 
        #通过esc键退出摄像
        cv.destroyAllWindows()
        break
    elif k == ord("s"):
        t = time.time()
        #通过s键保存图片，并退出。
        cv.imwrite("save/"+str(t)+".jpg",img)
        # cv.destroyAllWindows()
        # break
#关闭摄像头
cap.release()

