# Passo a passo (Windows + VS Code)

## Parte 1: Rodar na sua máquina

1. Extraia o .zip e abra a pasta `devops-tarefas` no VS Code (Arquivo > Abrir Pasta).
2. Abra o terminal (Terminal > Novo Terminal). O caminho deve terminar em `devops-tarefas`.
3. Rode: `Copy-Item .env.example .env`
4. Abra o arquivo `.env` e troque `troque_esta_senha` por uma senha simples.
5. Abra o Docker Desktop e espere o ícone ficar verde.
6. Rode: `docker compose up --build`
7. Abra http://localhost:8000 no navegador e adicione uma tarefa.
8. No terminal, aperte `Ctrl + C` para parar.

## Parte 2: Subir para o GitHub (entrega A1)

1. Crie um repositório vazio no GitHub (sem README).
2. No terminal: `git init -b main`
3. `git add .`
4. `git commit -m "feat: cria aplicação inicial do quadro de tarefas"`
5. `git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git`
6. `git push -u origin main`
7. Aba **Actions** do repositório: confirme que o CI ficou verde.
8. **Settings > Branches > Add rule**: branch `main`, marque *Require a pull request before merging* e *Require status checks to pass* (escolha `testes`).
9. Convide os colegas em **Settings > Collaborators**.
10. Faça pelo menos alguns commits seguindo o padrão do `CONTRIBUTING.md`, cada um em uma branch com Pull Request.

## Parte 3: Segredos e primeira versão (entrega A2)

1. **Settings > Secrets and variables > Actions > New repository secret**.
2. Nome: `DB_PASSWORD`. Valor: uma senha simples. Salve.
3. **Settings > Actions > General > Workflow permissions**: marque *Read and write permissions* e salve.
4. No terminal: `git tag v1.0.0`
5. `git push origin v1.0.0`
6. Aba **Actions**: acompanhe o workflow **CD** até os 3 jobs ficarem verdes.
7. Na página inicial do repositório, em **Packages**, confira a imagem `1.0.0`.
8. Crie uma Release: **Releases > Draft a new release**, escolha a tag `v1.0.0`.

## Parte 4: Simulação de rollback

1. Crie uma branch: `git switch -c fix/teste-falha`
2. No `Dockerfile`, troque `0.0.0.0:8000` por `0.0.0.0:9000` na última linha.
3. `git commit -am "chore: muda porta (teste de falha)"`
4. `git push -u origin fix/teste-falha`, abra o Pull Request e faça o merge.
5. `git switch main` e `git pull`
6. `git tag v1.1.0` e `git push origin v1.1.0`
7. Na aba Actions, o job **deploy-homologacao** deve **falhar**. Tire print.
8. Vá em **Actions > Rollback (homologação simulada) > Run workflow**, digite `1.0.0` e rode.
9. Quando ficar verde, tire print.
10. Cole os prints em `docs/rollback.md`.
11. Corrija a porta de volta para 8000 por Pull Request e crie a tag `v1.1.1`.

## Problemas comuns

- **"denied" ao baixar a imagem no deploy**: confira o passo 3 da Parte 3.
- **CD falha no teste rápido logo na `v1.0.0`**: confira se o segredo `DB_PASSWORD` foi criado.
- **Compose reclama de variável**: o arquivo `.env` não existe ou está incompleto.
