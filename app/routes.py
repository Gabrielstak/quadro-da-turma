import os

from flask import Blueprint, jsonify, render_template, request

from .models import Tarefa, db

bp = Blueprint("main", __name__)


def _versao():
    return os.getenv("APP_VERSION", "dev")


@bp.get("/")
def index():
    return render_template("index.html", versao=_versao())


@bp.get("/health")
def health():
    return jsonify(status="ok")


@bp.get("/version")
def version():
    return jsonify(versao=_versao())


@bp.get("/api/tarefas")
def listar():
    tarefas = Tarefa.query.order_by(Tarefa.id).all()
    return jsonify([t.to_dict() for t in tarefas])


@bp.post("/api/tarefas")
def criar():
    dados = request.get_json(silent=True) or {}
    titulo = (dados.get("titulo") or "").strip()
    if not titulo:
        return jsonify(erro="Informe o título da tarefa."), 400
    if len(titulo) > 120:
        return jsonify(erro="O título pode ter no máximo 120 caracteres."), 400
    tarefa = Tarefa(titulo=titulo)
    db.session.add(tarefa)
    db.session.commit()
    return jsonify(tarefa.to_dict()), 201


@bp.put("/api/tarefas/<int:tarefa_id>")
def atualizar(tarefa_id):
    tarefa = db.session.get(Tarefa, tarefa_id)
    if tarefa is None:
        return jsonify(erro="Tarefa não encontrada."), 404
    dados = request.get_json(silent=True) or {}
    if "concluida" in dados:
        tarefa.concluida = bool(dados["concluida"])
    db.session.commit()
    return jsonify(tarefa.to_dict())


@bp.delete("/api/tarefas/<int:tarefa_id>")
def apagar(tarefa_id):
    tarefa = db.session.get(Tarefa, tarefa_id)
    if tarefa is None:
        return jsonify(erro="Tarefa não encontrada."), 404
    db.session.delete(tarefa)
    db.session.commit()
    return "", 204
