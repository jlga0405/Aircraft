import requests
import json

# Leer la clave API desde el archivo Api.txt
with open("Api.txt", "r") as file:
    API_KEY = file.read().strip()

API_URL = "https://leak-lookup.com/api/search"

def check_email(email, results):
    # Crear los datos para la solicitud POST
    data = {
        "key": API_KEY,
        "type": "email_address",
        "query": email
    }

    # Realizar la solicitud POST
    response = requests.post(API_URL, data=data)

    if response.status_code == 200:
        data = response.json()
        print("Respuesta de la API:", data)

        # Verificar si hay un error
        if data['error'] == "false":
            message = data['message']
            if message:
                breaches = {}
                print(f"El correo {email} ha sido encontrado en las siguientes filtraciones:")
                for breach_site, details in message.items():
                    breaches[breach_site] = details if details else "Sin detalles adicionales"
                results[email] = breaches
            else:
                print(f"No se encontraron filtraciones para el correo {email}.")
                results[email] = "No se encontraron filtraciones"
        else:
            print(f"Error en la respuesta: {data['message']}")
            results[email] = f"Error: {data['message']}"
    else:
        print(f"Error en la solicitud: {response.status_code}")
        results[email] = f"Error en la solicitud: {response.status_code}"

# Lista de correos electrónicos a verificar
emails = [
    "j.garcia@pena.com.ar"
    
]

# Diccionario para almacenar los resultados
results = {}

# Realizar verificación para cada correo en la lista
for email in emails:
    check_email(email, results)

# Guardar los resultados en un archivo JSON
with open("resultados_filtraciones.json", "w") as json_file:
    json.dump(results, json_file, indent=4)

print("Los resultados han sido guardados en 'resultados_filtraciones.json'")
