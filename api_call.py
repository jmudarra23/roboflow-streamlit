import streamlit as st
import requests
from datetime import datetime

def get_stats():
    today_date = datetime.now().strftime('%Y-%m-%d')
    url = "https://api.roboflow.com/socceranalytics/stats"
    params = {
        "api_key": "OzBJXsvBWzwsfwDQjSPF",
        "userId": "uy78ZKhgl9d2Dl1tV8v20Q6DbTb2",
        "startDate": today_date,
        "endDate": today_date
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        boxes = sum(entry['boxesDrawn'] for entry in data)
        imgs = sum(entry['imagesLabeled'] for entry in data)
        st.success(f'Cajas totales: {boxes}\nNúmero de imágenes: {imgs}')
    else:
        st.error("Falla algo... llama a Héctor " + str(response.status_code))

st.title("Estadísticas de Imágenes")

# Botón para actualizar estadísticas
if st.button("Actualizar"):
    get_stats()

# Llamar a la función para obtener estadísticas al iniciar la aplicación
get_stats()
