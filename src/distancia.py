import pandas as pd
import math
import numpy as np


import src.geocode as geo

# IMPORTANDO NUESTROS DATOS LIMPIOS
centros_medicos_clean = pd.read_csv("data/centros_medicos_clean.csv")
farmacias_clean = pd.read_csv("data/farmacias_clean.csv")




# FUNCION BASE DE ESTE ARCHIVO
def haversine(coord1, coord2):
    
    '''
    Funcion en donde al meterle dos parametros de coordenadas te va a devolver la distancia que hay entre ambos puntos
    '''
    
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))


# FUNCION QUE DEVUELVE EL CENTRO MEDICO MÁS CERCANO A TU CASA


def distancia_entre_hospital_casa(casa):
    '''
    Esta funcion lo que coge es la latitud y longitud de la ubicacion de tu casa y te evuelve el nombre del centro medico 
    mas cercano a tu casa
    '''
    
    for index, row in centros_medicos_clean.iterrows(): 
        row['LATITUD']
        row['LONGITUD']
    
    centros_medicos_clean['DISTANCIA'] = 0 
    
    centros_medicos_clean['DISTANCIA'] = centros_medicos_clean.apply(lambda row: haversine(casa, (row['LATITUD'], row['LONGITUD'])), axis=1)
    
    return (centros_medicos_clean.loc[centros_medicos_clean.DISTANCIA.argmin(), "NOMBRE"], math.trunc(centros_medicos_clean.loc[centros_medicos_clean.DISTANCIA.argmin(), "DISTANCIA"]))
    



# FUNCION QUE DEVUELVE LA FARMACIA MAS CERCANA A TU CASA. LA DISTANCIA QUE VA A RECORRER EL REPARTIDOS POR TI
def distancia_entre_farmacia_casa(casa):
    for index, row in farmacias_clean.iterrows(): 
        row['latitud']
        row['longitud']
    
    farmacias_clean['DISTANCIA'] = 0 
    
    farmacias_clean['DISTANCIA'] = farmacias_clean.apply(lambda row: haversine(casa, (row['latitud'], row['longitud'])), axis=1)
    
    return (farmacias_clean.loc[farmacias_clean.DISTANCIA.argmin(), "titular_nombre"], farmacias_clean.loc[farmacias_clean.DISTANCIA.argmin(), "DISTANCIA"])
