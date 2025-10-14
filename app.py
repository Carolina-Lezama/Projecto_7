import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# cargar el dataframe
car_data = pd.read_csv('vehicles_us.csv')

# encabezado principal
st.header("Análisis de Venta de Coches")

# boton que construye un histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creando el histograma...')
    # creando con [st.plotly_chart()]
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    # añadir titulo
    fig.update_layout(title_text='Distribución')
    # mostrar y ajustar el ancho del contenedor
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir un grafico de dispersión')
if disp_button:
    st.write('Creando el gráfico de dispersión...')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                    y=car_data['price'], mode='markers+lines')])
    fig.update_layout(title_text='Dispersión entre odómetro y precio')
    st.plotly_chart(fig, use_container_width=True)

# ahora con checkboxes
histogram = st.checkbox('Crea histograma')
scatter = st.checkbox('Crear grafico de dispersion')

# Ejecutar según las selecciones
if histogram:
    st.write('Creando el histograma...')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución')
    st.plotly_chart(fig, use_container_width=True)

if scatter:
    st.write('Creando el gráfico de dispersión...')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                    y=car_data['price'], mode='markers+lines')])
    fig.update_layout(title_text='Dispersión entre odómetro y precio')
    st.plotly_chart(fig, use_container_width=True)
# las columnas seleccionadas fueron al azar
