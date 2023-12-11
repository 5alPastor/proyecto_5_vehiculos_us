#importar librerías 
import streamlit as st
import pandas as pd
import plotly.express as px


#leer archivo con los datos
car_data = pd.read_csv(r'C:\Users\jmrg2\Documents\Data analitics\proyectos\5to proyecto\Entorno virtual\proyecto_autos_us\proyecto_5_vehiculos_us\vehicles_us.csv')


#header
st.header('Información sobre precios de vehículos')


hist_button = st.button('Frecuencia de Precios de Vehículos (histograma)') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma con precio de los autos')
            
    # crear un histograma
    fig = px.histogram(car_data, x="price", labels={'price':'Precio'})
    
    #Cambiar el nombre del eje Y
    fig.update_layout(
    yaxis_title="Frecuencia")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 
            

dispersion_button = st.button('Información Sobre el Modelo de los Autos Por Año vs su Precio(Gráfico de Dispersión)') # crear un botón

if dispersion_button:
    #escribir mensaje
    st.write('Creación de un gráfico de dispersión que relaciona año del modelo los automoviles y su precio')
    
    #crear gráfico de  dispersión
    fig = px.scatter(car_data, x="model_year", y="price", title = "Gráfico de Dispersión", labels={'price': 'Precio', 'model_year': 'Modelo(año)'})
      
    #"mostrar un gráfico  Plotly interactivo"
    st.plotly_chart(fig, use_container_width=True)