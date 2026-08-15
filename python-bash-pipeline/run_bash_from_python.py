import subprocess
import json
from pathlib import Path

# Ruta al script Bash
bash_script = str(Path.home() / "work35" / "bash" / "collect_from_python.sh")

print("🚀 Ejecutando script Bash desde Python...\n")

# Ejecutar el script Bash
result = subprocess.run(["bash", bash_script], capture_output=True, text=True)

# Mostrar la salida del script Bash
print("📜 Salida del script Bash:")
print(result.stdout)
print("--------------------------------------")

# Mostrar errores si los hubiera
if result.stderr:
    print("⚠️ Errores detectados:")
    print(result.stderr)
else:
    print("✅ Sin errores detectados.")

