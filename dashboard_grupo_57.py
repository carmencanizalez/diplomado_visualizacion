import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(layout="wide")

# --- Cargar datos ---
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    return df

df = load_data()

# --- Filtros en barra lateral ---
st.sidebar.title("Filtros")
ciudades = st.sidebar.multiselect("Selecciona ciudad", df["City"].unique(), default=df["City"].unique())
generos = st.sidebar.multiselect("Selecciona género", df["Gender"].unique(), default=df["Gender"].unique())
productos = st.sidebar.multiselect("Línea de producto", df["Product line"].unique(), default=df["Product line"].unique())

df_filtrado = df[
    (df["City"].isin(ciudades)) & 
    (df["Gender"].isin(generos)) & 
    (df["Product line"].isin(productos))
]

# --- Título principal ---
st.title("Dashboard interactivo de ventas en supermercado")

# --- Métricas clave ---
st.subheader("Resumen")
col1, col2, col3 = st.columns(3)
col1.metric("Total vendido", f"${df_filtrado['Total'].sum():,.2f}")
col2.metric("Cantidad promedio", f"{df_filtrado['Quantity'].mean():.2f}")
col3.metric("Rating promedio", f"{df_filtrado['Rating'].mean():.2f}")

# --- Gráfico 1: Ventas por ciudad ---
st.subheader("Ventas por ciudad")
fig1, ax1 = plt.subplots()
sns.barplot(data=df_filtrado, x="City", y="Total", estimator=sum, ci=None, ax=ax1)
st.pyplot(fig1)

# --- Gráfico 2: Promedio por producto ---
st.subheader("Promedio de ventas por línea de producto")
fig2, ax2 = plt.subplots()
sns.barplot(data=df_filtrado, x="Product line", y="Total", estimator=np.mean, ci=None, ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# --- Gráfico 3: Distribución de calificación por género ---
st.subheader("Distribución de calificación por género")
fig3, ax3 = plt.subplots()
sns.boxplot(data=df_filtrado, x="Gender", y="Rating", ax=ax3)
st.pyplot(fig3)