from google import generativeai as genai
import random
import json
import genai.json_parser as jp

# Initialize the Gemini model (replace with your actual model version if different)
API_KEY = "AIzaSyDTZMVdTznk35EJDU4om7-em3Qo0js4IDQ"
genai.configure(api_key = API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_custom_quiz(topic="AI ML", num_questions=20,difficulty = "Moderate"):
    """
    Generate quiz questions based on user skills and interests using the Gemini model.
    
    :param interests: List of user interests
    :param skills: List of user skills
    :param num_questions: Number of questions to generate
    :return: List of generated questions in JSON format
    """
    
    # Prompt to generate multiple questions at once
    question_prompt = f"""
    Generate {num_questions} multiple-choice quiz questions related to the {topic}.
    Provide each response in JSON format. Each question should be structured like this:
    {{
        "question": "Your question text here",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "correct_option": "A"
    }}
    difficulty level is {difficulty}
    """

    # Use Gemini model to generate all the questions at once
    response = model.generate_content(question_prompt)

    # Assuming the response contains generated content
    generated_text = response.text  # Ensure you're accessing the correct part of the response
    return jp.parse_questions(response.text)


def generate_quiz(interests=["Mobile Application Development", "Software Dev"], skills=["Spring Boot", "Backend", "MySQL"], num_questions=20,difficulty = "Moderate"):
    """
    Generate quiz questions based on user skills and interests using the Gemini model.
    
    :param interests: List of user interests
    :param skills: List of user skills
    :param num_questions: Number of questions to generate
    :return: List of generated questions in JSON format
    """
    
    # Randomly choose a skill and interest
    skill = random.choice(skills)
    interest = random.choice(interests)

    # Prompt to generate multiple questions at once
    question_prompt = f"""
    Generate {num_questions} multiple-choice quiz questions related to the skill '{skill}' and the interest '{interest}'.
    Provide each response in JSON format. Each question should be structured like this:
    {{
        "question": "Your question text here",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "correct_option": "A"
    }}
    difficulty level is {difficulty}
    """

    # Use Gemini model to generate all the questions at once
    response = model.generate_content(question_prompt)

    # Assuming the response contains generated content
    generated_text = response.text  # Ensure you're accessing the correct part of the response

    # try:
    #     # Parse the generated text as JSON
    #     questions = json.loads(generated_text)
    #     return questions

    # except json.JSONDecodeError as e:
    #     print(f"Error parsing the response as JSON: {e}")
    #     return None
    return jp.parse_questions(response.text)
# Example usage




