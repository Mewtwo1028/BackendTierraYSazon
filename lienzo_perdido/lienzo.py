from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,jsonify
)
from werkzeug.exceptions import abort
from lienzo_perdido.db import get_db
from .auth import login_required

bp = Blueprint('lienzo',__name__)

#PANTILLAS GENERALES ---------------------------------------------
@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/eventosMusicales')
def eventosMusicales():
    return render_template('eventosMusicales.html') 

@bp.route('/exposicionesCulturales')
def exposicionesCulturales():
    return render_template('exposicionesCulturales.html') 

@bp.route('/menu')
def menu():
    return render_template('menu.html') 

@bp.route('/Principal')
def Principal():
    return render_template('Principal.html') 

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
            nombre = request.form['Nombre']
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
            if not sucursal:
                error = "La sucursal es requerida"

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
            id = request.form['id']
            nombre = request.form['nombre']
            tipo = request.form['tipo']
            precio = request.form['precio']
            descripcio = request.form['descripcion']
            cultura = request.form['cultura']
            sucursal = request.form['sucursal']

            if not id:
                error = "El ID es requerido"
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
                    'UPDATE menu SET nombre = %s, tipo = %s, precio = %s'
                    'descripcion = %s, cultura = %s,'
                    '"tierraYSazon_idSucursal" = %s WHERE "idMenu" = %s',
                    (nombre,tipo,precio,descripcio,cultura,sucursal,id)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboard'))
        elif accion == 'eliminar':
            id = request.form['id']

            if not id:
                error = 'El ID es requerido'
            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'DELETE FROM public.menu WHERE "idMenu" = %s',
                    (id,)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboard'))
            

    return render_template('dashboard.html')


#eventos admin ------------------------------------------------------------
@bp.route('/admin/eventos/dashboard', methods=['GET','POST'])
@login_required
def dashboardEventos():
    if request.method == 'POST':
        accion = request.form.get('accion')
        error = None
        
        if accion == 'insertar':
            descripcio = request.form['descripcion']
            fecha = request.form['fecha']
            imagen = request.form['imagen']
            sucursal = request.form['sucursal']

            if not descripcio:
                error = "La descripcion es requerida"
            if not fecha:
                error = "La fecha es requerida"
            if not imagen:
                error = "La imagen es requerida"
            if not sucursal:
                error = "La sucursal es requerida"

            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'INSERT INTO public.evento (descripcion,fecha,imagen,"tierraYSazon_idSucursal") values'
                    '(%s,%s,%s,%s)',
                    (descripcio,fecha,imagen,sucursal)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboardEventos'))
        elif accion == 'modificar':
            id = request.form['id']
            descripcio = request.form['descripcion']
            fecha = request.form['fecha']
            imagen = request.form['imagen']
            sucursal = request.form['sucursal']

            if not id:
                error = "El ID es requerido"
            if not descripcio:
                error = "La descripcion es requerida"
            if not fecha:
                error = "La fecha es requerida"
            if not imagen:
                error = "La imagen es requerida"
            if not sucursal:
                error = "La sucursal es requerida"

            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'UPDATE public.evento SET descripcion = %s, fecha = %s'
                    ', imagen = %s, "tierraYSazon_idSucursal" = %s'
                    'WHERE "idEvento" = %s',
                    (descripcio,fecha,imagen,sucursal,id)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboardEventos'))
        elif accion == 'eliminar':
            id = request.form['id']

            if not id:
                error = 'El ID es requerido'
            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'DELETE FROM public.evento WHERE "idEvento" = %s',
                    (id,)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboardEventos'))
            
    return render_template('dashboardEventos.html')

