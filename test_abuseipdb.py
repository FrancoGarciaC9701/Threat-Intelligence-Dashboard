from src.api_client import check_ip_abuseipdb
from src.utils import parse_abuseipdb_response
import config

ip = "8.8.8.8"

result = check_ip_abuseipdb(ip, config.ABUSEIPDB_API_KEY)

if result:
    parsed = parse_abuseipdb_response(result)
    print(parsed)
else:
    print("No se pudo obtener información.")
