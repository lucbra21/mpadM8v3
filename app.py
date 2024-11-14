import streamlit as st

# Título de la aplicación
st.title("Hola desde EC2 de AWS")

# Botón para mostrar el mensaje
if st.button("Mostrar mensaje"):
    st.write("Hola mundo")