#exposicion admin ----------------------------------------------------------
@bp.route('/admin/exposiciones/dashboard', methods=['GET','POST'])
@login_required
def dashboardExposiciones():
    if request.method == 'POST':
        accion = request.form.get('accion')
        error = None
        
        if accion == 'insertar':
            descripcio = request.form['descripcion']
            fecha = request.form['fecha']
            imagen = request.form['imagen']
            sucursal = request.form['sucursal']

            if not descripcio:
                error = "La descripcion es requerida"
            if not fecha:
                error = "La fecha es requerida"
            if not imagen:
                error = "La imagen es requerida"
            if not sucursal:
                error = "La sucursal es requerida"

            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'INSERT INTO public."exposicionCultural"'
                    ' (descripcion,fecha,imagen,"tierraYSazon_idSucursal") values'
                    ' (%s,%s,%s,%s)',
                    (descripcio,fecha,imagen,sucursal)
                )
                db.commit()
                return redirect(url_for('dashboardExposiciones'))
        elif accion == 'modificar':
            id = request.form['id']
            descripcio = request.form['descripcion']
            fecha = request.form['fecha']
            imagen = request.form['imagen']
            sucursal = request.form['sucursal']

            if not id:
                error = "El ID es requerido"
            if not descripcio:
                error = "La descripcion es requerida"
            if not fecha:
                error = "La fecha es requerida"
            if not imagen:
                error = "La imagen es requerida"
            if not sucursal:
                error = "La sucursal es requerida"

            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'UPDATE public."exposicionCultural" SET descripcion = %s, fecha = %s'
                    ', imagen = %s, "tierraYSazon_idSucursal" = %s'
                    'WHERE "idExposicionCultural" = %s',
                    (descripcio,fecha,imagen,sucursal,id)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboardExposiciones'))
        elif accion == 'eliminar':
            id = request.form['id']

            if not id:
                error = 'El ID es requerido'
            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'DELETE FROM public.evento WHERE "idExposicionCultural" = %s',
                    (id,)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboardExposiciones'))
    return render_template('dashboardExposiciones.html')

@bp.route('/admin/usuarios/dashboard', methods=['GET','POST'])
@login_required
def dashboardUsuarios():
    if request.method == 'POST':
        accion = request.form.get('accion')
        error = None
        
        if accion == 'insertar':
            descripcio = request.form['descripcion']
            fecha = request.form['fecha']
            imagen = request.form['imagen']
            sucursal = request.form['sucursal']

            if not descripcio:
                error = "La descripcion es requerida"
            if not fecha:
                error = "La fecha es requerida"
            if not imagen:
                error = "La imagen es requerida"
            if not sucursal:
                error = "La sucursal es requerida"

            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'INSERT INTO public."exposicionCultural"'
                    ' (descripcion,fecha,imagen,"tierraYSazon_idSucursal") values'
                    ' (%s,%s,%s,%s)',
                    (descripcio,fecha,imagen,sucursal)
                )
                db.commit()
                return redirect(url_for('dashboardUsuarios'))
        elif accion == 'modificar':
            id = request.form['id']
            descripcio = request.form['descripcion']
            fecha = request.form['fecha']
            imagen = request.form['imagen']
            sucursal = request.form['sucursal']

            if not id:
                error = "El ID es requerido"
            if not descripcio:
                error = "La descripcion es requerida"
            if not fecha:
                error = "La fecha es requerida"
            if not imagen:
                error = "La imagen es requerida"
            if not sucursal:
                error = "La sucursal es requerida"

            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'UPDATE public."exposicionCultural" SET descripcion = %s, fecha = %s'
                    ', imagen = %s, "tierraYSazon_idSucursal" = %s'
                    'WHERE "idExposicionCultural" = %s',
                    (descripcio,fecha,imagen,sucursal,id)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboardUsuarios'))
        elif accion == 'eliminar':
            id = request.form['id']

            if not id:
                error = 'El ID es requerido'
            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'DELETE FROM public.evento WHERE "idExposicionCultural" = %s',
                    (id,)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboardUsuarios'))
    return render_template('dashboardUsuarios.html')


#API MENU -----------------------------------------------------------------
@bp.route('/api/menu', methods=['GET'])
def menu_api():
    db, c = get_db()
    query = 'SELECT * FROM  menu'
    c.execute(query)
    menus = c.fetchall()
    return jsonify(menus)

#API EVENTOS ------------------------------------------------------------------
@bp.route('/api/eventos', methods=['GET'])
def eventos_api():
    db, c = get_db()
    query = 'SELECT * FROM  evento'
    c.execute(query)
    eventos = c.fetchall()
    return jsonify(eventos)

#API EXPOSICIONES -----------------------------------------------------------
@bp.route('/api/exposiciones', methods=['GET'])
def exposiciones_api():
    db, c = get_db()
    query = 'SELECT * FROM  public."exposicionCultural"'
    c.execute(query)
    exposiciones = c.fetchall()
    return jsonify(exposiciones)

@bp.route('/api/usuarios', methods=['GET'])
def usuarios_api():
    db, c = get_db()
    query = 'SELECT * FROM  public.usuario'
    c.execute(query)
    usuarios = c.fetchall()
    return jsonify(usuarios)