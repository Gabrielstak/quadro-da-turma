#!/usr/bin/env bash
# Teste rápido depois do deploy.
# Uso: bash scripts/smoke_test.sh [URL] [VERSAO_ESPERADA]
set -euo pipefail

URL="${1:-http://localhost:8000}"
ESPERADA="${2:-}"

echo "Esperando a API responder em $URL ..."
OK=0
for _ in $(seq 1 20); do
  if curl -fsS "$URL/health" > /dev/null 2>&1; then OK=1; break; fi
  sleep 3
done
if [ "$OK" != "1" ]; then
  echo "ERRO: a API não respondeu."
  exit 1
fi

VERSAO=$(curl -fsS "$URL/version" | python3 -c "import sys, json; print(json.load(sys.stdin)['versao'])")
echo "Versão em execução: $VERSAO"
if [ -n "$ESPERADA" ] && [ "$VERSAO" != "$ESPERADA" ]; then
  echo "ERRO: esperada $ESPERADA, mas está rodando $VERSAO"
  exit 1
fi

curl -fsS -X POST "$URL/api/tarefas" \
  -H 'Content-Type: application/json' \
  -d '{"titulo":"teste de fumaça"}' > /dev/null
echo "OK: API saudável e gravando no banco."
