from datetime import datetime, timezone

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    concluida = db.Column(db.Boolean, default=False, nullable=False)
    criada_em = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "concluida": self.concluida,
            "criada_em": self.criada_em.isoformat(),
        }
