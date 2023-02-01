import constantes
import utils
from flask import request, redirect
from modelos import User
from app import app, session


# Rota Login
@app.route(constantes.ID_ROUTE_LOGIN, methods=["POST", "GET"])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        restaurant_id = request.form['restaurant_id']

        user = User.query.filter_by(email=email).first()

        if user:

            if user.check_password(password) and user.check_restaurant_id(restaurant_id):

                session[constantes.SESSION_ID] = user

                return redirect(constantes.ID_ROUTE_PLATES)

            else:
                return utils.render_login_page(constantes.MESSAGE_ERROR_INVALID_CREDENTIALS) 
        else:
            return utils.render_login_page(constantes.MESSAGE_ERROR_INVALID_CREDENTIALS) 
    else:
        return utils.render_login_page(None)



# Rota Logout
@app.route(constantes.ID_ROUTE_LOGOUT, methods=["POST", "GET"])
def logout():

    message = None

    if not utils.is_empty_session():
        session[constantes.SESSION_ID] = None
        message = constantes.MESSAGE_LOG_OUT
    return utils.render_login_page(message)