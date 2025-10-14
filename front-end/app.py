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
            st.dataframe(filmes)
    else:
        st.error("erro ao acessar a API")

elif menu == "adicionar filme":
    st.subheader("➕ adicionar filmes")
    titulo = st.text_input("titulo do filme")
    genero = st.text_input("genero")
    ano = st.number_input("ano de lançamento", min_value=1880, max_value=2100, step=1)
    avaliacao = st.number_input("avaliacao de (0 a 10)", min_value=0.0, max_value=10.0, step=0.1)
    if st.button("salvar filme"):
        dados = {"titulo": titulo, "genero": genero, "ano": ano, "avaliacao": avaliacao}
        response = requests.post(f"{API_URL}/filmes", params=dados)
        if response.status_code == 200:
            st.success("filme adicinado com sucesso!")
        else:
            st.error("erro ao adicionar o filme")