import streamlit as st
from config import workspaces, MIN_BOXES, MIN_IMAGES
import requests
from datetime import datetime, timedelta


st.title("Etiquetado imágenes Wizard Football ⚽")


def get_first_date_week(date):
    dayweek = date.weekday()
    first_date = date - timedelta(days=dayweek)
    return first_date


def get_stats(date, labeler_code, api_key, subdomain):
    def fetch_data(start_date, end_date):
        response = requests.get(f"https://api.roboflow.com/{subdomain}/stats", params={
            "api_key": api_key,
            "userId": labeler_code,
            "startDate": start_date,
            "endDate": end_date
        })
        if response.status_code == 200:
            data = response.json()["data"]
            return sum(entry["boxesDrawn"] for entry in data), sum(entry["imagesLabeled"] for entry in data)
        else:
            st.error("Algo falla... llama a Jesús")
            return 0, 0

    first_date_week = get_first_date_week(date)

    col1, col2 = st.columns(2)

    boxes_today, imgs_today = fetch_data(date, date)
    boxes_week, imgs_week = fetch_data(first_date_week, date)

    with col1:
        st.subheader("Etiquetas")
        st.metric(label="Hoy", value=boxes_today)
        st.metric(label="Total semanal", value=boxes_week)
        if boxes_week <= MIN_BOXES:
            st.progress(boxes_week/MIN_BOXES) # Progreso semanal
            st.write(f"Progreso semanal: {round((boxes_week/MIN_BOXES)*100, 2)}%")
        else:
            st.progress(100)
            st.write("Progreso semanal: 100.0%")
    with col2:
        st.subheader("Imágenes")
        st.metric(label="Hoy", value=imgs_today)
        st.metric(label="Total semanal", value=imgs_week)
        if imgs_week <= MIN_IMAGES:
            st.progress(imgs_week/MIN_IMAGES)
            st.write(f"Progreso semanal: {round((imgs_week/MIN_IMAGES)*100, 2)}%")
        else:
            st.progress(100)
            st.write("Progreso semanal: 100.0%")

    if boxes_week < MIN_BOXES:
        st.warning(f"Te quedan {MIN_BOXES - boxes_week} etiquetas para llegar al objetivo semanal!")
    else:
        st.success(f"Felicidades! Llegaste al objetivo de etiquetas! 🚀")
        st.balloons()
    if imgs_week < MIN_IMAGES:
        st.warning(f"Te quedan {MIN_IMAGES - imgs_week} imágenes para llegar al objetivo semanal!")
    else:
        st.success(f"Felicidades! Llegaste al objetivo de imágenes! 🚀")
        st.balloons()

# Seleccionar el espacio de trabajo
workspace = st.sidebar.selectbox("**Selecciona el espacio de trabajo**", list(workspaces.keys()))

# Obtener los diccionarios correspondientes al espacio de trabajo seleccionado
api_key = workspaces[workspace]["api_key"]
labelers = workspaces[workspace]["labelers"]
subdomain = workspaces[workspace]["subdomain"]

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
