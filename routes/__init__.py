from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Configuración básica
    app.config['SECRET_KEY'] = 'tu-clave-secreta-aqui'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sgea.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Registrar blueprints
    from routes import auth, professor, alumno
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(professor.professor_bp, url_prefix='/professor')
    app.register_blueprint(alumno.alumno_bp, url_prefix='/alumno')
    
    # Crear tablas de la base de datos
    with app.app_context():
        db.create_all()
        
        # Crear usuario admin por defecto si no existe
        from models.user import User
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', email='admin@sgea.edu', role='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
    
    return app