import streamlit as st
from ultralytics import YOLO
import av
import cv2
import pyttsx3
from streamlit_webrtc import webrtc_streamer,VideoProcessorBase
import time
import threading

st.title("Welcome To OculusAI.")
st.write("OculusAI - An AI Powered Vision Assistant for Visually Impaired.")

# Non-blocking voice function
def speak(text):
   def _speak():
      eng = pyttsx3.init()
      eng.setProperty("rate", 130)
      eng.say(text)
      eng.runAndWait()
   threading.Thread(target=_speak, daemon=True).start()

class VideoProcessor(VideoProcessorBase):
   def __init__(self):
      self.model = YOLO("yolov8n.pt")
      self.last_spoken_time = 0
      self.announced_objects = {}

   def recv(self, frame):
      image = frame.to_ndarray(format="bgr24")
      height, width, _ = image.shape
      results = self.model(image, verbose=False)
      annotated_image = results[0].plot()

      detected_announcements = []

      for box in results[0].boxes:
         x1, y1, x2, y2 = map(int, box.xyxy[0])
         class_id = int(box.cls[0])
         class_name = self.model.names[class_id]

         centre = (x1 + x2) // 2
         if centre < width // 3:
            direction = "Left"
         elif centre > (2 * width) // 3:
            direction = "Right"
         else:
            direction = "Centre"

         coordinates = f"({x1}, {y1}) - ({x2}, {y2}) | {direction}"
         cv2.putText(
            annotated_image,
            coordinates,
            (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
         )

         detected_announcements.append(f"{class_name} on your {direction}.")

      current_time = time.time()
      for item in detected_announcements:
         # Only announce if new, or not announced in the last 20 seconds
         if item not in self.announced_objects or (current_time - self.announced_objects[item] > 20):
            if current_time - self.last_spoken_time > 3:
               self.announced_objects[item] = current_time
               self.last_spoken_time = current_time
               speak(item)
               break

      return av.VideoFrame.from_ndarray(annotated_image, format="bgr24")


webrtc_streamer(
   key="oculusai-camera",
   video_processor_factory=VideoProcessor,
   media_stream_constraints={"video": True, "audio": False},
)
