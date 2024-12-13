import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('vehicles_us.csv')

# Crear el encabezado
st.header('Análisis Exploratorio de Datos: Vehículos')

# Casilla de verificación para el histograma de precios
build_histogram_price = st.checkbox('Construir Histograma de Precios')

if build_histogram_price:
    st.write('Creación de un histograma para la distribución de precios de vehículos')
    
    # Crear un histograma de precios
    fig_hist_price = px.histogram(
        df, 
        x='price', 
        title='Distribución de Precios de Vehículos',
        color='condition',  
        color_discrete_map={'excellent': '#32CD32', 'good': '#1E90FF', 'fair': '#FF4500', 'like new': '#FFD700'}
    )
    
    # Personalizar el fondo y mejorar la visualización
    fig_hist_price.update_layout(
        plot_bgcolor='#F5F5F5',  
        paper_bgcolor='white',  
        xaxis=dict(title='Precio'),  
        yaxis=dict(title='Frecuencia')
    )
    
    # Mostrar el gráfico de histograma de precios
    st.plotly_chart(fig_hist_price, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión entre odómetro y precio
build_scatter = st.checkbox('Construir Gráfico de Dispersión (Odómetro vs Precio)')

if build_scatter:
    st.write('Creación de un gráfico de dispersión entre el odómetro y el precio de los vehículos')
    
    # Crear gráfico de dispersión
    fig_scatter = px.scatter(
        df, 
        x='odometer', 
        y='price', 
        title='Relación entre Odómetro y Precio de Vehículos',
        color='condition',  
        color_discrete_map={'excellent': '#32CD32', 'good': '#1E90FF', 'fair': '#FF4500', 'like new': '#FFD700'}
    )
    
    # Personalizar el fondo y mejorar la visualización
    fig_scatter.update_layout(
        plot_bgcolor='#F5F5F5',  
        paper_bgcolor='white',  
        xaxis=dict(title='Kilometraje (Odómetro)'),  
        yaxis=dict(title='Precio')
    )
    
    # Agregar bordes a los puntos para mejorar la visibilidad
    fig_scatter.update_traces(marker=dict(line=dict(width=1.5, color='black')))  
    
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)

# Casilla de verificación para el histograma del año de modelo
build_histogram_year = st.checkbox('Construir Histograma del Año de Modelo')

if build_histogram_year:
    st.write('Creación de un histograma para la distribución del año de modelo de los vehículos')
    
    # Crear un histograma del año de modelo
    fig_hist_year = px.histogram(
        df, 
        x='model_year', 
        title='Distribución del Año de Modelo de los Vehículos',
        color='condition',  
        color_discrete_map={'excellent': '#32CD32', 'good': '#1E90FF', 'fair': '#FF4500', 'like new': '#FFD700'}
    )
    
    # Personalizar el fondo y mejorar la visualización
    fig_hist_year.update_layout(
        plot_bgcolor='#F5F5F5',  
        paper_bgcolor='white',  
        xaxis=dict(title='Año de Modelo'),  
        yaxis=dict(title='Frecuencia')
    )
    
    # Mostrar el gráfico de histograma del año de modelo
    st.plotly_chart(fig_hist_year, use_container_width=True)

# Casilla de verificación para el gráfico de barras por tipo de vehículo
build_bar_type = st.checkbox('Construir Gráfico de Barras por Tipo de Vehículo')

if build_bar_type:
    st.write('Creación de un gráfico de barras para la cantidad de vehículos por tipo')
    
    # Crear un gráfico de barras por tipo de vehículo
    fig_bar_type = px.bar(
        df, 
        x='type', 
        title='Cantidad de Vehículos por Tipo', 
        color_discrete_sequence=['#FF4500']
    )
    
    # Personalizar el fondo y mejorar la visualización
    fig_bar_type.update_layout(
        plot_bgcolor='#F5F5F5',  
        paper_bgcolor='white',  
        xaxis=dict(title='Tipo de Vehículo'),   
        yaxis=dict(title='Cantidad de Vehículos'),  
        bargap=0.2  
    )
    
    # Agregar bordes a las barras para mayor contraste
    fig_bar_type.update_traces(marker=dict(line=dict(width=1.5, color='black')))  
    
    # Mostrar el gráfico de barras por tipo
    st.plotly_chart(fig_bar_type, use_container_width=True)

# Casilla de verificación para el gráfico de barras por condición de vehículo
build_bar_condition = st.checkbox('Construir Gráfico de Barras por Condición de Vehículo')

if build_bar_condition:
    st.write('Creación de un gráfico de barras para la distribución de las condiciones de los vehículos')
    
    # Crear un gráfico de barras por condición de vehículo
    fig_bar_condition = px.bar(
        df, 
        x='condition', 
        title='Distribución de las Condiciones de los Vehículos', 
        color_discrete_sequence=['#1E90FF']
    )
    
    # Personalizar el fondo y mejorar la visualización
    fig_bar_condition.update_layout(
        plot_bgcolor='#F5F5F5',  
        paper_bgcolor='white',  
        xaxis=dict(title='Condición del Vehículo'),  
        yaxis=dict(title='Cantidad de Vehículos'),  
        bargap=0.2  
    )
    
    # Agregar bordes a las barras para mayor contraste
    fig_bar_condition.update_traces(marker=dict(line=dict(width=1.5, color='black')))  
    
    # Mostrar el gráfico de barras por condición
    st.plotly_chart(fig_bar_condition, use_container_width=True)
