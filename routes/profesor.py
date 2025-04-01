from flask import Blueprint, render_template
from flask_login import login_required

professor_bp = Blueprint('professor', __name__)

@professor_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('vistaProfessor.html')

@professor_bp.route('/evaluaciones')
@login_required
def evaluaciones():
    return render_template('evaluaciones.html')

@professor_bp.route('/calificaciones')
@login_required
def calificaciones():
    return render_template('calificaciones.html')