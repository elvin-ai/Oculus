import streamlit as st
import pyttsx3

st.title("Welcome to Oculus")
st.header("Streamlit Test")
st.write("If you can see this, Streamlit is working successfully!")

engine=pyttsx3.init()


name = st.text_input("Enter your name:")

if name:
    engine.say(f"Hello, {name}!")
    engine.runAndWait()