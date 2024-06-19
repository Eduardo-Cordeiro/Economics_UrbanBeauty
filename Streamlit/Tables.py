import streamlit as st
import pandas as pd

neighborhoods = pd.read_csv("data_neighbors.csv")
macrozones = pd.read_csv("data_macrozones.csv")

st.table(neighborhoods)
