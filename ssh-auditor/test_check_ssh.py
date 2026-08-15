"""
Ejemplo de uso de check_ssh() contra un conjunto de hosts/credenciales.
Modifica la lista `pruebas` segun tu entorno de laboratorio autorizado.
"""

from check_ssh import check_ssh

# IPs y credenciales de ejemplo (modifica segun tu entorno de pruebas)
pruebas = [
    ("192.168.1.10", "admin", "1234"),
    ("192.168.1.11", "root", "toor"),
]

for ip, user, pwd in pruebas:
    resultado = check_ssh(ip, user, pwd, log_path="ssh_log.jsonl")
    estado = "Conectado" if resultado else "Fallo"
    print(f"{ip} -> {estado}")
