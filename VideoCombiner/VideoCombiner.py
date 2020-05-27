import os 
from cv2 import cv2
import numpy as np 

class VideoCombiner(object):

    def __init__(self, inputDir, outputFile, dataType=".mp4"):
        self.inputDir = inputDir
        self.outputFile = outputFile

        self.video = self.getVideo(dataType)

    def getVideo(self, dataType):
        fileLists = os.listdir(self.inputDir)
        fileLists = [self.inputDir+"/"+f for f in fileLists if(f[-len(dataType)::].lower()==dataType)]

        cap = cv2.VideoCapture(fileLists[0])
        cap.release()
        out = cv2.VideoWriter(self.outputFile, -1, int(cap.get(cv2.CAP_PROP_FPS)), (int(cap.get(3)), int(cap.get(4))))

        for i in fileLists:
            cap = cv2.VideoCapture(i)
            # print(cap.get(3), cap.get(4), cap.get(cv2.CAP_PROP_FPS))
            # print("video",i)
            while(cap.isOpened()):
                ret, frame = cap.read()
                cv2.imshow('Recording...', frame)
                # print(np.shape(frame))
                out.write(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                if(not ret):
                    break
            cap.release()
            
        out.release()
        return out
            

if __name__ == "__main__":
    a = VideoCombiner("D:/GoogleDrive/Media/123", "C:/Users/zxcv1/desktop/out.mp4")
    # print(a.videoList)