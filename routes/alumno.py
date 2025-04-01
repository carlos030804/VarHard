from flask import Blueprint, render_template
from flask_login import login_required

alumno_bp = Blueprint('alumno', __name__)

@alumno_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('vistaAlumno.html')

@alumno_bp.route('/calificaciones')
@login_required
def calificaciones():
    return render_template('calificacional.html')