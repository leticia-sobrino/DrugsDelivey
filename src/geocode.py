import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd
from time import sleep

# Mi key ID para que la llamada a la API de geocode se pueda hacer correctamente
key = os.getenv("key")


# Funcion para sacar coordenadas mediante la API de Geocode
def geocode(calle):
    """
    Saca las coordenadas en una lista de una dirección que le des.
    """
    sleep(2)
    data = requests.get(f"https://geocode.xyz/{calle}?json=1").json()
    try:
        
        return [float(data["latt"]),float(data["longt"])]
    except:
        return data

