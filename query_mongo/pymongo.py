from pymongo import MongoClient

# Configura la conexión a tu clúster de MongoDB Atlas
cliente = MongoClient("URI_de_tu_cluster")

# Selecciona la base de datos y la colección
db = cliente["nombre_de_tu_base_de_datos"]
coleccion = db["nombre_de_tu_coleccion"]

# Datos de las 399 partes (solo un ejemplo, reemplaza con tus datos reales)
partes = [
    {"parte": 1, "campo1": "valor1", "campo2": "valor2", ...},
    {"parte": 2, "campo1": "valor1", "campo2": "valor2", ...},
    # ... y así sucesivamente
]

# Inserta los datos en la colección
coleccion.insert_many(partes)

# Busca una parte específica (por ejemplo, parte 1)
parte_buscada = coleccion.find_one({"parte": 1})

if parte_buscada:
    print("Parte encontrada:")
    print(parte_buscada)
else:
    print("Parte no encontrada")

# Cierra la conexión
cliente.close()
