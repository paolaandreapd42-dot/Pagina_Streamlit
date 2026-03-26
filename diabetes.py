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

##navegacion
pg=st.navigation(["0_Inicio.py","1_Genero.py","2_Edad.py", "3_Tablas.py", "4_Calculadora_Riesgo.py", "5_Mapa_Calor.py", "6_Conclusiones.py"])
pg.run()


def main():
        st.sidebar.header("Genero de los pacientes")
    
    #cargar dataset
def cargar_datos():
    df = pd.read_csv('diabetes_risk_dataset.csv')
    df.columns = df.columns.str.strip()
    df.rename(columns={'age': 'edad', 'gender': 'Genero', 'bmi': 'IMC', 'blood_pressure': 'Presión Arterial', 'fasting_glucose_level': 'Glucosa en ayunas', 'insulin_level': 'Nivel de insulina', 'HbA1c_level': 'Nivel de insulina Glicosilada', 'cholesterol_level': 'Nivel de colesterol', 'triglycerides_level': 'Nivel de trigliceridos', 'physical_activity_level': 'Nivel de actividad fisica', 'daily_calorie_intake': 'Ingesta diaria de caloria', 'sugar_intake_grams_per_day': 'Ingesta de azucar g/dia', 'sleep_hours': 'Horas de sueño', 'stress_level':'Nivel de estres', 'family_history_diabetes': 'Historial Familiar', 'waist_circumference_cm': 'Circunferencia de cintura cm', 'diabetes_risk_score': 'Puntuacion de riesgo', 'diabetes_risk_category': 'Categoria de riesgo'}, inplace=True)
    return df
df=cargar_datos()
