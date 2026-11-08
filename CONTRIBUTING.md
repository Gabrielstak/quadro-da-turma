# Como trabalhamos

## Ramificação: Trunk-Based

- A branch principal é a `main`. Ela está protegida: só recebe código por Pull Request com o CI verde.
- Cada tarefa vira uma branch **curta** (de preferência 1 dia), por exemplo `feat/lista-tarefas` ou `fix/titulo-vazio`.
- Abra o Pull Request cedo, peça revisão a um colega e faça merge assim que o CI passar.

## Padrão de commits

Formato: `tipo: descrição curta no presente`

| Tipo | Quando usar |
|---|---|
| `feat` | função nova |
| `fix` | correção de erro |
| `test` | testes |
| `ci` | pipelines (GitHub Actions) |
| `docs` | documentação |
| `chore` | ajustes gerais (Dockerfile, dependências) |

Exemplos: `feat: adiciona rota para apagar tarefa`, `ci: roda testes a cada pull request`.

## Versionamento semântico

`vMAIOR.MENOR.CORREÇÃO`

- `v1.0.1`: correção de erro
- `v1.1.0`: função nova
- `v2.0.0`: mudança que quebra o que existia

Cada tag publicada gera a imagem `ghcr.io/<usuario>/<repositorio>:<versao>`.
