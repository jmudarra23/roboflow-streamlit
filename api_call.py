import streamlit as st
import requests
from datetime import datetime


def get_stats(date, labeler_code):
    # today_date = datetime.now().strftime('%Y-%m-%d')
    today_date = date
    url = "https://api.roboflow.com/socceranalytics/stats"
    params = {
        "api_key": api_key,
        "userId": labeler_code,
        "startDate": today_date,
        "endDate": today_date
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        boxes = sum(entry['boxesDrawn'] for entry in data)
        imgs = sum(entry['imagesLabeled'] for entry in data)
        st.success(f'Cajas totales: {boxes}')
        st.success(f'Número de imágenes: {imgs}')
    else:
        st.error("Falla algo... llama a Jesús " + str(response.status_code))

# Obtener las variables de entorno
api_key = st.secrets['API_KEY']

st.title("Etiquetado imágenes Wizard Football ⚽")

labelers = {
    "uy78ZKhgl9d2Dl1tV8v20Q6DbTb2": "José Enrique",
}

with st.sidebar.expander("**Etiquetador**"):
    labeler = st.selectbox(
        "**Nombre**", list(labelers.values()), index=None
    )
    if labeler:
        labeler_code = [code for code, name in labelers.items() if name == labeler][0]
    else:
        st.info("Por favor 🙏, seleccione un nombre.")

st.sidebar.markdown("---")

# Crear el selector de fechas
date = st.sidebar.date_input(
    "Selecciona una fecha",
    datetime.now()
)

if labeler:
    # Llamar a la función para obtener estadísticas al iniciar la aplicación
    get_stats(date, labeler_code)

    # Botón para actualizar estadísticas
    if st.button("Actualizar"):
        
        get_stats(date, labeler_code)
        st.empty()

else:
    st.info("Porfavor, elige tu nombre en el menú de la izquierda y la fecha de hoy.")
