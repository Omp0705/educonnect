from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import datetime as dt

professional_bp = Blueprint('professional', __name__)

def get_db():
    from app import mongo
    return mongo.db

SECRET_KEY = "your_secret_key"

@professional_bp.route('/register_professional', methods=['POST'])
def register_professional():
    professionals = get_db().professionals
    data = request.get_json()

    # Check if user already exists
    if professionals.find_one({"email": data['email']}):
        return jsonify({"error": "Professional already exists"}), 400

    hashed_password = generate_password_hash(data['password'])
    professional = {
        "name": data['name'],
        "email": data['email'],
        "password": hashed_password,
        "role": data['role'],
        "industry": data['industry'],
        "job_title": data['job_title'],
        "expertise": data['expertise'],
        "available_for_mentorship": data['available_for_mentorship'],
        "profile_image": data['profile_image'],
        "interests": data['intrests'],
        "socials": data['socials'],
        "created_at": dt.datetime.utcnow(),
        "updated_at": dt.datetime.utcnow()
    }
    professionals.insert_one(professional)
    return jsonify({"message": "Professional registered successfully"}), 201

@professional_bp.route('/login', methods=['POST'])
def login():
    professionals = get_db().professionals
    data = request.get_json()
    professional = professionals.find_one({"email": data['email']})

    if professional and check_password_hash(professional['password'], data['password']):
        access_token = create_access_token(identity=professional['email'])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

@professional_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    current_user = get_jwt_identity()
    professionals = get_db().professionals
    professional = professionals.find_one({"email": current_user}, {"_id": 0, "password": 0})

    if professional:
        return jsonify(professional), 200
    else:
        return jsonify({"error": "Professional not found"}), 404

@professional_bp.route('/update_profile', methods=['POST'])
@jwt_required()
def update_profile():
    data = request.get_json()
    current_user = get_jwt_identity()
    professionals = get_db().professionals

    update_result = professionals.update_one(
        {"email": current_user},
        {"$set": {
            "name": data['name'],
            "role": data['role'],
            "industry": data['industry'],
            "job_title": data['job_title'],
            "expertise": data['expertise'],
            "available_for_mentorship": data['available_for_mentorship'],
            "profile_image": data['profile_image'],
            "interests": data['interests'],
            "socials": data['socials'],
            "updated_at": dt.datetime.utcnow()
        }}
    )

    if update_result.modified_count == 1:
        return jsonify({'message': 'Profile updated successfully'}), 200
    else:
        return jsonify({'message': 'Profile not updated'}), 404

@professional_bp.route('/update_job_details', methods=['POST'])
@jwt_required()
def update_job_details():
    data = request.get_json()
    current_user = get_jwt_identity()
    professionals = get_db().professionals

    update_result = professionals.update_one(
        {"email": current_user},
        {"$set": {
            "job_title": data['job_title'],
            "industry": data['industry'],
            "updated_at": dt.datetime.utcnow()
        }}
    )

    if update_result.modified_count == 1:
        return jsonify({'message': 'Job details updated successfully'}), 200
    else:
        return jsonify({'message': 'Job details not updated'}), 404

@professional_bp.route('/add_skills', methods=['POST'])
@jwt_required()
def add_skills():
    data = request.get_json()
    current_user = get_jwt_identity()
    professionals = get_db().professionals

    update_result = professionals.update_one(
        {"email": current_user},
        {"$set": {"expertise": data['expertise'], "updated_at": dt.datetime.utcnow()}}
    )

    if update_result.modified_count == 1:
        return jsonify({'message': 'Skills added successfully'}), 200
    else:
        return jsonify({'message': 'Skills not added'}), 404

@professional_bp.route('/add_interests', methods=['POST'])
@jwt_required()
def add_interests():
    data = request.get_json()
    current_user = get_jwt_identity()
    professionals = get_db().professionals

    update_result = professionals.update_one(
        {"email": current_user},
        {"$set": {"interests": data['interests'], "updated_at": dt.datetime.utcnow()}}
    )

    if update_result.modified_count == 1:
        return jsonify({'message': 'Interests added successfully'}), 200
    else:
        return jsonify({'message': 'Interests not added'}), 404
