import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium import plugins
from folium.plugins import HeatMap, MarkerCluster
from folium import IFrame
import ipywidgets
from folium.features import CustomIcon

import numpy as np
import pandas as pd

# IMPORTANDO NUESTROS DATOS LIMPIOS
centros_medicos_clean = pd.read_csv("data/centros_medicos_clean.csv")
farmacias_clean = pd.read_csv("data/farmacias_clean.csv")

# VARIABLES PARA LA LOCALIZACION DEL MAPA
max_lat = centros_medicos_clean['LATITUD'].max()
max_lon = centros_medicos_clean['LONGITUD'].max()

# VARIABLES PARA LOS MARKERS PERSONALIZADOS
path = "../icons/{}".format

icon_drogo = path("centro-de-asistencia-drogodependientes-icon.png")
icon_otros = path("otros-centros-sanitarios.png")
icon_esp = path("especialidades.png")
icon_salud = path("centro-de-salud-icon.png")
icon_rehab = path("centro-rehabilitacion-psicosocial-icon.png")
icon_prev = path("icon-centro-de-prevencion-de-enfermedades.png")
icon_mental = path("icon-salud-mental.png")
icon_hosp = path("Hospital-clinica-sanatorio-icon.png")


# MAPA GENERAL CENTROS MÉDICOS PERSONALIZADO
def mapa_centros_medicos(mapa):
    
    map_personalizado = folium.Map(location=[max_lat, max_lon],zoom_start=10, control_scale = True)
    
    for i,row in centros_medicos_clean.iterrows():
    
        tipos = {"location" : [row["LATITUD"], row["LONGITUD"]],
                "tooltip" : row["TIPO"]}
    
        if row["TIPO"] == "CentrosAsistenciaDrogodependientes":
            icon = CustomIcon(
                icon_drogo,
                icon_size=(38, 50))

        elif row["TIPO"] == "OtrosCentrosMedicos":
            icon = CustomIcon(
                icon_otros,
                icon_size=(38, 50))
     
        elif row["TIPO"] == "CentrosEspecialidadesMedicas":
            icon = CustomIcon(
                icon_esp,
                icon_size=(38, 50))
    
        elif row["TIPO"] == "CentrosSalud":
            icon = CustomIcon(
                icon_salud,
                icon_size=(38, 50))
    
        elif row["TIPO"] == "CentrosRehabilitacionPsicosocial":
            icon = CustomIcon(
                icon_rehab,
                icon_size=(38, 50))

        elif row["TIPO"] == "CentrosPrevencionEnfermedades":
            icon = CustomIcon(
                icon_prev,
                icon_size=(38, 50))
        
        elif row["TIPO"] == "CentrosSaludMental":
            icon = CustomIcon(
                icon_mental,
                icon_size=(38, 50))
    
        # HospitalesClinicasSanatorios
        else:
            icon = CustomIcon(
                icon_hosp,
                icon_size=(38, 50))
            
            
    
        marker = Marker(**tipos,icon = icon).add_to(map_personalizado)


    return map_personalizado
