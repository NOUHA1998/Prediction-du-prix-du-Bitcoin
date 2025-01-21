import streamlit as st
import pandas as pd
import joblib

# Charger le modèle
try:
    model = joblib.load('bitcoin_price_model.pkl')
except FileNotFoundError:
    st.error("Le modèle 'bitcoin_price_model.pkl' est introuvable. Assurez-vous qu'il est dans le même dossier que 'app.py'.")

# Interface utilisateur
st.title('Prédiction du prix du Bitcoin')

# Saisie des caractéristiques
st.sidebar.header('Saisie des caractéristiques')
seven_day_avg = st.sidebar.number_input('Moyenne mobile sur 7 jours')
thirty_day_avg = st.sidebar.number_input('Moyenne mobile sur 30 jours')

# Prédiction
if st.sidebar.button('Prédire'):
    if 'model' in locals():
        input_data = pd.DataFrame({'7_day_avg': [seven_day_avg], '30_day_avg': [thirty_day_avg]})
        try:
            prediction = model.predict(input_data)
            st.write(f'Prédiction du prix du Bitcoin : {prediction[0]}')
        except Exception as e:
            st.error(f"Erreur lors de la prédiction : {e}")
