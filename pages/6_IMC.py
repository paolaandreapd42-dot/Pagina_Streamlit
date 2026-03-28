from PIL import Image
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np   # 👈 IMPORTANTE

st.markdown("<h1 style='color:blue;'>Distribución del Índice de Masa Corporal (IMC)</h1>", unsafe_allow_html=True)
st.write("""Mapa de calor que ilustra cómo se distribuyen los valores de IMC en la muestra, facilitando la identificación de zonas con mayor prevalencia de sobrepeso u obesidad.""")

# cargar dataset
def cargar_datos():
    df = pd.read_csv('diabetes_risk_dataset.csv')
    df.columns = df.columns.str.strip()
    df.rename(columns={
        'age': 'edad',
        'gender': 'Genero',
        'bmi': 'IMC',
        'blood_pressure': 'Presión Arterial',
        'fasting_glucose_level': 'Glucosa en ayunas',
        'insulin_level': 'Nivel de insulina',
        'HbA1c_level': 'Nivel de insulina Glicosilada',
        'cholesterol_level': 'Nivel de colesterol',
        'triglycerides_level': 'Nivel de trigliceridos',
        'physical_activity_level': 'Nivel de actividad fisica',
        'daily_calorie_intake': 'Ingesta diaria de caloria',
        'sugar_intake_grams_per_day': 'Ingesta de azucar g/dia',
        'sleep_hours': 'Horas de sueño',
        'stress_level':'Nivel de estres',
        'family_history_diabetes': 'Historial Familiar',
        'waist_circumference_cm': 'Circunferencia de cintura cm',
        'diabetes_risk_score': 'Puntuacion de riesgo',
        'diabetes_risk_category': 'Categoria de riesgo'
    }, inplace=True)
    return df

df = cargar_datos()

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

# Mostrar gráfico en Streamlit
st.plotly_chart(fig, use_container_width=True)



