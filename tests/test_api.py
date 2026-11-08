import pytest

from app import create_app


@pytest.fixture()
def client():
    app = create_app(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"}
    )
    return app.test_client()


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_version_usa_variavel_de_ambiente(client, monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.2.3")
    assert client.get("/version").get_json() == {"versao": "1.2.3"}


def test_pagina_inicial(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Quadro da Turma" in resp.get_data(as_text=True)


def test_lista_comeca_vazia(client):
    assert client.get("/api/tarefas").get_json() == []


def test_criar_tarefa(client):
    resp = client.post("/api/tarefas", json={"titulo": "Montar o pipeline"})
    assert resp.status_code == 201
    corpo = resp.get_json()
    assert corpo["titulo"] == "Montar o pipeline"
    assert corpo["concluida"] is False
    assert len(client.get("/api/tarefas").get_json()) == 1


@pytest.mark.parametrize("titulo", ["", "   ", None])
def test_criar_tarefa_sem_titulo(client, titulo):
    resp = client.post("/api/tarefas", json={"titulo": titulo})
    assert resp.status_code == 400


def test_criar_tarefa_titulo_longo(client):
    resp = client.post("/api/tarefas", json={"titulo": "x" * 121})
    assert resp.status_code == 400


def test_marcar_como_concluida(client):
    tarefa = client.post("/api/tarefas", json={"titulo": "Testar"}).get_json()
    resp = client.put(f"/api/tarefas/{tarefa['id']}", json={"concluida": True})
    assert resp.status_code == 200
    assert resp.get_json()["concluida"] is True


def test_apagar_tarefa(client):
    tarefa = client.post("/api/tarefas", json={"titulo": "Apagar"}).get_json()
    assert client.delete(f"/api/tarefas/{tarefa['id']}").status_code == 204
    assert client.get("/api/tarefas").get_json() == []


def test_tarefa_inexistente(client):
    assert client.put("/api/tarefas/999", json={"concluida": True}).status_code == 404
    assert client.delete("/api/tarefas/999").status_code == 404
