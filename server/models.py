from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
from typing import Optional


class Earthquake(db.Model, SerializerMixin):
    __table_name__ = "earthquakes"
    id: int = db.Column(db.Integer, primary_key=True)
    magnitude: float = db.Column(db.Float, nullable=False)
    location: str = db.Column(db.String, nullable=False)
    year: int = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
