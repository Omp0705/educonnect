import google.generativeai as genai

class StudyBuddyChatbot:
    def __init__(self, api_key):
        # Configure the API Key for Google Generative AI
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.chat = self.model.start_chat()
        # Initial system message for the chatbot
        self.chat.send_message(
            """You are a helpful and friendly educational chatbot called "Study Buddy". 
            You specialize in assisting students with their studies. 
            Respond to questions accurately and provide helpful explanations, study tips, and resources. 
            Avoid making claims of sentience or consciousness. Focus on providing practical assistance."""
            )
        

    def send_message(self, message):
        """Send a message to the chatbot and return the response."""
        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            return f"Error: {e}"
