import pandas as pd
import streamlit as st
import pickle
from PIL import Image

def recommend(movie):
    movie_index = movies[movies['movie_title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].movie_title)
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("IMDB Movie Recommendation")

selected_movie_name = st.selectbox(
    'Chose the movie you LIKE!',
    movies['movie_title'].values)

if st.button('RECOMMEND'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.image(movies[movies['movie_title'] == i].movie_poster.values[0],width= 75)
        st.write(i)

