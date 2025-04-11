import streamlit as st
from src.api_client import get_threat_feed_otx, read_iocs
import config
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Configuración básica
st.set_page_config(page_title="Threat Intelligence Dashboard", layout="wide")

# Título principal
st.title("🛡️ Threat Intelligence Dashboard")

# Menú lateral
menu = st.sidebar.selectbox("Selecciona una opción", ["Resumen General", "Feeds de Amenazas", "Análisis IOC", "Visualización Gráfica", "Configuración"])

# Inicializar la variable feed
feed = None  # Definir feed como None por defecto

# Función para obtener feed de amenazas
def obtener_feed():
    global feed
    api_key_otx = config.OTX_API_KEY  # Asegúrate de tener la clave en config.py
    feed = get_threat_feed_otx(api_key_otx)

# Función para generar PDF del reporte
def generate_pdf(df):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    text = c.beginText(40, 750)
    text.setFont("Helvetica", 12)
    text.textLine("Reporte de Amenazas")
    text.textLine("---------------------------")
    for index, row in df.iterrows():
        text.textLine(f"País: {row['País']}, Amenazas: {row['Amenazas']}, Severidad: {row['Severidad']}")
    c.drawText(text)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# Manejo de Feeds de Amenazas
if menu == "Feeds de Amenazas":
    st.header("🌐 Feeds de Amenazas")
    st.write("Aquí vamos a integrar los feeds de inteligencia de amenazas en tiempo real.")

    # Obtener feed de amenazas de OTX
    obtener_feed()

    if feed:
        st.subheader("IP Threat Feed")
        for threat in feed.get("results", []):
            ip = threat.get('indicator', 'N/A')
            tipo = threat.get('type', 'N/A')
            updated_at = threat.get('updated_at', 'No disponible')

            st.write(f"**IP**: {ip}")
            st.write(f"**Tipo**: {tipo}")
            st.write(f"**Última actualización**: {updated_at}")
            st.write("---")
    else:
        st.warning("No se pudieron obtener los feeds de amenazas.")

# Análisis de IOC
elif menu == "Análisis IOC":
    st.sidebar.header("🔍 Análisis de IOC")
    st.write("Sube un archivo CSV o STIX para analizar los IOCs.")

    uploaded_file = st.sidebar.file_uploader("Subí tus archivos de IOCs", type=["csv", "stix"])

    if uploaded_file is not None:
        st.subheader("IOCs cargados desde archivo:")
        try:
            if uploaded_file.type == "text/csv":
                df_ioc = pd.read_csv(uploaded_file)
                st.write(df_ioc)
            else:
                st.write("Archivo STIX aún no procesado.")
        except Exception as e:
            st.error(f"Error al leer el archivo: {e}")
    else:
        st.info("Por favor, subí un archivo de IOCs para comenzar el análisis.")

# Visualización Gráfica
elif menu == "Visualización Gráfica":
    st.header("📈 Visualización Gráfica")
    st.write("Visualización de los feeds de amenazas.")

    # Verificar si los datos de feed están disponibles
    if feed and 'results' in feed:
        # Convertir el feed a un DataFrame
        df = pd.DataFrame(feed.get("results", []))

        # Validar que las columnas necesarias existan
        if all(col in df.columns for col in ['indicator', 'type', 'updated_at']):
            # Primer gráfico - Barras
            st.subheader("Amenazas por País (Barra)")
            df['País'] = df['indicator'].apply(lambda x: x.split('.')[-1])  # Usar un campo para país (Ejemplo)
            df['Amenazas'] = 1  # Suponemos una amenaza por entrada
            df_grouped = df.groupby('País').agg({'Amenazas': 'sum'}).reset_index()

            fig, ax = plt.subplots()
            df_grouped.plot(kind='bar', x='País', y='Amenazas', legend=False, ax=ax, color='skyblue')
            plt.ylabel("Cantidad de Amenazas")
            plt.title("Cantidad de Amenazas por País")
            st.pyplot(fig)

            # Descargar imagen del gráfico
            buf = BytesIO()
            fig.savefig(buf, format="png")
            st.download_button(
                label="📥 Descargar gráfico de barras como imagen",
                data=buf.getvalue(),
                file_name="grafico_barras.png",
                mime="image/png"
            )

            # Segundo gráfico - Pie Chart (Plotly interactivo)
            st.subheader("Distribución de Severidad de Amenazas")
            df['Severidad'] = df['type'].apply(lambda x: 'Alta' if 'High' in x else 'Baja')  # Ejemplo de severidad
            fig2 = px.pie(df, names='Severidad', values='Amenazas', title='Distribución de Severidad')
            st.plotly_chart(fig2)

            # Descargar JSON del reporte
            st.subheader("Generar Reporte de Amenazas")
            report_json = df.to_json(orient="records", indent=2)
            st.download_button(
                label="📥 Descargar Reporte en JSON",
                data=report_json,
                file_name="reporte_amenazas.json",
                mime="application/json"
            )

            # Generar PDF del reporte
            pdf_buffer = generate_pdf(df)
            st.download_button(
                label="📥 Descargar Reporte en PDF",
                data=pdf_buffer,
                file_name="reporte_amenazas.pdf",
                mime="application/pdf"
            )

        else:
            st.warning("El feed no contiene las columnas necesarias para graficar.")

    else:
        st.warning("No se han recibido datos de amenazas para graficar.")

# Resumen General
elif menu == "Resumen General":
    st.header("📊 Resumen General")
    st.write("Bienvenido al resumen general del Dashboard.")

# Configuración
elif menu == "Configuración":
    st.header("⚙️ Configuración")
    st.write("Opciones de configuración del dashboard.")
