from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,jsonify
)
from werkzeug.exceptions import abort
from lienzo_perdido.db import get_db
from .auth import login_required
import psycopg2
import base64

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
            sucursal = 1#request.form['sucursal']

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
            nombre = request.form['Nombre']
            tipo = request.form['tipo']
            precio = request.form['precio']
            descripcio = request.form['descripcion']
            cultura = request.form['cultura']
            sucursal = 1#request.form['sucursal']

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
                    'UPDATE menu SET nombre = %s, tipo = %s, precio = %s, '
                    'descripcion = %s, cultura = %s, '
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
            descripcio = ''
            nombre = request.form['nombre']
            fecha = request.form['fecha']
            imagen = request.files['imagen']
            sucursal = '1'#request.form['sucursal']

            if not descripcio:
                error = "La descripcion es requerida"
            if not nombre:
                error = "El nombre es requerido"
            if not fecha:
                error = "La fecha es requerida"
            if not imagen:
                error = "La imagen es requerida"
            else:
                imagen_bytes = imagen.read()
            if not sucursal:
                error = "La sucursal es requerida"
           
            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'INSERT INTO public.evento (descripcion,nombre,fecha,imagen,"tierraYSazon_idSucursal") values'
                    '(%s,%s,%s,%s,%s)',
                    (descripcio,nombre,fecha,psycopg2.Binary(imagen_bytes),sucursal)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboardEventos'))
        elif accion == 'modificar':
            id = request.form['id']
            descripcio = ''
            nombre = request.form['nombre']
            fecha = request.form['fecha']
            imagen = request.files['imagen']
            sucursal = '1'#request.form['sucursal']

            if not id:
                error = "El ID es requerido"
            if not descripcio:
                error = "La descripcion es requerida"
            if not nombre:
                error = "El nombre es requerido"
            if not fecha:
                error = "La fecha es requerida"
            if not imagen:
                error = "La imagen es requerida"
            else:
                imagen_bytes = imagen.read()
            if not sucursal:
                error = "La sucursal es requerida"
            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'UPDATE public.evento SET descripcion = %s, nombre = %s, fecha = %s'
                    ', imagen = %s, "tierraYSazon_idSucursal" = %s'
                    'WHERE "idEvento" = %s',
                    (descripcio,nombre,fecha,psycopg2.Binary(imagen_bytes),sucursal,id)
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
            nombre = request.form['nombre']
            fecha = request.form['fecha']
            imagen = request.files['imagen']
            sucursal = 1#request.form['sucursal']

            if not descripcio:
                error = "La descripcion es requerida"
            if not nombre:
                error = "El nombre es requerido"
            if not fecha:
                error = "La fecha es requerida"
            if not imagen:
                error = "La imagen es requerida"
            else:
                imagen_bytes = imagen.read()
            if not sucursal:
                error = "La sucursal es requerida"

            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'INSERT INTO public."exposicionCultural"'
                    ' (descripcion,nombre,fecha,imagen,"tierraYSazon_idSucursal") values'
                    ' (%s,%s,%s,%s,%s)',
                    (descripcio,nombre,fecha,psycopg2.Binary(imagen_bytes),sucursal)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboardExposiciones'))
        elif accion == 'modificar':
            id = request.form['id']
            descripcio = request.form['descripcion']
            nombre = request.form['nombre']
            fecha = request.form['fecha']
            imagen = request.form['imagen']
            sucursal = 1#request.form['sucursal']

            if not id:
                error = "El ID es requerido"
            if not descripcio:
                error = "La descripcion es requerida"
            if not nombre:
                error = "El nombre es requerido"
            if not fecha:
                error = "La fecha es requerida"
            if not imagen:
                error = "La imagen es requerida"
            else:
                imagen_bytes = imagen.read()
            if not sucursal:
                error = "La sucursal es requerida"

            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'UPDATE public."exposicionCultural" SET descripcion = %s, nombre = %s, fecha = %s'
                    ', imagen = %s, "tierraYSazon_idSucursal" = %s'
                    'WHERE "idExposicionCultural" = %s',
                    (descripcio,nombre, fecha,psycopg2.Binary(imagen_bytes),sucursal,id)
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
                    'DELETE FROM public."exposicionCultural"' 
                    ' WHERE "idExposicionCultural" = %s',
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
            username = request.form['username']
            password = request.form['password']
            id = int(request.form['id'])

            if not username:
                error = "el Usuarios es requerido"
            if not password:
                error = "La contraseña es requerida"
            if not id:
                error = "el ID es requerido"
            
            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'INSERT INTO public.usuario'
                    ' values (%s,%s,%s)',
                    (id,username,password)
                )
                db.commit()
                return redirect(url_for('lienzo.dashboardUsuarios'))
        elif accion == 'modificar':
            username = request.form['username']
            password = request.form['password']
            id = request.form['id']

            if not username:
                error = "el Usuarios es requerido"
            if not password:
                error = "La contraseña es requerida"
            if not id:
                error = "el ID es requerido"
            
            if error is not None:
                flash(error)
            else:
                db, c = get_db()
                c.execute(
                    'update public.usuario'
                    ' SET nombre = %s, contra = %s'
                    'WHERE id = %s',
                    (username,password,id)
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
                    'DELETE FROM public.usuario WHERE id = %s',
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

@bp.route('/api/menu/platillo', methods=['GET'])
def platillo_api():
    db, c = get_db()
    query = 'SELECT * FROM  menu WHERE tipo = \'Platillo\''
    c.execute(query)
    menus = c.fetchall()
    return jsonify(menus)

@bp.route('/api/menu/bebida', methods=['GET'])
def bebida_api():
    db, c = get_db()
    query = 'SELECT * FROM  menu WHERE tipo = \'Bebida\''
    c.execute(query)
    menus = c.fetchall()
    return jsonify(menus)

@bp.route('/api/menu/entrada', methods=['GET'])
def entrada_api():
    db, c = get_db()
    query = 'SELECT * FROM  menu WHERE tipo = \'Entrada\''
    c.execute(query)
    menus = c.fetchall()
    return jsonify(menus)

@bp.route('/api/menu/postre', methods=['GET'])
def postre_api():
    db, c = get_db()
    query = 'SELECT * FROM  menu WHERE tipo = \'Postre\''
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
    eventos_con_imagenes = []
    for evento in eventos:
        if 'imagen' in evento and evento['imagen'] is not None:
            # Acceder a la clave "imagen" de cada evento y convertir los bytes a base64
            imagen_bytes = base64.b64encode(evento['imagen']).decode('utf-8')
            # Crear una copia del diccionario actual y actualizar la clave "imagen"
            evento_con_imagen = dict(evento)
            evento_con_imagen['imagen'] = imagen_bytes
            # Agregar el diccionario actualizado a la lista final
            eventos_con_imagenes.append(evento_con_imagen)
        else:
            evento_con_imagen = dict(evento)
            # Agregar el diccionario actualizado a la lista final
            eventos_con_imagenes.append(evento_con_imagen)
    return jsonify(eventos_con_imagenes)

#API EXPOSICIONES -----------------------------------------------------------
@bp.route('/api/exposiciones', methods=['GET'])
def exposiciones_api():
    db, c = get_db()
    query = 'SELECT * FROM  public."exposicionCultural"'
    c.execute(query)
    exposiciones = c.fetchall()
    exposiciones_con_imagenes = []
    for exposicion in exposiciones:
        if 'imagen' in exposicion and exposicion['imagen'] is not None:
            # Acceder a la clave "imagen" de cada evento y convertir los bytes a base64
            imagen_bytes = base64.b64encode(exposicion['imagen']).decode('utf-8')
            # Crear una copia del diccionario actual y actualizar la clave "imagen"
            exposicion_con_imagen = dict(exposicion)
            exposicion_con_imagen['imagen'] = imagen_bytes
            # Agregar el diccionario actualizado a la lista final
            exposiciones_con_imagenes.append(exposicion_con_imagen)
        else:
            exposicion_con_imagen = dict(exposicion)
            # Agregar el diccionario actualizado a la lista final
            exposiciones_con_imagenes.append(exposicion_con_imagen)
    return jsonify(exposiciones_con_imagenes)

@bp.route('/api/usuarios', methods=['GET'])
def usuarios_api():
    db, c = get_db()
    query = 'SELECT * FROM  public.usuario'
    c.execute(query)
    usuarios = c.fetchall()
    return jsonify(usuarios)