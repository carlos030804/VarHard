from app import db
from datetime import datetime

class Evaluation(db.Model):
    __tablename__ = 'evaluations'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    eval_type = db.Column(db.String(50))  # 'parcial', 'final', 'tarea', etc.
    date = db.Column(db.Date, default=datetime.utcnow)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relación
    grades = db.relationship('Grade', backref='evaluation', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Evaluation {self.name}>'