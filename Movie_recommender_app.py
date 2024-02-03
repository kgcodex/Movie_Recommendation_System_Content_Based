#importing Modules
import streamlit as st 
import pandas as pd 
import pickle
import requests 

# Title
st.title("Movie Recommender System")

# Loading DataFrame
movies_dict=pickle.load(open("movies_dict.pkl","rb"))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open("similarity.pkl","rb"))
similarity=pd.DataFrame(similarity)

# Search Box
selected_movie=st.selectbox(
"Select your Movie",
movies["title"].values)

# Recommended Movies and Poster
def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=5bf70dfae55dcee0874e25b0ac0043fe".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data["poster_path"]

def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    movie_list=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x: x[1])[1:6]
    names=[]
    poster=[]
    for i in movie_list:
        names.append(movies.iloc[i[0]].title)
        poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    
    return names,poster

# Recommend Button
if st.button("Recommend"):
    names,poster=recommend(selected_movie)

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(poster[0])
        st.write(names[0])
    with col2:
        st.image(poster[1])
        st.write(names[1])
    with col3:
        st.image(poster[2])
        st.write(names[2])
    with col4:
        st.image(poster[3])
        st.write(names[3])
    with col5:
        st.image(poster[4])
        st.write(names[4])
        