import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from time import sleep


import src.geocode as geo
import src.distancia as dis
import src.folium as fm

# IMPORTANDO NUESTROS DATOS LIMPIOS
centros_medicos_clean = pd.read_csv("data/centros_medicos_clean.csv")
farmacias_clean = pd.read_csv("data/farmacias_clean.csv")




st.markdown("<h1 style='text-align: center; color: black;'>Drugs delivery?</h1>", unsafe_allow_html=True)


# FOTO DE PORTADA Y TEXTO INTRODUCTORIO
image = Image.open('input/deliverybike.png')
st.image (image,use_column_width=True)
st.write(
"""
Este proyecto te va a ofrecer una nueva idea de negocio respaladada por datos.

Lo que queremos crear y fomentar mediante el desarrollo de este proyecto es el envio de medicamentos a casa es decir, el "Drug Delivery". Lo que quiero demostar es que el delivery de medicamentos sería un gran paso para las farmacias, con los cuales obtendrá muchos mayores benefios aunque tenga que realizar una pequeña inversión en repartidores y recursos necesarios para realizar los envios. 

¿Quieres que grandes multinacionales dedicadas al delivery se coman tu negocio? Si tu respuesta es no... ¡VAMOS A ANTICIPARNOS A ELLOS!

"""
)


# FRASE
st.markdown("<h1 style='text-align: center; color: black;'>¡VAMOS A ELLO! ¡NO PERDAMOS MÁS EL TIEMPO!</h1>", unsafe_allow_html=True)



# GIFT --> FALTA CENTRARLO
st.markdown("![Alt Text](https://ventolerartistica.files.wordpress.com/2018/05/kjsnckajsn.gif?w=349)", unsafe_allow_html=True)






### PONER EL INPUT PARA QUE METAN LA CALLE

calle = st.text_input('**Inserta tu direccion porfavor:** ', '')
st.write('Tu direccion es:', calle)

### PREGUNTA: ¿HAS IDO A LA CONSULTA PERSONALMENTE O LA HAS RECIBIDO DIGITALMENTE?

st.markdown('**¿Has ido al medico personalmente o has recibido la consulta digitalmente?**')


col1, col2 = st.beta_columns(2)
with col1:
    st.header("Digitalmente")
    image = Image.open('input/digital.png')
    st.image(image, use_column_width=True)

with col2:
    st.header("Personalmente")
    image = Image.open('input/personalmente.jpg')
    st.image(image, use_column_width=True)



if st.button('Personalmente'):
    st.write('He ido personalmente a mi Centro Médico')
    
    st.write("Estas son las coordenadas de tu casa: ", geo.geocode(calle))

    casa = geo.geocode(calle)
    st.write("El hospital más cercano al que podrías ir es: ", dis.distancia_entre_hospital_casa(casa))
    st.write("La farmacias mas cercana a tu casa es:", dis.distancia_entre_farmacia_casa(casa))

else:

    st.button('Digitalmente')
    st.write('He recibido la consulta médica digitalmente')

  

##### SI ES PERSONALMENTE
##### CALCULAR DISTANCIA ENTRE HOSPITAL Y CASA Y CASA Y FARMACIA


##### SI ES DIGITALMENTE
##### CALCULAR LA DISTANCIA ENTRE LA CASA Y LA FARMACIA MAS CERCANA
##### METER MAPA DE LA RUTA QUE VA HACER EL REPARTIDOR