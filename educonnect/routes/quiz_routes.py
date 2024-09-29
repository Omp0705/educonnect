from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
import datetime as dt
import random
import jwt 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import genai.generate_quiz as gquiz
quiz_bp = Blueprint('quiz', __name__)

def get_db():
    from app import mongo
    return mongo.db

@quiz_bp.route('/add_quiz', methods=['POST'])
@jwt_required() 
def add_quiz():
    quizzes = get_db().quizzes
    data = request.get_json()
    current_user = get_jwt_identity()
    # Fetch user details from the database
    users = get_db().users
    user = users.find_one({"username": current_user}, {"_id": 0, "password": 0})
    interests = user.get('interests', [])  # Get interests from user
    skills = user.get('skills',[])
    questions = gquiz.generate_quiz(interests,skills,data['noq'],difficulty = data['level'])
    data['questions'] = questions
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    try:
        quizzes.insert_one(data)
        return jsonify({'message': 'Quiz added successfully'}), 201
    except Exception as e:
        return jsonify({'message': f'Error adding quiz: {str(e)}'}), 500

@quiz_bp.route('/quiz/get_quiz/<string:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    quizzes = get_db().quizzes
    quiz = quizzes.find_one({"quiz_id": quiz_id})

    if quiz:
        return jsonify(quiz), 200
    else:
        return jsonify({'message': 'Quiz not found'}), 404

@quiz_bp.route('/generate_custom_quiz', methods=['POST'])
def generate_custom_quiz():
    data = request.get_json()
    questions = gquiz.generate_custom_quiz(topic=data['topic'],num_questions=data['noq'],difficulty = data['level'])

    if not questions:
        return jsonify({'message': 'No quizzes available'}), 404
    
    return jsonify({'questions':questions}), 200