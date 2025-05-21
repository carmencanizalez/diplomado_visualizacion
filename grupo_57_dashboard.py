import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar datos
df = pd.read_csv("data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Título principal del dashboard
st.title("Dashboard Estratégico – Visualización y Análisis de Ventas en tienda")

# Menú lateral
menu = st.sidebar.selectbox("Selecciona una sección", [
    "Vista general", 
    "Ventas Totales en el Tiempo", 
    "Ingresos por Línea de Producto",
    "Distribución por Rating",
    "Gasto por Tipo de Cliente",
    "Costo vs. Ganancia Bruta",
    "Métodos de Pago",
    "Correlación Numérica",
    "Ingreso Bruto por Sucursal y Línea"
])

# Vista general
def vista_general():
    st.header("Vista General del Dataset")
    st.write("### Primeros registros")
    st.dataframe(df.head())

    st.write("### Información de columnas")
    st.write(df.columns.tolist())

    st.markdown("## Variables Seleccionadas y Justificación")
    st.markdown("""
    | Variable               | Justificación                                                                 |
    |------------------------|-------------------------------------------------------------------------------|
    | `Date` y `Time`        | Analizar tendencias temporales de compras                                     |
    | `City` y `Branch`      | Comparar el rendimiento por ubicación                                         |
    | `Customer type`        | Explorar comportamiento de clientes miembros y normales                       |
    | `Gender`               | Explorar diferencias por género                                               |
    | `Product line`         | Determinar qué productos son más populares                                   |
    | `Unit price`, `Quantity`| Relacionadas directamente con el valor de compra                            |
    | `Total` y `Tax 5%`     | Evaluar ingreso y carga fiscal                                                |
    | `Payment`              | Preferencias de pago                                                          |
    | `Rating`               | Nivel de satisfacción del cliente                                             |
    """)

# Ventas totales en el tiempo
def ventas_totales():
    st.header("Evolución de Ventas Totales")
    ventas_diarias = df.groupby("Date")["Total"].sum().reset_index()
    fig = px.line(ventas_diarias, x="Date", y="Total", title="Ventas Totales por Día")
    st.plotly_chart(fig)

# Ingresos por línea de producto
def ingresos_por_producto():
    st.header("Ingresos por Línea de Producto")
    suma_productos = df.groupby("Product line")["Total"].sum().sort_values().reset_index()
    fig = px.bar(suma_productos, x="Total", y="Product line", orientation='h', title="Ingresos por Línea de Producto")
    st.plotly_chart(fig)

# Distribución del Rating
def distribucion_rating():
    st.header("Distribución del Rating de Clientes")
    fig = px.histogram(df, x="Rating", nbins=20, title="Distribución del Rating")
    st.plotly_chart(fig)

# Comparación por tipo de cliente
def gasto_por_tipo_cliente():
    st.header("Gasto por Tipo de Cliente")
    fig = px.box(df, x="Customer type", y="Total", color="Customer type", title="Distribución de Gasto por Tipo de Cliente")
    st.plotly_chart(fig)

# Relación costo vs ganancia
def costo_vs_ganancia():
    st.header("Relación entre Costo y Ganancia Bruta")
    fig = px.scatter(df, x="cogs", y="gross income", color="Branch", title="Costo vs. Ingreso Bruto")
    st.plotly_chart(fig)

# Métodos de pago
def metodos_pago():
    st.header("Métodos de Pago Preferidos")
    metodo = df["Payment"].value_counts().reset_index()
    metodo.columns = ["Método", "Cantidad"]
    fig = px.pie(metodo, names="Método", values="Cantidad", title="Distribución de Métodos de Pago")
    st.plotly_chart(fig)

# Correlación numérica
def correlacion_numerica():
    st.header("Correlación entre Variables Numéricas")
    numeric_cols = ["Unit price", "Quantity", "Tax 5%", "Total", "cogs", "gross income", "Rating"]
    corr = df[numeric_cols].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Ingreso bruto por sucursal y línea de producto
def ingreso_por_sucursal_y_producto():
    st.header("Ingreso Bruto por Sucursal y Línea de Producto")
    agrupado = df.groupby(["Branch", "Product line"])["gross income"].sum().reset_index()
    fig = px.sunburst(agrupado, path=["Branch", "Product line"], values="gross income", title="Ingreso Bruto por Sucursal y Producto")
    st.plotly_chart(fig)

# Lógica del menú
if menu == "Vista general":
    vista_general()
elif menu == "Ventas Totales en el Tiempo":
    ventas_totales()
elif menu == "Ingresos por Línea de Producto":
    ingresos_por_producto()
elif menu == "Distribución por Rating":
    distribucion_rating()
elif menu == "Gasto por Tipo de Cliente":
    gasto_por_tipo_cliente()
elif menu == "Costo vs. Ganancia Bruta":
    costo_vs_ganancia()
elif menu == "Métodos de Pago":
    metodos_pago()
elif menu == "Correlación Numérica":
    correlacion_numerica()
elif menu == "Ingreso Bruto por Sucursal y Línea":
    ingreso_por_sucursal_y_producto()