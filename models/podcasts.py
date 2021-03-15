from sqlalchemy import CheckConstraint

from db import db


class Podcast(db.Model):
    __table_args__ = (
        CheckConstraint('duration > 0'),
        CheckConstraint('array_length(participants, 1) <= 10')
    )
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.ARRAY(db.String(100), dimensions=1),
                             nullable=True, default=list())
    upload_time = db.Column(db.DateTime, nullable=False, server_default='now()')
    last_modified_time = db.Column(db.DateTime, nullable=False,
                                   server_default='now()', onupdate='now()')

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "host": self.host,
            "participants": self.participants,
            "duration": self.duration,
            "upload_time": self.upload_time,
            "last_modified_time": self.last_modified_time
        }
