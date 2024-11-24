
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Patient(name='{self.name}', description='{self.description}', weight='{self.weight}', quantity='{self.quantity}', price='{self.price}')"