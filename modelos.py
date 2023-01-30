from app import db
from datetime import datetime
import constantes

from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash



# Classe Modelo Para o Restaurante
class Restaurante(db.Model):
    __tablename__ = constantes.RESTAURANTS_TABLE_NAME

    id     = db.Column(db.Integer, primary_key = True)
    nome   = db.Column(db.String(90), nullable = False)
    pratos = db.relationship('Prato', backref='restaurantes', lazy="joined")
    usuarios  = db.relationship('Usuario',  backref='restaurantes', lazy="joined")
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'Restaurante [#{self.id}, nome: {self.name}, created_on: {self.created_on}]'


# Classe Modelo para o Prato
class Prato(db.Model):
    __tablename__ = constantes.PLATES_TABLE_NAME

    id         = db.Column(db.Integer, primary_key = True)
    nome       = db.Column(db.String(90), nullable = False)
    categoria   = db.Column(db.String(100), nullable = False)
    preco      = db.Column(db.String(10), nullable = False)    
    restaurante_id = db.Column(db.Integer, db.ForeignKey("restaurantes.id"))
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'Prato [#{self.id}, nome: {self.name}, categoria: {self.category}, preco: {self.price}, created_on: {self.created_on}]'


# Classe Modelo para o  Usuario
class Usuario(db.Model):
    __tablename__ = constantes.USERS_TABLE_NAME

    id         = db.Column(db.Integer, primary_key = True)
    nome       = db.Column(db.String(90), nullable = False)
    email      = db.Column(db.String(100), nullable = False)
    password_hash = db.Column(db.String(128), nullable = False)
    restaurante_id = db.Column(db.Integer, db.ForeignKey("restaurantes.id"), nullable = False)  
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    def check_email(self, email):
        return email == self.email

    def set_password(self, plainTextPassword):
        self.password_hash = generate_password_hash(plainTextPassword)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def check_restaurant_id(self, restaurant_id):
        return int(restaurant_id) == self.restaurant_id

    def __repr__(self):
        return f'Usuario [#{self.id}, nome: {self.name}, restaurante_id: {self.restaurant_id}, email: {self.email}, created_on: {self.created_on}]'
