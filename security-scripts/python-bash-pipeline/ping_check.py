#!/usr/bin/env python3
import json
from pathlib import Path

# Datos simulados — puedes cambiar los hosts si quieres
data = [
    {"host": "8.8.8.8", "reachable": True},
    {"host": "1.1.1.1", "reachable": True},
    {"host": "127.0.0.1", "reachable": True},
]

# Ruta del archivo de salida
out = Path.home() / "work35" / "outputs" / "python_data.json"
out.parent.mkdir(parents=True, exist_ok=True)

# Guardar el JSON en archivo
with open(out, "w") as f:
    json.dump(data, f)

# También imprimirlo en pantalla para que Bash lo use
print(json.dumps(data))


