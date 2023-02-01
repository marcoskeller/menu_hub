import constants
import utils
from flask import request, redirect
from models import User
from app import app, session


# Rota Login
@app.route(constants.ID_ROUTE_LOGIN, methods=["POST", "GET"])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        restaurant_id = request.form['restaurant_id']

        user = User.query.filter_by(email=email).first()

        if user:

            if user.check_password(password) and user.check_restaurant_id(restaurant_id):

                session[constants.SESSION_ID] = user

                return redirect(constants.ID_ROUTE_PLATES)

            else:
                return utils.render_login_page(constants.MESSAGE_ERROR_INVALID_CREDENTIALS) 
        else:
            return utils.render_login_page(constants.MESSAGE_ERROR_INVALID_CREDENTIALS) 
    else:
        return utils.render_login_page(None)



# Rota Logout
@app.route(constants.ID_ROUTE_LOGOUT, methods=["POST", "GET"])
def logout():

    message = None

    if not utils.is_empty_session():
        session[constants.SESSION_ID] = None
        message = constants.MESSAGE_LOG_OUT
    return utils.render_login_page(message)