import constantes
import utils
from flask import render_template, request, redirect
from modelos import Plate
from app import app, db, session


# Rota para Adcionar Uma Lista de Pratos
@app.route(constantes.ID_ROUTE_PLATES, methods=["POST", "GET"])
def home():
    
    if utils.is_empty_session():
        return utils.render_login_page(constantes.MESSAGE_PLEASE_LOG_IN)

     # Obtendo o ID do restaurante do usuário.
    logged_user_restaurant_id = get_restaurant_id_from_logged_user()

    if request.method == 'POST':

        plate = Plate(name=request.form['name'].upper(),
                      category=request.form['category'],
                      price=float(request.form['price']),
                      restaurant_id = logged_user_restaurant_id)
        try:           
            utils.save_in_database(db, plate)
            return redirect(constantes.ID_ROUTE_PLATES)
        except:
            print(constantes.MESSAGE_ERROR_SAVING_PLATE)
            return redirect(constantes.ID_ROUTE_PLATES)
    else:
         # Traz todos os pratos do restaurante do usuário.
        plates = get_plates_of_logged_user_restaurant(logged_user_restaurant_id)
        return render_template(constantes.ID_PAGE_PLATES, plates=plates)


 # Rota para Editar um prato
@app.route("/plates/edit", methods=["POST"])
def edit_plate():

    plate_id    = request.form['plateId']
    newName     = request.form['editedName'].upper()
    newCategory = request.form['editedCategory']
    newPrice    = request.form['editedPrice']

    try:
        plateToBeEdited = Plate.query.filter(Plate.id == int(plate_id)).first()

        if plateToBeEdited:
            plateToBeEdited.name = str(newName)
            plateToBeEdited.category = str(newCategory)
            plateToBeEdited.price = float(newPrice)
            db.session.flush()
            db.session.commit()
            db.session.close()
    except:
        print('[edit_plate]' + constantes.MESSAGE_ERROR_EDITING_PLATE)

    return redirect(constantes.ID_ROUTE_PLATES)


# Rota para Deletar um Prato
@app.route("/plates/delete/<plate_id>", methods=["GET"])
def delete_plate(plate_id):    
    try:
        Plate.query.filter(Plate.id == int(plate_id)).delete()
        db.session.commit()
    except:
        print('[delete_plate] - ' + constantes.MESSAGE_ERROR_DELETING_PLATE)
    return redirect(constantes.ID_ROUTE_PLATES)


""" 
Retorna o ID do restaurante do usuário.
"""
def get_restaurant_id_from_logged_user():
    user = session.get(constantes.SESSION_ID)
    return user.restaurant_id


""" 
Retorna uma lista de pratos cadastrados para o restaurante do usuário.
"""
def get_plates_of_logged_user_restaurant(logged_user_restaurant_id):
    return Plate.query.filter(Plate.restaurant_id == logged_user_restaurant_id).all()