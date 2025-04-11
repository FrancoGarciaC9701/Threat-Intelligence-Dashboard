import requests
import pandas as pd

def check_ip_abuseipdb(ip_address, api_key):
    url = "https://api.abuseipdb.com/api/v2/check"

    querystring = {
        "ipAddress": ip_address,
        "maxAgeInDays": "90"  # Opcional: últimos 90 días
    }

    headers = {
        "Accept": "application/json",
        "Key": api_key
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def check_ip_virustotal(ip_address, api_key):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"

    headers = {
        "x-apikey": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Función para obtener feeds de amenazas de OTX
def get_threat_feed_otx(api_key):
    url = "https://otx.alienvault.com/api/v1/indicators/export"
    headers = {
        "X-OTX-API-KEY": api_key
    }
    params = {
        "limit": 10,  # Limitar el número de resultados
        "indicator_type": "IP"  # Puedes filtrar por tipo de indicador (IP, dominio, URL)
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()  # Retorna el feed de amenazas
    else:
        return None

# Función para leer IOCs desde un archivo CSV
def read_iocs(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        return f"Error al leer el archivo: {str(e)}"
