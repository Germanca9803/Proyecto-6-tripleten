import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Mi proyecto sprint 6!")

car_data = pd.read_csv('./vehicles_us.csv')  # leer los datos

st.header("Elige que casilla deseas construir:")

build_bar_graph = st.checkbox('Construir un grafico de barras')
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un grafico de dispersion')

if build_histogram:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x=(
        ['odometer', 'price']), title='Histogramas')
    fig.show()

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_bar_graph:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafico de barras para el conjunto de datos por tipo de transmicion')

    # crear un grafico de barras
    df = car_data.groupby('transmission').count()
    fig3 = px.bar(df, y=(['price', 'fuel']))

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)

if build_scatter:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creacion de un grafico de dispersion'
    )
    # crear un grafico de barras
    fig2 = px.scatter(car_data, x="model_year", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("<p style='color:red'>Hecho por German Camacho Angulo</p>")
