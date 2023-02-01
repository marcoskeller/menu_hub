import constantes
import utils
from flask import render_template, request, redirect
from modelos import Restaurant
from app import app, db


# Rota para Adicionar Restaurante
@app.route(constantes.ID_ROUTE_RESTAURANT, methods=["POST", "GET"])
def add_restaurant():

    if request.method == 'POST':

        restaurant = Restaurant(name=request.form['name'].upper())

        try:           
            utils.save_in_database(db, restaurant)      
            return redirect(constantes.ID_ROUTE_RESTAURANT)
        except:
            print(constantes.MESSAGE_ERROR_SAVING_RESTAURANT)
            return redirect(constantes.ID_ROUTE_RESTAURANT)
    else:
        # Lista todos os restaurantes no banco de dados.
        restaurants = Restaurant.query.order_by(Restaurant.id).all()
        return render_template(constantes.ID_PAGE_RESTAURANT, restaurants=restaurants)