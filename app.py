import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st
vehi_data = pd.read_csv(
    r'C:\Users\fabri\Documents\VSC_projects\GitHub\vehicle_project\vehicles_project\vehicles_us.csv')
st.header('Sprint 7: Herramientas de desarrollo de software')
hist_cb = st.checkbox('Construir histograma')
if hist_cb:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de ventas de coches')
    fig = px.histogram(vehi_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
disp_cb = st.checkbox('Construir diagrama de dispersión')
if disp_cb:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de ventas de coches')
    fig = px.scatter(vehi_data, y='price', x='model_year')
    st.plotly_chart(fig, use_container_width=True)
