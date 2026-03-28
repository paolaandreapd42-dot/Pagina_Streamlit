from turtle import width
from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


 #cargar dataset
def cargar_datos():
    df = pd.read_csv('diabetes_risk_dataset.csv')
    df.columns = df.columns.str.strip()
    df.rename(columns={'age': 'edad', 'gender': 'Genero', 'bmi': 'IMC', 'blood_pressure': 'Presión Arterial', 'fasting_glucose_level': 'Glucosa en ayunas', 'insulin_level': 'Nivel de insulina', 'HbA1c_level': 'Nivel de insulina Glicosilada', 'cholesterol_level': 'Nivel de colesterol', 'triglycerides_level': 'Nivel de trigliceridos', 'physical_activity_level': 'Nivel de actividad fisica', 'daily_calorie_intake': 'Ingesta diaria de caloria', 'sugar_intake_grams_per_day': 'Ingesta de azucar g/dia', 'sleep_hours': 'Horas de sueño', 'stress_level':'Nivel de estres', 'family_history_diabetes': 'Historial Familiar', 'waist_circumference_cm': 'Circunferencia de cintura cm', 'diabetes_risk_score': 'Puntuacion de riesgo', 'diabetes_risk_category': 'Categoria de riesgo'}, inplace=True)
    return df
df=cargar_datos()
df['Categoria de riesgo'] = df['Categoria de riesgo'].replace({
        'Prediabetes': 'Prediabetes',
        'Low Risk': 'Bajo riesgo',
        'High Risk': 'Alto riesgo'
    })
st.markdown("<h1 style='color:blue;'>Análisis de Edad y Riesgo de Diabetes</h1>", unsafe_allow_html=True)
st.write("""En esta sección se analiza la relación entre la edad de los pacientes y su riesgo de desarrollar diabetes. Se observa que a medida que aumenta la edad, también lo hace el riesgo, lo que sugiere que la edad es un factor importante a considerar en la prevención y manejo de la diabetes.""")

## Riesgo por edad
df_avg = df.groupby('Categoria de riesgo')['edad'].mean().reset_index()
fig = px.bar(df_avg, x='Categoria de riesgo', y='edad', title='Edad Promedio por Categoría de Riesgo de Diabetes')
st.plotly_chart(fig, width=800)

