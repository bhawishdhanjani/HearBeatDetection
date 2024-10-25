# rppg.py
from collections import namedtuple
import numpy as np
import cv2
from detector import ROIDetector
class RPPG():
    def __init__(self, parent=None, video=1):
        super().__init__()
        self.detector = ROIDetector()
        self.signal = []
    def process_video(self, video_path):
        """Process the input video file frame by frame."""
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            raise RuntimeError("Error opening video file")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            rawimg = frame.copy()
            roimask, results = self.detector.process(frame)

            r, g, b, a = cv2.mean(rawimg, mask=roimask)
            self.signal.append(g)

            # Emit the results for each frame (if needed)
        cap.release()
        return self.calculate_average_heartbeat()
    def calculate_average_heartbeat(self):
        """Calculate average heartbeat from the signal."""
        if len(self.signal) == 0:
            return 0  
        average_heartbeat = np.mean(self.signal) 
        return average_heartbeat

