import constantes
import utils
from flask import render_template, request
from modelos import Plate
from app import app


# Rota Pesquisa de Pratos
@app.route(constantes.ID_ROUTE_SEARCH, methods=["POST", "GET"])
def search():
    if utils.is_empty_session():
        return utils.render_login_page(constantes.MESSAGE_PLEASE_LOG_IN)
    
    plates = None
    message = None

    if request.method == 'POST':

        plate_id = request.form.get('plate_id')
        plate_name = request.form.get('plate_name')
        
        if plate_id:
            plates = Plate.query.filter(Plate.id == plate_id).all()

        if plate_name:
            plates = Plate.query\
                .filter(Plate.name == plate_name.upper())\
                .order_by(Plate.restaurant_id).all()
        
        if not plates:
            message = constantes.MESSAGE_NOTHING_FOUND
    else:
        plates = Plate.query.order_by(Plate.id).all()

    return render_template(constantes.ID_PAGE_SEARCH, plates=plates, message=message)