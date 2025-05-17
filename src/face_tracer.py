import matplotlib.pyplot as plt
import cv2
from mtcnn import MTCNN

class FaceDetector:
    def __init__(self, path:str):
        self.detector = MTCNN()
        self.video = cv2.VideoCapture(path)
        if not self.video.isOpened():
            raise ValueError(f"Could not open video file: {path}")
        
        self.frame_count = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        self.current_frame = 0
        self.faces = dict()
        self.num_faces = 0
        
    def get_frame(self, time:int) -> None:
        self.video.set(cv2.CAP_PROP_POS_FRAMES, time * self.fps)
        ret, self.frame = self.video.read()
        if not ret:
            raise ValueError(f"Failed to read frame at {time} seconds")
    
    def release(self) -> None:
        self.video.release()
    
    def detect_faces(self, time:int) -> None:
        self.get_frame(time)
        rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        faces = self.detector.detect_faces(rgb)
        if not faces:
            raise ValueError("No faces detected")
        else:
            self.faces = faces
        self.num_faces = len(self.faces)
    
    def draw_faces(self,)-> None:
        for i, face in enumerate(self.faces):
            x, y, width, height = face['box']
            confidence = face['confidence']
            # Draw rectangle around the face
            cv2.rectangle(self.frame, (x, y), (x + width, y + height), (0, 255, 0), 1)
            
            label = f"Face #{i+1}: {confidence:.2f}"
            cv2.putText(self.frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            
            # Optionally, draw key facial points
            keypoints = face['keypoints']
            for point in keypoints.values():
                cv2.circle(self.frame, point, 2, (0, 255, 0), 2)

        plt.figure(figsize=(10, 8))
        plt.imshow(self.frame)
        plt.axis('off')
        plt.show()