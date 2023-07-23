import functools

from flask import (
    Blueprint,flash,g,render_template,request,url_for,session, redirect
)
from werkzeug.security import check_password_hash, generate_password_hash
from lienzo_perdido.db import get_db

bp = Blueprint('auth',__name__, url_prefix='/auth')


@bp.route('/register', methods=['GET','POST'])
def register():
    return render_template('auth/register.html')

@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            'SELECT * FROM public.usuario WHERE "nombre" = %s',
            (username,)
        )
        user = c.fetchone()
        if user is None:
            
            error = 'user and/or password incorret'
        elif not user['contra'].strip() == password:
            error = 'user and/or password incorret'
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('lienzo.dashboard'))

        flash(error)
    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute(
            'SELECT * FROM usuario WHERE id = %s',
            (user_id,)
        )
        g.user = c.fetchone()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@bp.route('logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login')) 