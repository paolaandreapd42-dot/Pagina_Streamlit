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

df['Genero'] = df['Genero'].replace({
        'Male': 'Hombre',
        'Female': 'Mujer'
    })

df['Nivel de actividad fisica'] = df['Nivel de actividad fisica'].replace({
        'Low': 'Bajo',
        'Moderate': 'Moderado',
        'High': 'Alto'
    })

df['Historial Familiar'] = df['Historial Familiar'].replace({
        'Yes': 'Si',
        'No': 'No'
    })

df['Categoria de riesgo'] = df['Categoria de riesgo'].replace({
        'Prediabetes': 'Prediabetes',
        'Low Risk': 'Bajo riesgo',
        'High Risk': 'Alto riesgo'
    })
filtro_Edad = st.slider("Selecciona el rango de edad", int(df['edad'].min()), int(df['edad'].max()), (int(df['edad'].min()), int(df['edad'].max())))

filtro_Genero = st.selectbox("Selecciona el género", ["Todos"] + df['Genero'].unique().tolist())

filtro_IMC = st.slider("Selecciona el rango de IMC", float(df['IMC'].min()), float(df['IMC'].max()), (float(df['IMC'].min()), float(df['IMC'].max())))

filtro_Actividad_fisica =st.multiselect("Selecciona el nivel de actividad física", ["Todos"] + df['Nivel de actividad fisica'].unique().tolist())

filtro_nivel_estres = st.slider("Selecciona el rango de nivel de estrés", float(df['Nivel de estres'].min()), float(df['Nivel de estres'].max()), (float(df['Nivel de estres'].min()), float(df['Nivel de estres'].max())))

filtro_categoria_riesgo = st.multiselect("Selecciona la categoría de riesgo", ["Todos"] + df['Categoria de riesgo'].unique().tolist())

#df_busqueda = df.query("edad >= @filtro_Edad[0] and edad <= @filtro_Edad[1] and IMC >= @filtro_IMC[0] and IMC <= @filtro_IMC[1] and `Nivel de estres` >= @filtro_nivel_estres[0] and `Nivel de estres` <= @filtro_nivel_estres[1]"  + (" and Genero == @filtro_Genero" if filtro_Genero != "Todos" else " + (" and `Nivel de actividad fisica` in @filtro_Actividad_fisica" if filtro_Actividad_fisica and "Todos" not in filtro_Actividad_fisica else " + (" and `Categoria de riesgo` in @filtro_categoria_riesgo" if filtro_categoria_riesgo and "Todos" not in filtro_categoria_riesgo else "")))

query_1 = "edad >= @filtro_Edad[0] and edad <= @filtro_Edad[1] and IMC >= @filtro_IMC[0] and IMC <= @filtro_IMC[1] and `Nivel de estres` >= @filtro_nivel_estres[0] and `Nivel de estres` <= @filtro_nivel_estres[1]"
if filtro_Genero != "Todos":
    query_1 += " and Genero == @filtro_Genero"
if filtro_Actividad_fisica and "Todos" not in filtro_Actividad_fisica:
    query_1 += " and `Nivel de actividad fisica` in @filtro_Actividad_fisica"
if filtro_categoria_riesgo and "Todos" not in filtro_categoria_riesgo:
    query_1 += " and `Categoria de riesgo` in @filtro_categoria_riesgo"

df_busqueda = df.query(query_1)


st.dataframe(df_busqueda)
## Mostrar la tabla completa


