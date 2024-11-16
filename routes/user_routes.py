from flask import Blueprint,request,jsonify
from models.user_model import User
from config import db

user_bp=Blueprint('user_bp',__name__)

#GET - optener usuarios
@user_bp.route('/user',methods=['GET','POST'])
def get_user():
    users=users.query.all()
    return jsonify([user.to_dict() for user in users])