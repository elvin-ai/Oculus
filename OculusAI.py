import streamlit as st
import pyttsx3
from ultralytics import YOLO
import cv2
import numpy as np
import pandas as pd
from PIL import Image

st.title("Welcome To OculusAI.")
st.write("OculusAI - An AI Powered Vision Assistant for Visually Impaired.")

cap=cv2.VideoCapture(1)

vh = st.empty()
model=YOLO("yolov8n.pt")
engine=pyttsx3.init()

threshold=0.75

start=st.button("Start Camera")
stop=st.button("Stop Camera")

if start : 
    for i in range(100) : 
       ret,frame=cap.read()
       frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

       if not ret :
        break

       result=model(frame)
       detections=[]

       for box in result[0].boxes :
        b=float(box.conf)
        
        if b>threshold :
            id=int(box.cls[0])
            name=model.names[id]
            annotate=result[0].plot()
            vh.image(annotate)
            detections.append([name,id])

    df=pd.DataFrame(detections,columns=["Object","Confidence"])
    st.dataframe(df)


cap.release()
cv2.destroyAllWindows()