# Quadro da Turma

Aplicação web simples para o grupo anotar tarefas e marcar o que já foi entregue.
Projeto da disciplina **Integração DevOps** (Ciência da Computação, CEUB, 2026_2, Prof. Danilo Silva).

## O que tem no projeto

| Requisito da disciplina | Onde está |
|---|---|
| Código-fonte | `app/` (Python + Flask) |
| Interface para interação | `app/templates/index.html` (página web) |
| Banco de dados | PostgreSQL (no Docker Compose) |
| Testes automatizados | `tests/` (pytest, 12 testes) |
| Pipeline de CI | `.github/workflows/ci.yml` |
| Dockerfile | `Dockerfile` (2 etapas, usuário sem root, healthcheck) |
| Orquestração | `docker-compose.yml` (aplicação + banco) |
| Pipeline de CD | `.github/workflows/cd.yml` |
| Segredos | GitHub Secrets (nada de senha no código) |
| Versionamento e rollback | tags `vX.Y.Z`, `rollback.yml` e `docs/rollback.md` |

## Como rodar na sua máquina (precisa do Docker Desktop)

1. Copie `.env.example` para `.env` e troque a senha.
2. Rode `docker compose up --build`.
3. Abra http://localhost:8000.

Para parar: `Ctrl + C` e depois `docker compose down`.

## Rotas

| Rota | O que faz |
|---|---|
| `GET /` | Página do quadro |
| `GET /health` | Mostra se a API está viva |
| `GET /version` | Mostra a versão em execução |
| `GET /api/tarefas` | Lista as tarefas |
| `POST /api/tarefas` | Cria tarefa (`{"titulo": "..."}`) |
| `PUT /api/tarefas/<id>` | Marca como concluída (`{"concluida": true}`) |
| `DELETE /api/tarefas/<id>` | Apaga a tarefa |

## Rodar os testes sem Docker

```
pip install -r requirements-dev.txt
python -m pytest
```

## Como o pipeline funciona

- **CI** (`ci.yml`): a cada push na `main` e a cada Pull Request, roda os testes e confirma que a imagem Docker é construída.
- **CD** (`cd.yml`): ao criar uma tag como `v1.0.0`, roda os testes, publica a imagem no GitHub Container Registry (GHCR) com a versão e faz o deploy simulado em homologação (sobe o Compose e roda o teste rápido).
- **Rollback** (`rollback.yml`): execução manual que volta o ambiente para uma versão anterior. Veja `docs/rollback.md`.

Detalhes de organização do grupo em `docs/divisao-grupo.md` e padrão de trabalho em `CONTRIBUTING.md`.
