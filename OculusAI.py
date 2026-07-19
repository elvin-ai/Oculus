import streamlit as st
import pyttsx3
from ultralytics import YOLO
import cv2


model=YOLO("yolov8n.pt")

