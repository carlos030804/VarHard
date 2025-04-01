from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import pymysql

# Configuración específica para MySQL
pymysql.install_as_MySQLdb()

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Registrar blueprints
    from routes.auth import auth_bp
    from routes.profesor import professor_bp
    from routes.alumno import alumno_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(professor_bp, url_prefix='/professor')
    app.register_blueprint(alumno_bp, url_prefix='/alumno')
    
    # Crear base de datos y tablas si no existen
    with app.app_context():
        create_database()
        db.create_all()
        create_initial_data()
    
    return app

def create_database():
    """Crea la base de datos si no existe"""
    import pymysql
    from config import Config
    
    # Conexión sin especificar base de datos
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=''
    )
    
    try:
        with connection.cursor() as cursor:
            # Crear base de datos si no existe
            cursor.execute("CREATE DATABASE IF NOT EXISTS sgea_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    finally:
        connection.close()

def create_initial_data():
    """Crea datos iniciales para pruebas"""
    from models.user import User
    
    # Verificar si ya existe el usuario admin
    if not User.query.filter_by(username='admin').first():
        admin = User(
            username='admin',
            email='admin@sgea.edu',
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()