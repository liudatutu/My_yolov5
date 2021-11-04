# import os
# from utils.autoanchor import kmean_anchors


# a=kmean_anchors()
# print(a)



import cv2
import os

imagedir='/home/ai/sda/MyCode/yolov5-master/datasets/coco128/images/train2017/*'
gtdir='/home/ai/sda/MyCode/yolov5-master/datasets/coco128/labels/train2017'

imagedir='/home/ai/版面分析/04.SS/yolo_test/img/*'
gtdir='/home/ai/版面分析/04.SS/yolo_test/gt'


imagedir='/home/ai/版面分析/05.五三/yolo_demo/train/*'
gtdir='/home/ai/版面分析/05.五三/yolo_demo/train_gt'


import glob 
for imgf in glob.glob(imagedir):
    imgbasename=os.path.basename(imgf)
    if imgbasename.startswith('1'):continue
    gtname=imgbasename.replace('jpg','txt')
    gtf=os.path.join(gtdir,gtname)
    img=cv2.imread(imgf)
    ih,iw=img.shape[:2]
    print(iw,ih)
    with open(gtf) as f:
        data=f.readlines()
        for m in data:
            m=m.strip()
            m=m.split(' ')
            m=[eval(i) for i in m]
            x,y,w,h=m[1:]
            print(x,y,w,h)
            xx=int(x*iw)
            yy=int(y*ih)
            ww=int(w*iw/2)
            hh=int(h*ih/2)
            print(xx)
            cv2.rectangle(img,(xx-ww,yy-hh),(xx+ww,yy+hh),(255,0,0),2)
            cv2.putText(img, str(m[0]),(xx,yy-hh+3),cv2.FONT_HERSHEY_COMPLEX,1.0, (0,0,255), 2)
    cv2.namedWindow('img',2)
    cv2.imshow('img',img)
    cv2.waitKey(0)
