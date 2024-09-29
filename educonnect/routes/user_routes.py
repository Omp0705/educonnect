from flask import request,jsonify,Blueprint,current_app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime as dt
from functools import wraps
import logging

user_bp = Blueprint('user',__name__)
SECRET_KEY = ""
def get_db():
    from app import mongo
    return mongo.db

@user_bp.route('/register', methods=['POST'])
def register():
    users = get_db().users
    data = request.get_json()
    
    if users.find_one({"email": data['email']}):
        return jsonify({"error": "User already exists"}), 400
    
    hashed_password = generate_password_hash(data['password'])
    user = {
        "name": data['name'],
        "username":data['username'],
        "email": data['email'],
        "password": hashed_password,
        "domain": data['domain'],
        "profile_image": data['url'],
        "education": data['education'],
        "skills": data['skills'],
        "interests": data['interests'],
        "created_at": dt.datetime.utcnow(),
        "updated_at": dt.datetime.utcnow()
        }
    users.insert_one(user)
    return jsonify({"message": "User registered successfully"}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    users = get_db().users
    data = request.get_json()
    user = users.find_one({"email": data['email']})
    if user and check_password_hash(user['password'], data['password']):
        access_token = create_access_token(identity=user['email'])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error":"Invalid email or passowrd"}),401
    

@user_bp.route('/profile', methods=['GET'])
@jwt_required()  
def get_profile():
    # Get the identity (username) from the JWT
    current_user = get_jwt_identity()
    
    # Fetch user details from the database
    users = get_db().users
    user = users.find_one({"email": current_user}, {"_id": 0, "password": 0})
    
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route("/update",methods=['POST'])
@jwt_required()
def update_profile():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    data['password'] = hashed_password
    current_user = get_jwt_identity()
    # {name,username,password,profile_pic,education}
    users =get_db().users
    # user = users.find_one({"username":current_user},{"_id":0,"password":0})
    # Update the user with the provided data
    update_result = users.update_one(
        {"email": current_user}, 
        {"$set": data}  # Using $set to update fields
    )

    if update_result.modified_count == 1:
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'message': 'User not found or not updated'}), 404


@user_bp.route("/addSkills",methods = ["POST"])
@jwt_required()
def add_skills():
    data = request.get_json()
    current_user = get_jwt_identity()
    users =get_db().users
    # user = users.find_one({"username":current_user},{"_id":0,"password":0})
    # Update the user with the provided data
    update_result = users.update_one(
        {"email": current_user}, 
        {"$set": data}  # Using $set to update fields
    )
    if update_result.modified_count == 1:
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'message': 'User not found or not updated'}), 404
        
@user_bp.route("/addIntrests",methods = ["POST"])
def add_intrests():
    data = request.get_json()
    current_user = get_jwt_identity()
    users =get_db().users
    # user = users.find_one({"username":current_user},{"_id":0,"password":0})
    # Update the user with the provided data
    update_result = users.update_one(
        {"email": current_user}, 
        {"$set": data}  # Using $set to update fields
    )
    if update_result.modified_count == 1:
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'message': 'User not found or not updated'}), 404
        