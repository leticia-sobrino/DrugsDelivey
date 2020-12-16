import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from time import sleep
from streamlit_folium import folium_static
import folium

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

#### MAPAS GENERALES ####
# Variables necesarias para el mapa de centros medicos
max_lat = centros_medicos_clean['LATITUD'].max()
max_lon = centros_medicos_clean['LONGITUD'].max()

# Mapa de iconos personalizados por tipo de centro médico
st.header("Mapas Generales Centros Médicos")
st.subheader("Mapa Iconos Personalizados")
st.write('''
En este primer mapa le mostramos la localización de todos los Centros Sanitarios de Madrid que nos ha proporcionado el dataset.
Los Centros de Madrid se ven agrupados en 8 tipos, en el cual cada uno se ve representado por un icono personalizado.  
Si pasa el ratón por encima del mapa y de los iconos podrá observar que tipo de icono representa a cada tipo de Centro médico, además el mapa es
interactivo y le permite hacer zoom para alejarse o para acercarse.
'''
)
map_personalizado = folium.Map(location=[max_lat, max_lon],zoom_start=10, control_scale = True)

folium_static(fm.mapa_centros_medicos(map_personalizado))

# Mapa de Calor de los centros médicos
st.subheader("Mapa de calor - ControlLayer")
st.write(
    '''
    Este segundo mapa muestra también los Centros Médicos Sanitarios de todo Madrid pero de una manera visual diferente. Este mapa de calor 
    contiene un panel de control interactivo también llamado como ControlLayer en el que usted puede elegir los tipos de centros que quiere ver ubicados en 
    el mapa. Puede elegir desde ninguno hasta todos los tipos de centros, es de libre elección. A demás también posee la herramienta de zoom por si necesita jugar con ella.
    '''
)
map_capas = folium.Map(location=[max_lat, max_lon],zoom_start=10)
folium_static(fm.mapa_calor(map_capas))

# Mapa de Farmacias
st.header("Mapa General de Farmacias")
st.subheader("Mapa de Calor")
st.write('''
En este tercer mapa se muestra la localización de todas las farmacias proporcionadas en su dataset y así, podremos observar esos datos de manera visual
plasmados en un mapa. Esta información solamente se ha podido visualizar en un mapa de calor ya que utilizando un mapa con markers no nos devolvia una 
información útil debido a la cantidad de datos. Por ello, se muestran los datos de todas las farmacias de Madrid en este mapa de calor interactivo, 
con el cual puede decidir ver marcando en el panel de control las farmacias del Centro de Madrid y de la afueras. A demás se proprociona la herramienta de zoom. 

'''
)
map_municipio = folium.Map(location=[max_lat, max_lon],zoom_start=10)
folium_static(fm.map_calor_farmacias(map_municipio))






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