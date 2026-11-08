# Evidência de versionamento e rollback

Preencha esta página com **prints** durante a simulação.

## 1. Versão boa publicada

- Tag criada: `v1.0.0`
- Imagem publicada: `ghcr.io/<usuario>/<repositorio>:1.0.0`
- Print do CD verde: (cole aqui)
- Print da página mostrando "Versão em execução: 1.0.0": (cole aqui)

## 2. Versão com falha

- Mudança feita de propósito: no `Dockerfile`, a linha `CMD` foi trocada de porta `8000` para `9000`.
  Os testes continuam passando, mas a aplicação deixa de responder na porta certa.
- Tag criada: `v1.1.0`
- Print do job `deploy-homologacao` **falhando** no teste rápido: (cole aqui)

## 3. Rollback

- Workflow executado: *Rollback (homologação simulada)* com a versão `1.0.0`
- Print do rollback verde (a versão confirmada foi 1.0.0): (cole aqui)

Rollback manual na máquina local (alternativa):

```
set APP_IMAGE=ghcr.io/<usuario>/<repositorio>:1.0.0
docker compose up -d --no-build
```

## 4. Correção definitiva

- A mudança com defeito foi revertida por Pull Request.
- Nova tag: `v1.1.1`
- Print do CD verde: (cole aqui)

## O que aprendemos

(Escreva 3 ou 4 linhas: o que falhou, como percebemos, quanto tempo levou para voltar.)
