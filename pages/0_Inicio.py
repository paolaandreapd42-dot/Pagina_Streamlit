from turtle import width
from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


#icono de página
icono = Image.open("Icono_diabetes.png")

##Configurar nombre de pagina
st.set_page_config(page_title="Mi APP_Diabetes", page_icon=icono, layout="wide")

##Agregar titulo y descripcion
st.sidebar.header("La diabetes no siempre se siente, pero siempre cuenta. Cada decisión diaria puede marcar la diferencia entre el riesgo y el bienestar.")
st.markdown("<h1 style='color:blue;'>Predicción de la Diabetes</h1>", unsafe_allow_html=True)
##st.write("La diabetes es una condición crónica que afecta la forma en que el cuerpo utiliza la glucosa, su principal fuente de energía. Existen diferentes tipos de diabetes, y cada uno requiere cuidados especiales para mantener una buena calidad de vida. El objetivo de esta página es brindar información básica, fomentar la conciencia sobre la importancia de la prevención y promover hábitos saludables que ayuden a controlar la enfermedad.")


# 🔷 DESCRIPCIÓN EN CAJA VISUAL
st.markdown("""
La <b>diabetes</b> es una condición crónica que afecta la forma en que el cuerpo utiliza la glucosa, 
su principal fuente de energía. Existen diferentes tipos de diabetes, y cada uno requiere cuidados 
especiales para mantener una buena calidad de vida.<br><br>

</div>

""", unsafe_allow_html=True)

with open("ReflexivoDiabetes.mp4", "rb") as video_file:
    st.video(video_file.read(), start_time=0)



