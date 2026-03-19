from turtle import width
from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

 #cargar dataset
def cargar_datos():
    df = pd.read_csv('diabetes_risk_dataset.csv')
    df.columns = df.columns.str.strip()
    df.rename(columns={'age': 'edad', 'gender': 'Genero', 'bmi': 'IMC', 'blood_pressure': 'Presión Arterial', 'fasting_glucose_level': 'Glucosa en ayunas', 'insulin_level': 'Nivel de insulina', 'HbA1c_level': 'Nivel de insulina Glicosilada', 'cholesterol_level': 'Nivel de colesterol', 'triglycerides_level': 'Nivel de trigliceridos', 'physical_activity_level': 'Nivel de actividad fisica', 'daily_calorie_intake': 'Ingesta diaria de caloria', 'sugar_intake_grams_per_day': 'Ingesta de azucar g/dia', 'sleep_hours': 'Horas de sueño', 'stress_level':'Nivel de estres', 'family_history_diabetes': 'Historial Familiar', 'waist_circumference_cm': 'Circunferencia de cintura cm', 'diabetes_risk_score': 'Puntuacion de riesgo', 'diabetes_risk_category': 'Categoria de riesgo'}, inplace=True)
    return df
df=cargar_datos()

## funcion riesgo
def calcular_riesgo(edad, bmi, glucosa, presion_arterial, insulina, actividad_fisica):
      riesgo = 0
      if edad > 45:
          riesgo += 1
      if bmi > 30:
          riesgo += 1 
      if glucosa > 125:
            riesgo += 1 
      if presion_arterial > 130:
            riesgo += 1  
      if insulina > 200:
            riesgo += 1
      if actividad_fisica < 3:
            riesgo += 1

      return riesgo
 # Input fields for user data
st.write("Para predecir su diabetes, seleccione las siguintes preguntas.")

embarazos = st.number_input("Numero de embarazos", min_value=0, max_value=20, value=0)
glucosa = st.number_input("Nivel de glucosa", min_value=0, max_value=200, value=0)
presion_arterial = st.number_input("Presión arterial", min_value=0, max_value=150, value=0)
skin_thickness = st.number_input("Grosor de la piel", min_value=0, max_value=100, value=0)
insulina = st.number_input("Nivel de insulina", min_value=0, max_value=900, value=0)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=0.0)
edad = st.number_input("Edad", min_value=1, max_value=120, value=1)

    # Button to trigger prediction
if st.button("Predict"):
        # Here you would typically load your trained model and make a prediction
        # For demonstration purposes, we'll just display the input values
        st.write(f"Pregnancies: {embarazos}")
        st.write(f"Glucose Level: {glucosa}")
        st.write(f"Blood Pressure: {presion_arterial}")
        st.write(f"Skin Thickness: {skin_thickness}")
        st.write(f"Insulin Level: {insulina}")
        st.write(f"BMI: {bmi}")
        st.write(f"Edad: {edad}")
 # Placeholder for prediction result

edad = st.slider("Seleccina tu edad", min_value=1, max_value=120, value=1,step=1)
st.write(f"Tu edad es: {edad}")
st.write("Tu riesgo de diabetes es: ", calcular_riesgo(edad, bmi, glucosa, presion_arterial, insulina))



