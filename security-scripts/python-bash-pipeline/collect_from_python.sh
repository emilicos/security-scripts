#!/usr/bin/env bash
# ~/work35/bash/collect_from_python.sh

PY=~/work35/python/ping_check.py
OUT=~/work35/outputs/from_python.csv

echo "🔍 Iniciando recolección desde Python..."

# Verificar que el script Python existe
if [ ! -f "$PY" ]; then
  echo "❌ ERROR: No se encontró el script de Python en $PY" >&2
  exit 1
fi

# Ejecutar el script Python y capturar su salida JSON
echo "🚀 Ejecutando script Python..."
json_out=$(python3 "$PY")

# Mostrar la salida (depuración)
echo "🐍 Salida del script Python:"
echo "$json_out"
echo "--------------------------------------"

# Si la salida está vacía, error
if [ -z "$json_out" ]; then
  echo "❌ ERROR: No se recibió salida JSON del script Python" >&2
  exit 2
fi

mkdir -p ~/work35/outputs

echo "📦 Procesando datos JSON..."
if command -v jq >/dev/null 2>&1; then
  echo "✅ Usando jq para parsear JSON"
  echo "host,reachable" > "$OUT"
  echo "$json_out" | jq -r '.[] | "\(.host),\(.reachable)"' >> "$OUT"
else
  echo "⚙️ No se encontró jq, usando Python inline"
  # Guardar el JSON en un archivo temporal
  tmp_json=$(mktemp)
  echo "$json_out" > "$tmp_json"

  python3 - "$tmp_json" <<'PYCODE' > "$OUT"
import sys, json, pathlib
tmp_path = sys.argv[1]
raw = pathlib.Path(tmp_path).read_text().strip()
if not raw:
    print("ERROR: archivo temporal vacío", file=sys.stderr)
    sys.exit(1)
try:
    data = json.loads(raw)
except json.JSONDecodeError as e:
    print("ERROR al decodificar JSON:", e, file=sys.stderr)
    sys.exit(2)
print("host,reachable")
for e in data:
    print(f"{e['host']},{e['reachable']}")
PYCODE

  rm -f "$tmp_json"
fi

echo "✅ Wrote CSV to $OUT"



