"""
Verificador de brechas de correo electronico usando la API de Have I Been Pwned (HIBP).

Uso:
    python verificar_correo.py correo@ejemplo.com

Requiere una API key de HIBP configurada como variable de entorno:
    export HIBP_API_KEY="tu_api_key_aqui"   (Linux/Mac)
    setx HIBP_API_KEY "tu_api_key_aqui"     (Windows)

La API key se obtiene en: https://haveibeenpwned.com/API/Key
"""

import sys
import requests
import time
import os
import logging
import csv

logging.basicConfig(
    filename="registro.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

if len(sys.argv) != 2:
    print("Uso: python verificar_correo.py correo@ejemplo.com")
    sys.exit(1)

correo = sys.argv[1]

# Lectura segura de la API key desde variable de entorno (nunca desde un
# archivo de texto plano ni hardcodeada en el codigo).
api_key = os.environ.get("HIBP_API_KEY")
if not api_key:
    print("Error: no se encontro la variable de entorno HIBP_API_KEY.")
    print("Configúrala antes de correr el script (ver encabezado del archivo).")
    logging.error("HIBP_API_KEY no configurada.")
    sys.exit(1)

url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{correo}"
headers = {
    "hibp-api-key": api_key,
    "user-agent": "PythonScript-PortfolioProject",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    brechas = response.json()
    logging.info(f"Consulta exitosa para {correo}. Brechas encontradas: {len(brechas)}")

    with open("reporte.csv", "w", newline="", encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(
            ["Titulo", "Dominio", "Fecha de Brecha", "Datos Comprometidos", "Verificada", "Sensible"]
        )

        for i, brecha in enumerate(brechas[:3]):
            nombre = brecha["Name"]
            detalle_url = f"https://haveibeenpwned.com/api/v3/breach/{nombre}"
            detalle_resp = requests.get(detalle_url, headers=headers)

            if detalle_resp.status_code == 200:
                detalle = detalle_resp.json()
                writer.writerow(
                    [
                        detalle.get("Title"),
                        detalle.get("Domain"),
                        detalle.get("BreachDate"),
                        ", ".join(detalle.get("DataClasses", [])),
                        detalle.get("IsVerified"),
                        detalle.get("IsSensitive"),
                    ]
                )
            else:
                logging.error(f"No se pudo obtener detalles de la brecha: {nombre}")
            if i < 2:
                time.sleep(10)
    print(f"Reporte generado en reporte.csv para {correo}")
elif response.status_code == 404:
    print(f"La cuenta {correo} no aparece en ninguna brecha conocida.")
    logging.info(f"Consulta exitosa para {correo}. No se encontraron brechas.")
elif response.status_code == 401:
    print("Error de autenticacion: revisa tu API key.")
    logging.error("Error 401: API key invalida.")
else:
    print(f"Error inesperado. Codigo de estado: {response.status_code}")
    logging.error(f"Error inesperado. Codigo de estado: {response.status_code}")
