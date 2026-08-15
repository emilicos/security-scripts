# Python + Bash Pipeline

Ejemplo de integración entre Python y Bash: un script de Python genera datos (estado de conectividad de hosts) en formato JSON, y un script de Bash los recibe, procesa y exporta a CSV.

## ¿Para qué sirve?

Muestra un patrón común en automatización de seguridad/IT: usar Python para lógica y estructuras de datos, y Bash para orquestación y procesamiento rápido en línea de comandos (con fallback automático si `jq` no está instalado).

## Archivos

- `ping_check.py` — genera datos de conectividad de hosts en JSON.
- `run_bash_from_python.py` — ejecuta el pipeline completo desde Python usando `subprocess`.
- `collect_from_python.sh` — recibe el JSON, lo procesa (con `jq` o Python inline como respaldo) y genera un CSV.

## Uso

```bash
python run_bash_from_python.py
```

Esto ejecuta la cadena completa: Python genera datos → Bash los procesa → se exporta `from_python.csv`.

## Posibles mejoras

- Reemplazar los datos simulados de `ping_check.py` por comprobaciones reales (`ping` o `socket`).
- Agregar manejo de timeouts para hosts no alcanzables.
