import requests

def obtener_cabeceras_http(ip):
    url = f"http://{ip}"
    try:
        response = requests.head(url)
        return response.headers
    except requests.RequestException as e:
        return f"Error al conectar con {ip}: {e}"

# IP obtenida del dominio 145.aero
ip = "35.190.16.47"
cabeceras = obtener_cabeceras_http(ip)

print(f"Cabeceras HTTP de {ip}:")
for key, value in cabeceras.items():
    print(f"{key}: {value}")
