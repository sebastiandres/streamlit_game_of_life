from scipy.signal import convolve2d
import streamlit as st
import numpy as np
import time

def life_step(X):
    """Game of life step using scipy tools - jakevdp smart version"""
    nbrs_count = convolve2d(X, np.ones((3, 3)), mode='same', boundary='wrap') - X
    return (nbrs_count == 3) | (X & (nbrs_count == 2))

def next():
    A = st.session_state["matrix"]
    st.session_state["matrix"] = life_step(A)

def play():    
    while st.session_state["play"]:
        next()
        time.sleep(0.5)

def stop():
    st.session_state["play"] = False
    del st.session_state["play"]

# Set wide display
st.set_page_config(layout="wide")

# A boolean matrix of size 10x10
if "matrix" not in st.session_state:
    int_matrix = np.random.randint(0, 2, size=(15, 15))
    #int_matrix = np.zeros((15,15))
    st.session_state["matrix"] = int_matrix.astype(bool)


# Display the boolean matrix
c1, c2, c3 = st.columns(3)
c1.button("Next", on_click=next)
c2.button("Play", on_click=play)
c3.button("Stop", on_click=stop)


st.session_state["matrix"] = st.experimental_data_editor(st.session_state["matrix"], height=750, width=1000)
