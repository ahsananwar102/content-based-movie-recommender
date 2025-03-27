import streamlit as st
import pickle
import pandas as pd
import os
import requests

# Function to fetch movie poster from TMDB API
def get_poster(movie_title):
    """Fetch movie poster using TMDb API."""
    API_KEY = st.secrets["TMDB_API_KEY"]  # Store API key securely
    search_url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&api_key={API_KEY}"
    
    response = requests.get(search_url)
    data = response.json()

    if data["results"]:
        poster_path = data["results"][0]["poster_path"]
        full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
        return full_path
    return None  # No poster found


# Function to recommend movies
def recommend(movie):
    """Return top 5 recommended movies based on similarity."""
    l = []
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movies_list:
        l.append(movies_df.iloc[i[0]]['title'])

    return l


# ✅ Load Pickle Files
if os.path.exists("movies_df.pkl") and os.path.exists("similarity.pkl"):
    with open("movies_df.pkl", "rb") as file:
        movies_df = pickle.load(file)

    with open("similarity.pkl", "rb") as file:
        similarity = pickle.load(file)
else:
    st.error("Pickle files not found! Please upload `movies_df.pkl` and `similarity.pkl`.")
    st.stop()

# ✅ Streamlit UI
st.title("🎬 Movie Recommender System")

option = st.selectbox("Choose a movie:", movies_df["title"])

if st.button("Recommend"):
    recs = recommend(option)

    st.subheader("Recommended Movies")
    cols = st.columns(5)  # Display 5 movies in a row

    for i, movie in enumerate(recs):
        with cols[i]:  # Place each movie in a separate column
            poster_url = get_poster(movie)
            if poster_url:
                st.image(poster_url, width=120)
            else:
                st.write("No poster found.")
            st.text(movie)

