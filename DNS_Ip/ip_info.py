import requests

def obtener_info_ip(ip):
    token = '3d61f810af3736'  # Tu token de acceso de IPinfo
    url = f"https://ipinfo.io/{ip}?token={token}"
    try:
        response = requests.get(url)
        return response.json()
    except requests.RequestException as e:
        return f"Error al conectar con IPinfo: {e}"

# IP obtenida del dominio 145.aero
ip = "35.190.16.47"
info_ip = obtener_info_ip(ip)

print(f"Información de la IP {ip}:")
for key, value in info_ip.items():
    print(f"{key}: {value}")
