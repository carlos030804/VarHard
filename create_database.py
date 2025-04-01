import pymysql
import sys
import os
from datetime import datetime

# Añade el directorio principal al path para las importaciones
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ahora las importaciones funcionarán correctamente
from app import create_app
from models.user import User
from models.evaluacion import Evaluation
from models.grade import Grade

app = create_app()

def setup_database():
    with app.app_context():
        # Crear tablas
        from app.extensions import db
        db.create_all()
        
        # Datos de prueba
        if not User.query.first():
            # Crear usuarios
            admin = User(username='admin', email='admin@sgea.edu', role='admin')
            admin.set_password('admin123')
            
            profesor = User(username='profesor1', email='profesor@sgea.edu', role='professor')
            profesor.set_password('profesor123')
            
            alumno = User(username='alumno1', email='alumno@sgea.edu', role='alumno')
            alumno.set_password('alumno123')
            
            db.session.add_all([admin, profesor, alumno])
            db.session.commit()
            
            # Crear evaluación
            evaluacion = Evaluation(
                name='Primer Parcial',
                eval_type='parcial',
                date=datetime(2023, 11, 20),
                teacher_id=profesor.id
            )
            db.session.add(evaluacion)
            db.session.commit()
            
            # Crear calificación
            calificacion = Grade(
                score=8.5,
                comments='Buen trabajo',
                student_id=alumno.id,
                evaluation_id=evaluacion.id
            )
            db.session.add(calificacion)
            db.session.commit()

if __name__ == '__main__':
    setup_database()
    print("✅ Base de datos y datos iniciales creados exitosamente!")