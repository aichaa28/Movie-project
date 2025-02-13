import streamlit as st
import joblib
import numpy as np
import pickle

# 🟢 ✅ set_page_config doit être le premier appel Streamlit
st.set_page_config(page_title="Prédiction de la Note d'un Film", layout="centered")

# Chemin du modèle
MODEL_PATH = "C:\\Users\\Aycha\\Desktop\\M2_BDIA\\NLP\\Projet_movie\\final\\model\\best_model_0.09.pkl"

# 🔹 Chargement sécurisé du modèle
@st.cache_resource
def load_model():
    try:
        return joblib.load(MODEL_PATH)  # Suppression de mmap_mode=None
    except Exception as e:
        st.error(f"Erreur lors du chargement du modèle : {e}")
        return None

model = load_model()

# Interface utilisateur
st.title("🎬 Prédiction de la Note d'un Film")
st.write("Remplissez les détails du film pour obtenir une prédiction.")

# Formulaire utilisateur
with st.form("film_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        duration = st.number_input("Durée du film (en minutes)", min_value=1, step=1)
        genres = st.text_input("Genres (ex: Action, Thriller)")
        cast = st.text_input("Casting (ex: Julia Stiles, Patrick Muldoon)")
    
    with col2:
        producers = st.text_input("Producteurs (ex: Frank Beddor, Greg Steinberg)")
        synopsis = st.text_area("Synopsis")
        reviews = st.text_area("Critiques")
    
    submit_button = st.form_submit_button("🔍 Prédire la Note")

# Prédiction
if submit_button:
    if not synopsis or not reviews or not genres or not cast or not producers:
        st.warning("⚠️ Veuillez remplir tous les champs.")
    else:
        with st.spinner("Analyse des données en cours..."):
            if model is None:
                st.error("Le modèle n'a pas pu être chargé.")
            else:
                # 🔹 Remplacer cette ligne par une vraie transformation des textes
                input_features = np.random.rand(1, 3000)  
                
                try:
                    predicted_rating = model.predict(input_features)[0]
                    st.success(f"✅ Note prédite : {round(predicted_rating, 2)}/5.")
                    
                    # Affichage sous forme de barre de progression
                    st.progress(min(max(int(predicted_rating * 20), 0), 100))
                except Exception as e:
                    st.error(f"Erreur lors de la prédiction : {e}")

# Footer
st.markdown("---")
st.caption("📌 Modèle basé sur l'entraînement précédent.")
