import streamlit as st
from src.api_client import check_ip_abuseipdb, check_ip_virustotal
from src.utils import parse_abuseipdb_response, parse_virustotal_response
import config

# Configuración inicial del Dashboard
st.set_page_config(page_title="Threat Intelligence Dashboard", layout="wide")
st.title("🚨 Threat Intelligence Dashboard")
st.markdown("Consulta información de amenazas sobre direcciones IP utilizando **AbuseIPDB** y **VirusTotal**.")

# Input del usuario
ip_address = st.text_input("Ingresa una dirección IP para analizar:")

# Botón para iniciar análisis
if st.button("Analizar IP"):

    if ip_address:
        with st.spinner("Analizando la IP, por favor espera..."):
            # Consulta AbuseIPDB
            abuseipdb_raw = check_ip_abuseipdb(ip_address, config.ABUSEIPDB_API_KEY)
            abuseipdb_data = parse_abuseipdb_response(abuseipdb_raw)

            # Consulta VirusTotal
            virustotal_raw = check_ip_virustotal(ip_address, config.VIRUSTOTAL_API_KEY)
            virustotal_data = parse_virustotal_response(virustotal_raw)

        st.success("✅ Análisis completado!")

        # Mostramos resultados
        st.subheader("Resultados de AbuseIPDB")
        st.json(abuseipdb_data)

        st.subheader("Resultados de VirusTotal")
        st.json(virustotal_data)

    else:
        st.warning("Por favor, ingresa una dirección IP válida para continuar.")
