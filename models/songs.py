from sqlalchemy import CheckConstraint

from db import db


class Song(db.Model):
    __table_args__ = (
        CheckConstraint('duration > 0'),
    )
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False, server_default='now()')
    last_modified_time = db.Column(db.DateTime, nullable=False,
                                   server_default='now()', onupdate='now()')

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "duration": self.duration,
            "upload_time": self.upload_time,
            "last_modified_time": self.last_modified_time
        }
