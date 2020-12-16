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


#### EMPEZANDO A CREAR LA API ####

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
st.header("¡VAMOS A ELLO! ¡NO PERDAMOS MÁS EL TIEMPO!")



# GIFT --> FALTA CENTRARLO

#st.markdown("![Alt Text](https://ventolerartistica.files.wordpress.com/2018/05/kjsnckajsn.gif?w=349)", unsafe_allow_html=True)

#st.markdown(“<h1 style=‘text-align: center; color: red;’>Some title</h1>“, unsafe_allow_html=True)

data_url = "https://ventolerartistica.files.wordpress.com/2018/05/kjsnckajsn.gif?w=349"
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)


# EXPLICACION DE LOS DATOS USADOS DE MANERA VISUAL CON MAPAS
st.write(
'''
Antes de todo le quiero especificar que los datos usados para el desarrollo de este proyecto han sido:

1. Un dataset de Sedes de Centros médicos en Madrid, recogido del Portal de Datos Abiertos del Ayuntamiento de Madrid

2. Un dataset de Farmacias, recogido de la página de la Comunidad de Madrid

Ambos links se proporcionan en el README.md del proyecto en el apartado de Documentación.
Y a continuación, le presentaré estos conjuntos de datos de una manera visual volcados en diferentes mapas.
'''
)

# MAPAS GENERALES





### PONER EL INPUT PARA QUE METAN LA CALLE

st.subheader("**Datos obligatorios**")
st.write("No se preocupe, por motivos de seguridad y protección de datos sus datos no se guardarán en la nube")

calle = st.text_input('Inserta tu direccion porfavor: ', '')

if not calle:
    st.warning('Introduzca su dirección para pode continuar')
    st.stop()
st.success('¡Muchas gracias!')

st.write('Tu direccion es:', calle)




### PREGUNTA: ¿HAS IDO A LA CONSULTA PERSONALMENTE O LA HAS RECIBIDO DIGITALMENTE?

st.subheader('**¿Has ido al medico personalmente o has recibido la consulta digitalmente?**')

# Imagenes
col1, col2 = st.beta_columns(2)
with col1:
    #st.header("Digitalmente")
    image = Image.open('input/digital.png')
    st.image(image, use_column_width=True)

with col2:
    #st.header("Personalmente")
    image = Image.open('input/personalmente.jpg')
    st.image(image, use_column_width=True)

#################################################################################################################################
# BOX SELECTION
option = st.selectbox(
    'Porfavor introduzca su caso:',
    ('Seleccione','Personalmente', 'Digitalmente'))

if option == 'Seleccione':
    st.stop()
st.success("¡Muchas gracias!")

st.write('Ha seleccionado:', option)



if option == 'Personalmente':
    st.write('He ido personalmente a mi Centro Médico')
    
    st.write("Estas son las coordenadas de tu casa: ", geo.geocode(calle))

    casa = geo.geocode(calle)
    st.write("El hospital más cercano al que podrías ir es: ", dis.distancia_entre_hospital_casa(casa))
    st.write("La farmacias mas cercana a tu casa es:", dis.distancia_entre_farmacia_casa(casa))

elif option == 'Digitalmente':
    st.write('He tenido mi consulta médica digitalmente')

    st.write("Estas son las coordenadas de tu casa: ", geo.geocode(calle))

    casa = geo.geocode(calle)
    st.write("Distancia que vas a ahorrarte porque en vez de hacerla tú va a ir un repartidor propio esta farmcaia a llevartela a casa:", dis.distancia_entre_farmacia_casa(casa))


  

##### SI ES PERSONALMENTE
##### CALCULAR DISTANCIA ENTRE HOSPITAL Y CASA Y CASA Y FARMACIA


##### SI ES DIGITALMENTE
##### CALCULAR LA DISTANCIA ENTRE LA CASA Y LA FARMACIA MAS CERCANA
##### METER MAPA DE LA RUTA QUE VA HACER EL REPARTIDOR