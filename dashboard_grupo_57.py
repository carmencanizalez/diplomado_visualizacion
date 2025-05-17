import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de página
st.set_page_config(page_title="Dashboard Grupo 57", layout="wide")

# Título
st.title("Dashboard Estratégico: Visualización de Ventas para Tienda Retail")
st.markdown("### Diplomado de Visualización de Datos – Grupo 57")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    return df

df = load_data()

# Sidebar para navegación
menu = st.sidebar.selectbox(
    "Selecciona una sección",
    ["Vista general", "Análisis descriptivo", "Visualizaciones 2D", "Visualización 3D", "Reflexión final"]
)

# --- Sección: Vista general
if menu == "Vista general":
    st.subheader("Vista previa de los datos")
    st.dataframe(df.head())

    st.subheader("Resumen estadístico")
    st.dataframe(df.describe())

    st.subheader("Columnas disponibles")
    st.write(df.columns.tolist())

# --- Sección: Análisis descriptivo
elif menu == "Análisis descriptivo":
    st.subheader("Variables categóricas más frecuentes")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Género")
        st.bar_chart(df["Gender"].value_counts())

        st.write("Tipo de Cliente")
        st.bar_chart(df["Customer type"].value_counts())

    with col2:
        st.write("Método de Pago")
        st.bar_chart(df["Payment"].value_counts())

        st.write("Ciudad")
        st.bar_chart(df["City"].value_counts())

# --- Sección: Visualizaciones 2D
elif menu == "Visualizaciones 2D":
    st.subheader("Relaciones y Distribuciones")

    fig1, ax1 = plt.subplots()
    sns.boxplot(x="Payment", y="Total", data=df, ax=ax1)
    ax1.set_title("Distribución del Total según Método de Pago")
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    sns.scatterplot(x="Total", y="Quantity", hue="Rating", data=df, palette="viridis", ax=ax2)
    ax2.set_title("Total vs Cantidad con Rating")
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    sns.histplot(df["Rating"], bins=10, kde=True, ax=ax3)
    ax3.set_title("Distribución de Rating")
    st.pyplot(fig3)

# --- Sección: Visualización 3D
elif menu == "Visualización 3D":
    from mpl_toolkits.mplot3d import Axes3D

    st.subheader("Visualización 3D: Total vs Quantity vs Rating")

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(df["Total"], df["Quantity"], df["Rating"], c=df["Rating"], cmap="viridis", alpha=0.6)
    ax.set_xlabel("Total")
    ax.set_ylabel("Quantity")
    ax.set_zlabel("Rating")
    ax.set_title("Relación 3D entre Total, Cantidad y Rating")
    fig.colorbar(scatter, ax=ax, label='Rating')
    st.pyplot(fig)

# --- Sección: Reflexión final
elif menu == "Reflexión final":
    st.subheader("Reflexión crítica y experiencia con el dashboard")

    st.markdown("""
    - La posibilidad de interactuar con los datos a través de un dashboard permite descubrir patrones, 
      validar hipótesis y tomar decisiones informadas sin necesidad de conocimientos técnicos avanzados.
    - La visualización 3D, aunque impactante, puede ser menos intuitiva que gráficos simples. Su uso debe 
      justificarse por la complejidad de los datos.
    - El análisis descriptivo reveló, por ejemplo, cómo ciertas ciudades concentran más ventas o cómo los 
      métodos de pago pueden influir en el gasto.
    - Esta experiencia permitió aplicar conceptos teóricos de visualización, reforzando la importancia de 
      la claridad, jerarquía visual y narrativa de datos.
    """)