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

cap=cv2.VideoCapture(1)

while(True) :
    ret,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    if not ret :
        break

    vh.image(frame)
    result=model(frame)

cap.release()
cv2.destroyAllWindows()