# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 2025
@author: Guillermo
"""




# Paso 0: instalar librerías y fijar el directorio de trabajo


# pip install python-dotenv
# python -m pip install tinytuya


import os
import tinytuya
from dotenv import load_dotenv


os.chdir(r"C:\espaciopython\CODIGOS UTILES\PROGRAMAS-REALES\Tuya")



# Paso 1: Cargar variables de entorno desde .env

load_dotenv(r"C:\espaciopython\enviroments\tokens.env")

API_KEY = os.getenv("TUYA_API_KEY")
API_SECRET = os.getenv("TUYA_API_SECRET")
DEVICE_ID = os.getenv("TUYA_DEVICE_ID")



# Paso 2: Conectarse a la API de Tuya


c = tinytuya.Cloud(
    apiRegion="eu",
    apiKey=API_KEY,
    apiSecret=API_SECRET
)


# Paso 3: Obtener el estado del dispositivo
device_status = c.getstatus(DEVICE_ID)

if device_status.get("success"):
    arbol = device_status["result"]

    # Paso 4: Procesar y mostrar los datos relevantes
    for hojas in arbol:
        if hojas["code"] == "va_temperature":
            temperatura = hojas["value"] / 10
            print(f"La temperatura es de {temperatura} grados")
        elif hojas["code"] == "va_humidity":
            humedad = hojas["value"]
            print(f"La humedad es {humedad} %")
        elif hojas["code"] == "battery_percentage":
            bateria = hojas["value"]
            print(f"El porcentaje de batería es {bateria} %")
else:
    print(f"Error al obtener datos: {device_status.get('msg')}")



# Paso 5: Esperar antes de cerrar
input("Presiona Enter para salir...")
