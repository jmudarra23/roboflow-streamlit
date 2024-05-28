import streamlit as st

workspaces = {
    "socceranalytics": {
        "subdomain": "socceranalytics-5vbz1",
        "api_key": st.secrets['API_KEY'],
        "labelers": {
            "lSjzzgbjkmNbcNh4xpae27ywdd92": "Elite Sports17",
            "uy78ZKhgl9d2Dl1tV8v20Q6DbTb2": "José Enrique",
        }
    },
    "socceranalytics2": {
        "subdomain": "socceranalytics2",
        "api_key": st.secrets['API_KEY2'],
        "labelers": {
            "n7XjGcQyOURfX4CSmFX3Q617QBZ2": "Alessa Marce",
            "lSjzzgbjkmNbcNh4xpae27ywdd92": "Elite Sports17",
        }
    }
}