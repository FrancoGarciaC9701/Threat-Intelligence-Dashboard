# Threat Intelligence Dashboard

🛡️ **Threat Intelligence Dashboard** es una aplicación interactiva desarrollada con Streamlit, diseñada para visualizar y analizar feeds de amenazas, IOCs (Indicators of Compromise) y generar reportes en diferentes formatos. 

Este proyecto tiene como objetivo ofrecer una forma visual y práctica de analizar datos de ciberseguridad, facilitando la detección de amenazas y la creación de reportes sobre la seguridad de una red.

## Características

- **Feeds de Amenazas:** Visualización de datos sobre amenazas obtenidos en tiempo real desde OTX (Open Threat Exchange).
- **Análisis de IOCs:** Carga y análisis de archivos CSV o STIX con indicadores de compromiso (IOCs).
- **Visualización Gráfica:** Generación de gráficos para mostrar la distribución de amenazas por país y severidad.
- **Generación de Reportes:** Posibilidad de generar reportes en formato JSON y PDF.
- **Descarga de Gráficos:** Opción para descargar los gráficos generados como imágenes PNG.

## Requisitos

Para ejecutar esta aplicación, necesitarás tener instalados los siguientes paquetes:

- `streamlit`
- `plotly`
- `matplotlib`
- `pandas`
- `reportlab`
- `requests`

Puedes instalar todas las dependencias ejecutando:

- pip install -r requirements.txt

## Instalación

1. Clonar el repositorio:
  - git clone https://github.com/tu_usuario/threat-intelligence-dashboard.git

2. Instalar las dependencias:
  - cd threat-intelligence-dashboard
  - pip install -r requirements.txt

3. Ejecutar la aplicación:
  - streamlit run app.py

## Funcionalidades

1. Feeds de Amenazas
En esta sección, se cargan y muestran los feeds de amenazas desde OTX (Open Threat Exchange). Los resultados incluyen la IP, tipo de amenaza y la última actualización.

2. Análisis de IOC
Puedes cargar archivos CSV o STIX que contienen IOCs. Los indicadores se leen y se muestran para su análisis.

3. Visualización Gráfica
Se generan dos gráficos:

- Gráfico de Barras: Muestra la cantidad de amenazas por país.
- Gráfico de Pie: Muestra la distribución de amenazas por severidad.

4. Generación de Reportes
Los reportes generados se pueden descargar en formato JSON o PDF, y contienen información detallada sobre las amenazas, como país, cantidad de amenazas y severidad.

5. Descarga de Gráficos
Los gráficos generados se pueden descargar como imágenes PNG.

## Configuración
La aplicación requiere una clave API de OTX para obtener los feeds de amenazas. Asegúrate de añadir tu clave en el archivo config.py.
- OTX_API_KEY = "tu_clave_otx"

## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor realiza un fork y envía un pull request.

## Contacto
https://www.linkedin.com/in/franco-garcia9701/ | https://github.com/FrancoGarciaC9701

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

