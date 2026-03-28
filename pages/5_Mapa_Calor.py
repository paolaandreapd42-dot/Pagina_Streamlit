from turtle import width
from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


st.markdown("<h1 style='color:blue;'>Mapa de calor</h1>", unsafe_allow_html=True)

st.write("""“Mapa de calor que muestra la relación entre distintos factores de riesgo —como edad, IMC, presión arterial, glucosa, colesterol, triglicéridos, actividad física y hábitos de sueño— y su asociación con la probabilidad de desarrollar diabetes. Los colores indican la intensidad de la correlación: valores más altos reflejan una mayor influencia en el riesgo.”.
""")
 #cargar dataset
def cargar_datos():
    df = pd.read_csv('diabetes_risk_dataset.csv')
    df.columns = df.columns.str.strip()
    df.rename(columns={'age': 'edad', 'gender': 'Genero', 'bmi': 'IMC', 'blood_pressure': 'Presión Arterial', 'fasting_glucose_level': 'Glucosa en ayunas', 'insulin_level': 'Nivel de insulina', 'HbA1c_level': 'Nivel de insulina Glicosilada', 'cholesterol_level': 'Nivel de colesterol', 'triglycerides_level': 'Nivel de trigliceridos', 'physical_activity_level': 'Nivel de actividad fisica', 'daily_calorie_intake': 'Ingesta diaria de caloria', 'sugar_intake_grams_per_day': 'Ingesta de azucar g/dia', 'sleep_hours': 'Horas de sueño', 'stress_level':'Nivel de estres', 'family_history_diabetes': 'Historial Familiar', 'waist_circumference_cm': 'Circunferencia de cintura cm', 'diabetes_risk_score': 'Puntuacion de riesgo', 'diabetes_risk_category': 'Categoria de riesgo'}, inplace=True)
    return df
df=cargar_datos()
columns_to_plot = ["edad", "IMC", "Presión Arterial", "Glucosa en ayunas", "Nivel de insulina", "Nivel de insulina Glicosilada", "Nivel de colesterol", "Nivel de trigliceridos", "Nivel de actividad fisica", "Ingesta diaria de caloria", "Ingesta de azucar g/dia", "Horas de sueño", "Nivel de estres", "Circunferencia de cintura cm"
                ]
matriz_correlacion = df[columns_to_plot].corr(numeric_only=True)


fig = go.Figure(data=go.Heatmap(z=matriz_correlacion.values, x=columns_to_plot, y=columns_to_plot, colorscale='Viridis'))
st.plotly_chart(fig)



# Ajuste lineal: y = m*x + b
m, b = np.polyfit(df["IMC"], df["Puntuacion de riesgo"], 1)

# Crear figura con puntos
fig = go.Figure(data=go.Scatter(
    x=df["IMC"], 
    y=df["Puntuacion de riesgo"], 
    mode='markers',
    name="Datos"
))

# Añadir línea de regresión
fig.add_trace(go.Scatter(
    x=[df["IMC"].min(), df["IMC"].max()],
    y=[m*df["IMC"].min()+b, m*df["IMC"].max()+b],
    line=dict(color='red'),
    name="Tendencia"
))

fig.update_layout(
    title="Relación Médica: IMC vs Puntuación de Riesgo",
    xaxis_title="IMC",
    yaxis_title="Puntuación de Riesgo"
)

st.plotly_chart(fig, width=800)
