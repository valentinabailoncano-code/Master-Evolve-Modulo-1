# 📊 Impacto del Teletrabajo en la Productividad

Este proyecto analiza si existen diferencias significativas en la productividad de los empleados dependiendo del modo de trabajo: **presencial** vs **teletrabajo**.

---

## 🎯 Objetivo

Contrastar la hipótesis de que *no hay diferencia significativa* en métricas clave de desempeño semanal como:

- Tareas completadas
- Horas trabajadas
- Pausas diarias
- Nivel de satisfacción

---

## 📁 Estructura del proyecto

```
teletrabajo-productividad/
├── datos_productividad.csv          # Datos simulados de 30 empleados por 8 semanas
├── main.py                          # Versión terminal del análisis
├── productividad_app.py            # Aplicación Streamlit interactiva
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Este archivo explicativo
```

---

## 🧪 Metodología

1. **Limpieza de datos**: eliminación de registros inválidos
2. **Estadísticas descriptivas** por grupo
3. **Contraste de hipótesis (t-test)** para detectar diferencias significativas
4. **Visualización interactiva** de resultados y evolución semanal

---

## 🚀 Cómo ejecutar

### Terminal
```bash
python main.py
```

### Interfaz interactiva
```bash
streamlit run productividad_app.py
```

---

## 📦 Requisitos

Instala las dependencias con:
```bash
pip install -r requirements.txt
```

---

## 👩‍💻 Autor

**Valentina Bailón Cano**  
Máster en Data Science & IA – Evolve  
[LinkedIn](https://www.linkedin.com/in/valentina-bailon-2653b22b7)

---

## 🧠 Notas

- Dataset simulado pero diseñado con lógica realista
- No se usa ningún dato confidencial
- Este proyecto es de carácter **individual**, entregado para el **Módulo 1**
