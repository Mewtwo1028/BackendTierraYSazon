from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,jsonify
)
from werkzeug.exceptions import abort
from lienzo_perdido.db import get_db
from .auth import login_required

bp = Blueprint('lienzo',__name__)

@bp.route('/')
def index():
    return render_template('index.html') 


#menu admin ---------------------------------------------------------------
@bp.route('/admin/menu/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        accion = request.form.get('accion')
        error = None
        
        if accion == 'insertar':
            nombre = request.form['nombre']
            tipo = request.form['tipo']
            precio = request.form['precio']
            descripcio = request.form['descripcion']
            cultura = request.form['cultura']
            sucursal = request.form['sucursal']

            if not nombre:
                error = "El nombre es requerido"
            if not tipo:
                error = "El tipo es requerido"
            if not precio:
                error = "El precio es requerido"
            if not descripcio:
                error = "La descripcion es requerida"
            if not cultura:
                error = "La cultura es requerida"

            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'INSERT INTO menu (nombre,tipo,precio,descripcion,cultura,"tierraYSazon_idSucursal") values'
                    '(%s,%s,%s,%s,%s,%s)',
                    (nombre,tipo,precio,descripcio,cultura,sucursal)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboard'))
        elif accion == 'modificar':
            pass
        elif accion == 'eliminar':
            id = request.form['id']

            if not id:
                error = 'El ID es requerido'
            if error is not None:
                flash(error)
            else:
                print(id)
            

    return render_template('dashboard.html')


#eventos admin ------------------------------------------------------------
@bp.route('/admin/eventos/dashboard', methods=['GET','POST'])
@login_required
def dashboardEventos():
    return render_template('dashboardEventos.html')

#exposicion admin ----------------------------------------------------------
@bp.route('/admin/eventos/dashboard', methods=['GET','POST'])
@login_required
def dashboardExposiciones():
    return render_template('dashboardExposiciones.html')

#API MENU -----------------------------------------------------------------
@bp.route('/api/menu', methods=['GET'])
def menu():
    db, c = get_db()
    query = 'SELECT * FROM  menu'
    c.execute(query)
    menus = c.fetchall()
    return jsonify(menus)

#API EVENTOS ------------------------------------------------------------------
@bp.route('/api/eventos', methods=['GET'])
def eventos():
    db, c = get_db()
    query = 'SELECT * FROM  evento'
    c.execute(query)
    eventos = c.fetchall()
    return jsonify(eventos)

#API EXPOSICIONES -----------------------------------------------------------
@bp.route('/api/exposiciones', methods=['GET'])
def exposiciones():
    db, c = get_db()
    query = 'SELECT * FROM  public."exposicionCultural"'
    c.execute(query)
    exposiciones = c.fetchall()
    return jsonify(exposiciones)