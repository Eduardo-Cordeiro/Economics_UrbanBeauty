import streamlit as st
import pandas as pd

neighborhoods = pd.read_csv("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Data\\Data\\data_neighbors.csv")
macrozones = pd.read_csv("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Data\\Data\\data_macrozones.csv")

st.table(neighborhoods)