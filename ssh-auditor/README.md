# SSH Auditor

Script en Python que prueba autenticación SSH contra un host usando la librería `paramiko`, y registra cada intento en un log estructurado (JSON Lines) con timestamp, IP, usuario y resultado.

## ¿Para qué sirve?

Simula el tipo de comprobación que haría un analista al auditar si credenciales débiles o por defecto (`admin/1234`, `root/toor`, etc.) permiten acceso no autorizado a servidores dentro de un entorno de pruebas propio.

> ⚠️ Solo usar contra hosts de tu propiedad o con autorización explícita para pruebas de seguridad.

## Archivos

- `check_ssh.py` — función principal `check_ssh(ip, usuario, password, log_path)`.
- `test_check_ssh.py` — ejemplo de uso contra una lista de hosts/credenciales.

## Uso

```bash
pip install paramiko
python test_check_ssh.py
```

Cada intento queda registrado en `ssh_log.jsonl`, por ejemplo:

```json
{"timestamp": "2026-08-14T10:32:01", "ip": "192.168.1.10", "usuario": "admin", "exito": false, "error": "Autenticacion fallida"}
```

## Posibles mejoras

- Leer la lista de hosts/credenciales desde un archivo CSV en vez de hardcodearla.
- Agregar límite de intentos / delay para evitar bloqueos por fuerza bruta accidental.
