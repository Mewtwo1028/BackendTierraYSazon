import psycopg2
from psycopg2.extras import RealDictCursor
import click
from flask import current_app,g
from flask.cli import with_appcontext
from .schema import querys

def get_db():
    if 'db' not in g:
        g.db =  psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Codeboy1028',
            database='LIENZO_PERDIDO'
        )
        g.c = g.db.cursor(cursor_factory=RealDictCursor)
    return g.db, g.c

def close_db(e=None):
    db = g.pop('db',None)
    if db is not None:
        db.close()

def init_db():
    db, c = get_db()
    for i in querys:
        c.execute(i)
        db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('base de datos iniciada')

def init_app(app):
    app.teardown_appcontext(close_db)       
    app.cli.add_command(init_db_command)