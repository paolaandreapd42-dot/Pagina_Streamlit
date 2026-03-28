from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
#import os

#icono de página
icono = Image.open("Icono_diabetes.png")

##Configurar nombre de pagina
st.set_page_config(page_title="Mi APP_Diabetes", page_icon=icono, layout="wide")
# Esto obtiene la carpeta donde está guardado diabetes.py
#current_dir = os.path.dirname(__file__)
#path_a_inicio = os.path.join(current_dir, "0_Inicio.py")
#path_a_genero = os.path.join(current_dir, "1_Genero.py")
#path_a_edad = os.path.join(current_dir, "2_Edad.py")
#path_a_tablas = os.path.join(current_dir, "3_Tablas.py")
#path_a_calculadora = os.path.join(current_dir, "4_Calculadora_Riesgo.py")
#path_a_mapa_calor = os.path.join(current_dir, "5_Mapa_Calor.py")
#path_a_imc = os.path.join(current_dir, "6_IMC.py") 
#path_a_conclusiones = os.path.join(current_dir, "7_Conclusiones.py")

##navegacion
pages = [
      st.Page("pages/0_Inicio.py", title="Inicio"),
      st.Page("pages/1_Genero.py", title="Genero"),
      st.Page("pages/2_Edad.py", title="Edad"),
      st.Page("pages/3_Tablas.py", title="Tablas"),
      st.Page("pages/4_Calculadora_Riesgo.py", title="Calculadora de Riesgo"),
      st.Page("pages/5_Mapa_Calor.py", title="Mapa de Calor"),
      st.Page("pages/6_IMC.py", title="IMC"),
      st.Page("pages/7_Conclusiones.py", title="Conclusiones")
]
pg=st.navigation(pages)
pg.run()##navegacion


def main():
        st.sidebar.header("Genero de los pacientes")
    
    #cargar dataset
def cargar_datos():
    df = pd.read_csv('diabetes_risk_dataset.csv')
    df.columns = df.columns.str.strip()
    df.rename(columns={'age': 'edad', 'gender': 'Genero', 'bmi': 'IMC', 'blood_pressure': 'Presión Arterial', 'fasting_glucose_level': 'Glucosa en ayunas', 'insulin_level': 'Nivel de insulina', 'HbA1c_level': 'Nivel de insulina Glicosilada', 'cholesterol_level': 'Nivel de colesterol', 'triglycerides_level': 'Nivel de trigliceridos', 'physical_activity_level': 'Nivel de actividad fisica', 'daily_calorie_intake': 'Ingesta diaria de caloria', 'sugar_intake_grams_per_day': 'Ingesta de azucar g/dia', 'sleep_hours': 'Horas de sueño', 'stress_level':'Nivel de estres', 'family_history_diabetes': 'Historial Familiar', 'waist_circumference_cm': 'Circunferencia de cintura cm', 'diabetes_risk_score': 'Puntuacion de riesgo', 'diabetes_risk_category': 'Categoria de riesgo'}, inplace=True)
    return df
df=cargar_datos()
