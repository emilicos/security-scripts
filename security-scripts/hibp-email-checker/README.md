# HIBP Email Checker

Script en Python que consulta la API de [Have I Been Pwned (HIBP)](https://haveibeenpwned.com/) para verificar si un correo electrónico ha sido expuesto en brechas de datos conocidas, y genera un reporte en CSV con el detalle de las brechas encontradas.

## ¿Para qué sirve?

Automatiza una tarea común de higiene de seguridad: verificar si una cuenta de correo aparece en filtraciones públicas, y documentar qué datos fueron comprometidos, cuándo, y si la brecha está verificada.

## Requisitos

- Una API key de HIBP (se obtiene en [haveibeenpwned.com/API/Key](https://haveibeenpwned.com/API/Key)).
- La key se configura como **variable de entorno**, nunca hardcodeada ni en un archivo de texto plano:

```bash
export HIBP_API_KEY="tu_api_key_aqui"      # Linux/Mac
setx HIBP_API_KEY "tu_api_key_aqui"        # Windows
```

## Uso

```bash
pip install requests
python verificar_correo.py correo@ejemplo.com
```

Genera `reporte.csv` con las brechas encontradas (título, dominio, fecha, tipo de datos comprometidos, si está verificada), y registra la actividad en `registro.log`.

## Nota de seguridad

Una versión anterior de este script leía la API key desde un archivo `apikey.txt` en texto plano. Se corrigió para usar variables de entorno, evitando exponer credenciales por accidente al subir el código a un repositorio.
