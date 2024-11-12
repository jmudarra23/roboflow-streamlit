import streamlit as st

workspaces = {
    "socceranalytics": {
        "subdomain": "socceranalytics-5vbz1",
        "api_key": st.secrets['API_KEY'],
        "labelers": {
            "lSjzzgbjkmNbcNh4xpae27ywdd92": "Elite Sports17",
            "EhV0M7z3ZRfzW6CLd7Ho2fKFmwe2": "Niel John Butad",
            "3pM0YPyULBYBdnJP0eBLUu8HaJv1": "Developers IPSUM PH",
            "l3bW925TA7hgB3e9XNcjTzJoPGB3": "Etiquetador SR",
            "uy78ZKhgl9d2Dl1tV8v20Q6DbTb2": "Jose Enrique Ferrero",
        }
    },
    "socceranalytics2": {
        "subdomain": "socceranalytics2",
        "api_key": st.secrets['API_KEY2'],
        "labelers": {
            "lSjzzgbjkmNbcNh4xpae27ywdd92": "Elite Sports17",
            "n7XjGcQyOURfX4CSmFX3Q617QBZ2": "Alessa Marce",
            "jSkhmVdFEzZCZDjbByrSpO7Ua3M2": "Victoria Bajo",
        }
    }
}

MIN_BOXES = 6500
MIN_IMAGES = 450
