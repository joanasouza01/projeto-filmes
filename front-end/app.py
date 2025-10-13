import streamlit as st
import requests

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

#rede o streamlit 
#python -m streamlit run app.py

st.set_page_config(page_title="Gerenciador de Filmes", page_icon="🎬")
st.title("🎥 Gerenciador de Filmes")

#menu lateral
menu = st.sidebar.radio("navegação", ["catalogo", "adicionar filme"])

if menu == "catalogo":
    st.subheader("todos os filmes disponiveis")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            for filme in filmes:
                st.write(f"{filme["titulo"]}")
    else:
        st.error("erro ao acessar a API")