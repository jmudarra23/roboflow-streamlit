import streamlit as st

workspaces = {
    "Workspace 1": {
        "subdomain": "socceranalytics",
        "api_key": st.secrets['API_KEY'],
        "labelers": {
            "uy78ZKhgl9d2Dl1tV8v20Q6DbTb2": "José Enrique",
            "hLuoV809g9hspaa0gpQxoqEu8Ix1": "Jesús Mudarra",
            "FxdpyaaXtQbLc3V14u8Dvc2zJ8B3": "Daniel Rendon",
        }
    },
    "Workspace 2": {
        "subdomain": "socceranalytics-p4xjo",
        "api_key": st.secrets['API_KEY2'],
        "labelers": {
            "lSjzzgbjkmNbcNh4xpae27ywdd92": "Elite Sports17",
        }
    }
}