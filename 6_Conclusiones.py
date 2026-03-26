import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.title("Análisis de Riesgo de Diabetes")

st.write("""Este proyecto analiza un dataset de factores de riesgo de diabetes
como edad, IMC, presión arterial y glucosa para identificar patrones
asociados al riesgo de desarrollar la enfermedad.
""")
#-------

st.header("Objetivos")

st.write("""- Analizar factores de riesgo asociados a la diabetes.
- Identificar patrones en variables como edad, glucosa y BMI.
- Visualizar tendencias y distribución de los datos.
""")

#-------

df= pd.read_csv("diabetes_risk_dataset.csv")

st.header("Dataframe")
st.dataframe(df)
ID_paciente = st.selectbox("Seleccionar paciente",df.index)
st.write(df.loc[ID_paciente])
#-------

st.header("Filtros")

@st.cache_data
def load_data():
    return pd.read_csv("diabetes_risk_dataset.csv")
df = load_data()
st.sidebar.header("Filtros")
min_age = int(df["age"].dropna().min())
max_age = int(df["age"].dropna().max())
edad = st.sidebar.slider("Edad", min_age, max_age, (min_age, max_age))
df = df[(df["age"] >= edad[0]) & (df["age"] <= edad[1])]

@st.cache_data
def load_data():
    return pd.read_csv("diabetes_risk_dataset.csv")
df = load_data()
st.sidebar.header("Filtros")
min_bmi = float(df["bmi"].dropna().min())
max_bmi = float(df["bmi"].dropna().max())
imc = st.sidebar.slider("IMC",min_value=min_bmi,max_value=max_bmi,value=(min_bmi, max_bmi),step=0.1)
df = df[(df["bmi"] >= imc[0]) & (df["bmi"] <= imc[1])]
#-------

@st.cache_data
def load_data():
    return pd.read_csv("diabetes_risk_dataset.csv")
df = load_data()
st.sidebar.header("Filtros")
genero = st.sidebar.selectbox("Género",["Todos", "Female", "Male"])
if genero == "Female":df = df[df["gender"] == 0]
elif genero == "Male":df = df[df["gender"] == 1]
#-------

st.header("Hallazgos")

st.write("""1. Los pacientes con mayor nivel de glucosa tienen mayor probabilidad
de diagnóstico positivo de diabetes.
2. El BMI alto está asociado con mayor riesgo.
3. La edad también influye en el incremento del riesgo.""")
#-------

st.header("Recomendaciones")

st.write("""- Implementar programas de prevención enfocados en control del peso.
- Promover chequeos de glucosa periódicos en población de riesgo.""")

st.header("Conclusiones")

st.write(""" - La diabetes es una enfermedad crónica que afecta la forma en que el cuerpo utiliza la glucosa. Existen diferentes tipos de diabetes, cada uno con características y tratamientos específicos.