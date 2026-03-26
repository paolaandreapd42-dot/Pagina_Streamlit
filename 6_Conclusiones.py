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

st.write(""" - La diabetes es una enfermedad crónica que afecta la forma en que el cuerpo utiliza la glucosa. Existen diferentes tipos de diabetes, cada uno con características y tratamientos específicos.""")
         