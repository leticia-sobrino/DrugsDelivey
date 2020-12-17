# Drugs Delivery :bike:

### ÍNDICE
#### 1. INTRUDUCCIÓN :ghost:
#### 2. PROYECTO :rocket:
#### 3. ESTURCTURA :skull:
#### 4. FUNCIONAMIENTO :boom:
#### 5. DOCUMENTACIÓN :white_check_mark:

![fotodeportada](https://github.com/leticia-sobrino/ProyectoFinal/blob/main/input/deliverybike.png)


### 1. INTRUCCIÓN :ghost:
Este proyecto es el proyecto final del Data Analys Bootcamp de Ironhack. 
En él, aplico todos mis conocimientos aprendidos durante los dos meses y medio del bootcamp. Demuestro mis destrezas y habilidades a la hora de manejar grandes cantidades de datos con el fin de saber devolver un producto con valor.

### 2. PROYECTO:rocket:
Como tema abierto que podíamos decidir, yo personalmente elegí una nueva idea de negocio que se me ocorrió. En este proyecto defiendo esta idea y demuestro lo rentable que podría ser respaldada por datos. 
El fin de este proyecto es poder vender la idea al sector sanitario con la intención de podernos anticipar a que las grandes empresas como Amazon entren en nuestra parte de mercado.
El fin por ello, es devolver mediantes un análisis de datos una serie de resultados y visualizaciones para entender que si no actuamos a tiempo, grandes empresas de delivery entrarán en el sector sanitario. 


### 3. ESTRUCTURA :skull:
El proyecto presenta la siguiente estructura: 
1. Una carpeta de data que se encuentra oculta debido a su peso pero, en donde se encuentran las dos bases de datos utilizadas para este proyecto y cuya documentación se encontrará en el punto cinco del README.md.
2. La carpeta de notebooks: 
   - En donde podrás encontrar los notebooks con los que he podido ir trabajando a la hora de hacer el ETLS de las bases de datos proporcionadas por la Comunidad de Madrid, utilizando la herramientas de Pandas y Numpy. 
   - Los notebooks respectivos para la visualización de datos en mapas mediante la utlización de la libreria Folium.
   - Otro notebook para realizar el cáldulo de distancias de manera matemática entre los diferentes lugares (tu propia dirección de casa, y todas las farmacias y centros médicos de Madrid). Para este cálculo hemos utilizado la función haversine y sus librerias necesarias.
   - Y, por último un notebook en el que nos encontraremos las requests necesarias a la API de Geocode que hemos tenido que utilizar para inyectar más datos a nuestro proyecto y completarlo más.
3. Una carpeta de output en donde encontraras los mapas finales
4. La carpeta de input en dónde se guardan las imagenes utilizadas para diseñar la API que he creado para devolver el produco final de este proyecto.
5. Una carpeta de icons en dónde encontrarás iconos en el formato png para insertar a mis mapas como markers y personalizar mi producto final.
6. Y, por último y lo más importante, la base de todo este proyecto y el cerebro del producto final: la carpeta de src con todas las funciones para aplicar todas las herramientas de análisis, filtrado y devolución de datos con valor y, el archivo main.py que se encarga de dar vida al proyecto y devolver toda la información  con tan solo ejecutar el siguiente comando en su local:

        streamlit run main.py


### FUNCIONAMINETO :boom:
Cómo he dicho anteriormente el main.py es el archivo que hace que cobre vida este proyecto.
Este proyecto devuelve una API, contruida por la herramienta Streamlit, cuyo uso solamente esta limitado desde local. 
Si quiere ver su funcionamineto solamente debería de seguir los siguientes pasos:
1. Clonar este repositorio en su local
2. Accecer a la dirección de este repositorio en su terminal (donde lo haya clonado)
3. Y escribir el siguinete comando para que la API empiece a correr:
   
        streamlit run main.py

4. Ahora se le habrá abierto una pestaña en su navegador con la API de este proyecto, lea lo que pone, juegue con los mapas interactivos que se le proporcionan y siga los pasos para ver la mínima distancia que usted en un futuro NO va a tener que realizar porque lo va a hacer un repartidor por tí, lo que llamamos Delivery.


### DOCUMENTACIÓN :white_check_mark:
1. Datasets: 
   - Base de datos de Centros Médicos en Madrid: https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=da7437ac37efb410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default
  
   - pdf de la documentación del dataset de los centros médicos en Madrid: https://datos.madrid.es/FWProjects/egob/Catalogo/XComun/Ficheros/Estructura_DS_ConjuntoDatos.pdf
  
   - Base de datos de farmacias en Madrid : https://datos.comunidad.madrid/catalogo/dataset/oficinas_farmacia
  
2. API Geocode
   - Documentacion de Geocode: https://geocode.xyz/
  
3. Documentación de herramientas utilizadas
   - Pandas: https://pandas.pydata.org/docs/
   - Numpy: https://numpy.org/doc/
   - Folium: https://docs.streamlit.io/en/stable/
   - Streamlit: https://docs.streamlit.io/en/stable/getting_started.html
   



