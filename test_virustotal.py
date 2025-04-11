from src.api_client import check_ip_virustotal
from src.utils import parse_virustotal_response
import config

ip = "8.8.8.8"

result = check_ip_virustotal(ip, config.VIRUSTOTAL_API_KEY)

if result:
    parsed = parse_virustotal_response(result)
    print(parsed)
else:
    print("No se pudo obtener información.")
