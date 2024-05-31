import dns.resolver
import socket
import time

# Configurar resolver DNS con servidores DNS de Google
resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '8.8.4.4']

def probar_conectividad():
    try:
        socket.create_connection(("8.8.8.8", 53))
        print("Conectividad a Internet: OK")
    except OSError:
        print("Sin conectividad a Internet")

def probar_resolucion_basica():
    try:
        datos = socket.gethostbyname_ex("google.com")
        print("Resolución de google.com exitosa:", datos)
    except socket.gaierror as e:
        print("Error al resolver google.com:", e)

def obtener_ips(dominio):
    ips = set()

    try:
        # Obtener registros A (IPv4)
        try:
            respuestas = resolver.query(dominio, 'A')
            for rdata in respuestas:
                ips.add(rdata.to_text())
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout) as e:
            print(f"No se pudieron obtener registros A para {dominio}: {e}")

        # Obtener registros AAAA (IPv6)
        try:
            respuestas = resolver.query(dominio, 'AAAA')
            for rdata in respuestas:
                ips.add(rdata.to_text())
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout) as e:
            print(f"No se pudieron obtener registros AAAA para {dominio}: {e}")

        # Obtener registros CNAME (nombre canónico)
        try:
            respuestas = resolver.query(dominio, 'CNAME')
            for rdata in respuestas:
                cname = rdata.to_text()
                ips.update(obtener_ips(cname))
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout) as e:
            print(f"No se pudieron obtener registros CNAME para {dominio}: {e}")

    except dns.resolver.NoNameservers as e:
        print(f"No se pudo contactar con los servidores DNS para {dominio}: {e}")

    # Método alternativo con socket
    try:
        datos = socket.gethostbyname_ex(dominio)
        for ip in datos[2]:
            ips.add(ip)
    except socket.gaierror as e:
        print(f"Error con socket al resolver {dominio}: {e}")

    return ips

# Probar conectividad a Internet
probar_conectividad()

# Probar resolución DNS básica
probar_resolucion_basica()

# Dominios a consultar
dominios = ["145.aero"]
ips_totales = {dominio: set() for dominio in dominios}

# Realizar múltiples consultas para capturar posibles rotaciones de IPs
for dominio in dominios:
    for _ in range(5):  # Puedes aumentar el número de intentos
        ips = obtener_ips(dominio)
        ips_totales[dominio].update(ips)
        time.sleep(1)  # Esperar 1 segundo entre consultas

# Imprimir las IPs asociadas con cada dominio
for dominio, ips in ips_totales.items():
    print(f"IPs asociadas con {dominio}:")
    for ip in ips:
        print(ip)
