import streamlit as st
import pyttsx3
from ultralytics import YOLO
import cv2
import numpy as np
import pandas as pd
from PIL import Image

st.title("Welcome To OculusAI.")
st.write("OculusAI - An AI Powered Vision Assistant for Visually Impaired.")

vh = st.empty()
model=YOLO("yolov8n.pt")
engine=pyttsx3.init()
cap=cv2.VideoCapture(1)

threshold=0.75

while(True) :
    ret,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    if not ret :
        break
    result=model(frame)
    for box in result[0].boxes :
        b=float(box.conf)

        if b>threshold :
            annotate=result[0].plot()

        vh.image(annotate)

    
cap.release()
cv2.destroyAllWindows()