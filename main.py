import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("datos_productividad.csv")

def limpiar_datos(df):
    df = df.dropna()
    df = df[df['Horas_Trabajadas'] > 0]
    return df

df = limpiar_datos(df)

def calcular_estadisticas(df, columna):
    estadisticas = {}
    for modo in df['Modo'].unique():
        subset = df[df['Modo'] == modo][columna]
        estadisticas[modo] = {
            'media': round(subset.mean(), 2),
            'desviacion': round(subset.std(), 2),
            'n': len(subset)
        }
    return estadisticas

def contrastar_hipotesis(df, columna):
    tele = df[df['Modo'] == 'Teletrabajo'][columna]
    pres = df[df['Modo'] == 'Presencial'][columna]
    t_stat, p_value = stats.ttest_ind(tele, pres, equal_var=False)
    return round(t_stat, 4), round(p_value, 4)

print("\n--- ANÁLISIS DE PRODUCTIVIDAD ---\n")
columna = 'Tareas_Completadas'
print("Estadísticas por modo de trabajo:")
estadisticas = calcular_estadisticas(df, columna)
for modo, stats_ in estadisticas.items():
    print(f"{modo}: Media = {stats_['media']}, Desviación = {stats_['desviacion']}, n = {stats_['n']}")

print("\nHipótesis nula: No hay diferencia entre teletrabajo y presencial")
t_stat, p_value = contrastar_hipotesis(df, columna)
print(f"t = {t_stat}, p-valor = {p_value}")
if p_value < 0.05:
    print("➡️ Se rechaza la hipótesis nula.")
else:
    print("➡️ No se puede rechazar la hipótesis nula.")

print("\nSatisfacción por semana:")
promedios = df.groupby('Semana')['Nivel_Satisfaccion'].mean().sort_values()
print(f"Menor: Semana {promedios.idxmin()} con media {round(promedios.min(), 2)}")
print(f"Mayor: Semana {promedios.idxmax()} con media {round(promedios.max(), 2)}")
