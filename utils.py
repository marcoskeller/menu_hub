import constantes
from app import session
from flask import render_template
from modelos import Restaurant


def is_empty_session():
    return constantes.SESSION_ID not in session or session[constantes.SESSION_ID] == None


def render_login_page(message):
    #List de todos os  restaurantes.
    restaurants = Restaurant.query.all()
    return render_template(constantes.ID_PAGE_LOGIN, list_of_restaurants=restaurants, message=message)


def save_in_database(database, model_object):
    database.session.add(model_object)
    database.session.commit()