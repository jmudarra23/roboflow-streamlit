import streamlit as st
from config import workspaces
import requests
from datetime import datetime


st.title("Etiquetado imágenes Wizard Football ⚽")

def get_stats(date, labeler_code, api_key, subdomain):
    today_date = date
    url = f"https://api.roboflow.com/{subdomain}/stats"
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
        st.error("Algo falla... llama a Jesús")

# Seleccionar el espacio de trabajo
workspace = st.sidebar.selectbox("**Selecciona el espacio de trabajo**", list(workspaces.keys()))

# Obtener los diccionarios correspondientes al espacio de trabajo seleccionado
api_key = workspaces[workspace]['api_key']
labelers = workspaces[workspace]['labelers']
subdomain = workspaces[workspace]['subdomain']

st.sidebar.markdown("---")

labeler = st.sidebar.selectbox(
    "**Nombre**", list(labelers.values()), index=None
)
if labeler:
    labeler_code = [code for code, name in labelers.items() if name == labeler][0]


st.sidebar.markdown("---")

# Crear el selector de fechas
date = st.sidebar.date_input(
    "**Selecciona una fecha**",
    datetime.now()
)

if labeler:

    # Llamar a la función para obtener estadísticas al iniciar la aplicación
    get_stats(date, labeler_code, api_key, subdomain)

    # Botón para actualizar estadísticas
    if st.button("Actualizar"):
        
        get_stats(date, labeler_code, api_key, subdomain)
        st.empty()

else:
    st.info("Por favor 🙏, selecciona el Workspace al que perteneces y tu nombre.")
