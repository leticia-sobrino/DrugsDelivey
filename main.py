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
st.header("Proyecto:")
st.write(
"""
Este proyecto te va a ofrecer una nueva idea de negocio respaladada por datos.

Lo que queremos crear y fomentar mediante el desarrollo de este proyecto es el envio de medicamentos a casa es decir, el "Drug Delivery". Lo que quiero demostar es que el delivery de medicamentos sería un gran paso para las farmacias, con los cuales obtendrá muchos mayores benefios aunque tenga que realizar una pequeña inversión en repartidores y recursos necesarios para realizar los envios. 

¿Quieres que grandes multinacionales dedicadas al delivery se coman tu negocio? Si tu respuesta es no... ¡VAMOS A ANTICIPARNOS A ELLOS!

"""
)


st.header("Datos:")

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



# FRASE
st.header("**¡VAMOS A ELLO! ¡NO PERDAMOS MÁS EL TIEMPO!**")


# GIFT --> FALTA CENTRARLO
st.markdown("![loading...](https://ventolerartistica.files.wordpress.com/2018/05/kjsnckajsn.gif?w=349)", unsafe_allow_html=True)




### PONER EL INPUT PARA QUE METAN LA CALLE

st.header("**Datos obligatorios**")
st.markdown("_**IMPORTANTE:** No se preocupe por sus datos, por motivos de seguridad y protección de datos no se guardarán en la nube_")

st.subheader("Rellene los campos vacios:")
st.write('Porfavor siga la misma estructura del ejemplo para evitar errores y que la búsqueda sea más precisa. Ejemplo:')
st.code('Calle Marbella 83 28034 Madrid')

calle = st.text_input('Inserta tu direccion porfavor: ', '')

if not calle:
    st.warning('Introduzca su dirección completa para poder continuar')
    st.stop()
st.success('¡Muchas gracias!')

st.write('Su direccion es:', calle)





### PREGUNTA: ¿HAS IDO A LA CONSULTA PERSONALMENTE O LA HAS RECIBIDO DIGITALMENTE?

st.subheader('**¿Va a ir a su Centro médico personalmente o va a recibir un consulta digital?**')

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
    ('Seleccione una de las siguientes opciones','Personalmente', 'Digitalmente'))

if option == 'Seleccione una de las siguientes opciones':
    st.stop()
st.success("¡Muchas gracias!")

st.write('Ha seleccionado:', option)



if option == 'Personalmente':
    st.write('En su caso, va a ir personalmente a su Centro Médico')
    
    # st.write("Estas son las coordenadas de tu casa: ", geo.geocode(calle))

    casa = geo.geocode(calle)
    # st.markdown(casa)
    st.write("El hospital más cercano al que podrías ir es: ", dis.distancia_entre_hospital_casa(casa))
    st.write("La farmacias mas cercana a tu casa es:", dis.distancia_entre_farmacia_casa(casa))

    
    st.write("Aquí podrás observar visualmente el hospital más cercano y la farmacias mas cercana que en un futuro te podrás ahorrar ir")
    
    # MAPA VISUAL
    # variables
    # casa = geo.geocode(calle)
    # path = "icons/{}".format
    # icon_hosp = path("Hospital-clinica-sanatorio-icon.png")
    coord_farm_cercana = dis.coordenadas_farmacia_mas_cercana(casa)
    coord_hospital_cercano = dis.coordenadas_hospital_mas_cercano(casa)
    # map_final = folium.Map(location = casa, zoom_start=15, control_scale = True)

    #funcion
    folium_static(fm.distancia_visual_3(casa))




elif option == 'Digitalmente':
    st.write('En su caso, va a tener la consulta médica digitalmente')

    # st.write("Estas son las coordenadas de tu casa: ", geo.geocode(calle))

    casa = geo.geocode(calle)
    
    st.write("Distancia que vas a ahorrarte porque en vez de hacerla tú va a ir un repartidor propio de esta farmacia a llevartela a casa:", dis.distancia_entre_farmacia_casa(casa))

    st.write("Aquí podrás observar visualmente la farmacia mas cercana a tu casa que en un futuro te podrás ahorrar ir ")
    
    # MAPA VISUAL
    # variables
    # casa = geo.geocode(calle)
    coord_farm_cercana = dis.coordenadas_farmacia_mas_cercana(casa)
    #map_final_2 = folium.Map(location = casa, zoom_start=15, control_scale = True)
    
    #function
    folium_static(fm.distancia_visual(casa))


st.header("**Juego interactivo**")
st.write(
    '''
    Aquí os dejo un mapa interactivo con los markers de todos los centros medicos de Madrid para que calculeir vosotros mismos la distacia entre
    los dos puntos que querais.
    Solamente teneis que hacer click en el cuadrito que aparece en el lado derecho del mapa y luego pinchar en "create a new measurament". Ahora,
    desliza el raton por encima del mapa y verás un punto rojo en el cursor, haciendo click en cualquier parte del mapa elegirás los dos puntos de 
    los cuales quieras saber la distancia entre ellos. 
    Te aparecerá un recuadro blanco con las coordenales geofráficas de los dos sitios que has marcado y la distancia que hay entre ellos dos medias en km.
    Si quieres guardar la medida solamente tienes que darle a "finish measurement" y si la quieres borrar tendrás que pinchas en "cancel".
    ¡Pasalo bien!
    '''
)

map_juego = fm.mapa_centros_medicos(map_personalizado)
folium_static(fm.include_meas_control(map_juego))


st.markdown("<h1 style='text-align: center; color: black;'>¿Te imaginas no tener ni que recorrer la mínima distancia para comprar un medicamento?</h1>", unsafe_allow_html=True)

image = Image.open('input/reloj.png')
st.image (image,use_column_width=False)

st.markdown("<h1 style='text-align: center; color: black;'>¡No escapemos esta oportunidad de negocio!</h1>", unsafe_allow_html=True)