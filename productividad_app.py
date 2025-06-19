# productividad_app.py - Versión Streamlit del proyecto "Impacto del Teletrabajo en la Productividad"

import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de página
st.set_page_config(page_title="Análisis de Productividad: Teletrabajo vs Presencial", layout="wide")
st.title("📊 Impacto del Teletrabajo en la Productividad")
st.markdown("""
Este proyecto analiza cómo afecta el **modo de trabajo** (teletrabajo o presencial) a la productividad semanal
medida por tareas completadas, horas trabajadas, pausas diarias y nivel de satisfacción.
""")

# Cargar datos
df = pd.read_csv("datos_productividad.csv")
df = df.dropna()
df = df[df['Horas_Trabajadas'] > 0]  # limpieza básica

# Selección de métrica
metrica = st.selectbox("Selecciona la métrica a analizar:", [
    'Tareas_Completadas', 'Horas_Trabajadas', 'Pausas_Diarias', 'Nivel_Satisfaccion'
])

# Mostrar estadísticas
st.subheader("📌 Estadísticas Descriptivas")
col1, col2 = st.columns(2)
with col1:
    st.write(df.groupby('Modo')[metrica].describe()[['mean', 'std']])
with col2:
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='Modo', y=metrica, palette="Set2", ax=ax)
    st.pyplot(fig)

# Contraste de hipótesis
st.subheader("🔬 Contraste de Hipótesis")
st.markdown("**Hipótesis nula:** No hay diferencia en la métrica seleccionada entre teletrabajo y presencial")

def contraste_hipotesis(df, metrica):
    tele = df[df['Modo'] == 'Teletrabajo'][metrica]
    pres = df[df['Modo'] == 'Presencial'][metrica]
    t_stat, p_valor = stats.ttest_ind(tele, pres, equal_var=False)
    return t_stat, p_valor

if st.button("Ejecutar Contraste"):
    t, p = contraste_hipotesis(df, metrica)
    st.write(f"**t = {t:.4f}, p-valor = {p:.4f}**")
    if p < 0.05:
        st.success("Se rechaza la hipótesis nula. Hay una diferencia significativa.")
    else:
        st.info("No se puede rechazar la hipótesis nula. No hay evidencia de diferencia.")

# Análisis por semana
st.subheader("📅 Análisis Semanal de Satisfacción")
semana_promedio = df.groupby("Semana")["Nivel_Satisfaccion"].mean().reset_index()
fig2, ax2 = plt.subplots()
sns.lineplot(data=semana_promedio, x="Semana", y="Nivel_Satisfaccion", marker="o", ax=ax2)
ax2.set_title("Evolución Semanal del Nivel de Satisfacción")
st.pyplot(fig2)
