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
path = "icons/{}".format

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

# MAPA DE CALOR CENTROS MEDICOS
### variables necesarias plara aplicar luego la funcion
def dataframescapas(elemento):
    return centros_medicos_clean[centros_medicos_clean['TIPO'].str.contains(f"{elemento}")]

capas = list(centros_medicos_clean['TIPO'].unique())

data0 = dataframescapas(capas[0])
data1 = dataframescapas(capas[1])
data2 = dataframescapas(capas[2])
data3 = dataframescapas(capas[3])
data4 = dataframescapas(capas[4])
data5 = dataframescapas(capas[5])
data6 = dataframescapas(capas[6])
data7 = dataframescapas(capas[7])

def mapa_calor(mapa):
    map_capas = Map(location=[max_lat, max_lon],zoom_start=10)
    
    data0_group = folium.FeatureGroup(name = "Drogodependientes")
    HeatMap(data = data0[["LATITUD","LONGITUD"]], radius = 10).add_to(data0_group)
    data0_group.add_to(map_capas)


    data1_group = folium.FeatureGroup(name = "Otros Centos Medicos")
    HeatMap(data = data1[["LATITUD","LONGITUD"]], radius = 10).add_to(data1_group)
    data1_group.add_to(map_capas)


    data2_group = folium.FeatureGroup(name = "Especialidades Medicas")
    HeatMap(data = data2[["LATITUD","LONGITUD"]], radius = 10).add_to(data2_group)
    data2_group.add_to(map_capas)

    data3_group = folium.FeatureGroup(name = "Centros Salud")
    HeatMap(data = data3[["LATITUD","LONGITUD"]], radius = 10).add_to(data3_group)
    data3_group.add_to(map_capas)


    data4_group = folium.FeatureGroup(name = "Centros Rehabilitacion Psicosocial")
    HeatMap(data = data4[["LATITUD","LONGITUD"]], radius = 10).add_to(data4_group)
    data4_group.add_to(map_capas)


    data5_group = folium.FeatureGroup(name = "Centros Prevencion de Enfermedades")
    HeatMap(data = data5[["LATITUD","LONGITUD"]], radius = 10).add_to(data5_group)
    data5_group.add_to(map_capas)


    data6_group = folium.FeatureGroup(name = "Centros Salud Mental")
    HeatMap(data = data6[["LATITUD","LONGITUD"]], radius = 10).add_to(data6_group)
    data6_group.add_to(map_capas)


    data7_group = folium.FeatureGroup(name = "Hospitales Clinicas Sanatorios")
    HeatMap(data = data7[["LATITUD","LONGITUD"]], radius = 10).add_to(data7_group)
    data7_group.add_to(map_capas)

    # Esta ultima linea SOLO se pone alfinal de haber definido tus capas, para que te aparezca el Later control con todas tus opciones

    folium.LayerControl(collapsed = False).add_to(map_capas) 

    return map_capas