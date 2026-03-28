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
    df.rename(columns={'age': 'edad', 'gender': 'Genero', 'bmi': 'imc', 'blood_pressure': 'Presión Arterial', 'fasting_glucose_level': 'Glucosa en ayunas', 'insulin_level': 'Nivel de insulina', 'HbA1c_level': 'Nivel de insulina Glicosilada', 'cholesterol_level': 'Nivel de colesterol', 'triglycerides_level': 'Nivel de trigliceridos', 'physical_activity_level': 'Nivel de actividad fisica', 'daily_calorie_intake': 'Ingesta diaria de caloria', 'sugar_intake_grams_per_day': 'Ingesta de azucar g/dia', 'sleep_hours': 'Horas de sueño', 'stress_level':'Nivel de estres', 'family_history_diabetes': 'Historial Familiar', 'waist_circumference_cm': 'Circunferencia de cintura cm', 'diabetes_risk_score': 'Puntuacion de riesgo', 'diabetes_risk_category': 'Categoria de riesgo'}, inplace=True)
    return df
df=cargar_datos()

st.markdown("<h1 style='color:blue;'>Calculadora de Riesgo de Diabetes</h1>", unsafe_allow_html=True)   
st.write("""En esta sección se puede calcular el riesgo de desarrollar diabetes, según sus resultados de examanes médicos, asi como los factores de riesgo y prevalencia de diabetes en la familia.""")


## funcion riesgo
def calcular_riesgo(edad, imc, glucosa, presion_arterial, insulina, actividad_fisica):
      riesgo = 0
      if edad > 45:
          riesgo += 1
      if imc > 30:
          riesgo += 1 
      if glucosa > 125:
            riesgo += 1 
      if presion_arterial > 130:
            riesgo += 1  
      if insulina > 200:
            riesgo += 1
      if actividad_fisica == "low":
            riesgo += 1

      return riesgo
 # Input fields for user data

st.write("Para predecir su diabetes, seleccione las siguintes preguntas.")

embarazos = st.number_input("Numero de embarazos", min_value=0, max_value=20, value=0)
glucosa = st.number_input("Nivel de glucosa", min_value=0, max_value=200, value=0)
presion_arterial = st.number_input("Presión arterial", min_value=0, max_value=150, value=0)
insulina = st.number_input("Nivel de insulina", min_value=0, max_value=900, value=0)
peso = st.number_input("Peso", min_value=0.0, max_value=200.0, value=0.0)
altura = st.number_input("Altura", min_value=0.0, max_value=250.0, value=0.0)
if peso > 0 and altura > 0:
    imc = peso / (altura / 100) ** 2
else:
    imc = 0
edad = st.number_input("Edad", min_value=1, max_value=120, value=1)
actividad_fisica = st.selectbox("Nivel de actividad física", ["Baja", "Media", "Alta"])
  
# Calcular el resultado
resultado = calcular_riesgo(edad, imc, glucosa, presion_arterial, insulina, actividad_fisica)

st.write("Tu riesgo de diabetes es:", resultado)

# Clasificación del riesgo (ajusta los rangos a tu modelo)
if resultado < 2:
    riesgo = "bajo"
elif 2 <= resultado < 4:
    riesgo = "moderado"
else:
    riesgo = "alto"

# Mostrar columnas
col1, col2, col3 = st.columns(3)

# Columna 1 - Bajo
with col1:
    if riesgo == "bajo":
        st.success("Riesgo bajo ✅")
    else:
        st.header("Riesgo bajo")

    st.write("""
    Mantén un estilo de vida saludable:
    - Alimentación equilibrada
    - Ejercicio regular
    - Evitar tabaco y alcohol
    """)

# Columna 2 - Moderado
with col2:
    if riesgo == "moderado":
        st.warning("Riesgo moderado ⚠️")
    else:
        st.header("Riesgo moderado")

    st.write("""
    Toma medidas para reducir el riesgo:
    - Mejorar la dieta
    - Aumentar actividad física
    - Consultar con un profesional de salud
    """)

# Columna 3 - Alto
with col3:
    if riesgo == "alto":
        st.error("Riesgo alto 🚨")
    else:
        st.header("Riesgo alto")

    st.write("""
    Es importante actuar de inmediato:
    - Consulta médica
    - Control de glucosa
    - Cambios intensivos en estilo de vida
    """)
