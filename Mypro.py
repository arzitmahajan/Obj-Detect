import cv2

#img = cv2.imread('test14.jpg')
cap =cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

classNames = []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip("\n").split("\n")
print(classNames)

configPath = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightPath = 'frozen_inference_graph.pb'
net = cv2.dnn_DetectionModel(weightPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)
while True:
    success,img = cap.read()
    classIDs,confs,bbox = net.detect(img,confThreshold=0.5)
    print(classIDs,bbox)

    for classID,confidence,box in zip(classIDs.flatten(),confs.flatten(),bbox):
        cv2.rectangle(img,box,color=(8,255,10),thickness=3)
        cv2.putText(img,classNames[classID-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    cv2.imshow('OUTPUT',img)
    cv2.waitKey(0)