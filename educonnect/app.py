from flask import Flask,render_template,jsonify
from flask_pymongo import PyMongo 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import jwt
import google.generativeai as genai
from dotenv import load_dotenv
import os
from datetime import timedelta
from routes.upload_image import upload_bp
from routes.user_routes import user_bp
from routes.professional_routes import professional_bp
from routes.quiz_routes import quiz_bp
import genai.generate_quiz as quiz
from studdybuddy.chatbot import StudyBuddyChatbot
from flask_socketio import SocketIO, emit
import eventlet
load_dotenv()

app = Flask(__name__)

app.register_blueprint(upload_bp, url_prefix='/image')
app.register_blueprint(user_bp,url_prefix='/user')
app.register_blueprint(professional_bp,url_prefix='/professional')
app.register_blueprint(quiz_bp,url_prefix ='/quizes' )

app.config["MONGO_URI"] = os.getenv("MONGO_URI")  
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)

mongo = PyMongo(app)
jwt = JWTManager(app)
socketio = SocketIO(app,async_mode='eventlet')

db = mongo.db
users_collection = db["users"]
login_details = db["logins"]
users_collection.create_index("email", unique=True)
users_collection.create_index("username", unique=True)
login_details.create_index("username", unique=True)
chatbot = StudyBuddyChatbot(os.getenv("API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

# Handle WebSocket messages
@socketio.on('send_message')
def handle_message(data):
    user_message = data.get('message')
    print(f"Received message: {user_message}")

    # Send the message to the chatbot and get the response
    chatbot_response = chatbot.send_message(user_message)
    print(f"Chatbot response: {chatbot_response}")

    # Send the response back to the client
    emit('response_message', {'response': chatbot_response})

if __name__ == '__main__':
    # app.run(debug=True)
    socketio.run(app, host='0.0.0.0', port=5000)