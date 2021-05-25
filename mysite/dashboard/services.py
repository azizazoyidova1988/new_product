from django.db import connection
from contextlib import closing


def get_homes():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from dashboard_home""")
        homes = dict_fetchall(cursor)
        return homes


def get_homes_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from dashboard_home""")
        homes = dict_fetchall(cursor)
        return homes


def get_client():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from dashboard_client""")
        clients = dict_fetchall(cursor)
        return clients


def get_client_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(full_name) from dashboard_client""")
        clients = dict_fetchall(cursor)
        return clients


def get_product():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from dashboard_products""")
        products = dict_fetchall(cursor)
        return products


def get_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(id) from dashboard_products""")
        products = dict_fetchall(cursor)
        return products


def get_references():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from dashboard_reference""")
        references = dict_fetchall(cursor)
        return references


def get_references_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from dashboard_reference""")
        references = dict_fetchall(cursor)
        return references


def get_recipes():
    with closing(connection.cursor())as cursor:
        cursor.execute("""select * from dashboard_recipes""")
        recipes = dict_fetchall(cursor)
        return recipes


def get_recipes_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(title) from dashboard_recipes""")
        recipes = dict_fetchall(cursor)
        return recipes

def get_register():
    with closing(connection.cursor())as cursor:
        cursor.execute("""select * from dashboard_register""")
        register = dict_fetchall(cursor)
        return register


def get_register_count():
    with closing(connection.cursor()) as cursor:
        cursor.exegute("""select count(name) from dashboard_register""")
        register = dict_fetchall(cursor)
        return register



def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
