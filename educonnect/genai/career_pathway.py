import google.generativeai as genai
import os
# sample for testing
user_data = {
    "interests": "AI development, mobile app design,web dev",
    "skills": "Python, Java, Android development, Machine Learning",
    "career_goals": "high income, growth opportunities"
}
generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 40,
        "max_output_tokens": 2048,
    }
safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]

API_KEY = "AIzaSyDTZMVdTznk35EJDU4om7-em3Qo0js4IDQ"
genai.configure(api_key = API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def get_carrier_guidance(user_data = user_data):
    prompt = f"""
    I need career guidance based on my responses to the following questions. Please analyze my inputs and provide a list of relevant resources, including online tutorials, courses, YouTube channels, free books, blog posts, articles, and community forums that can help me explore potential career paths.

Interests: {user_data['interests']}
Key Skills: {user_data['skills']}
Career Goals: {user_data['career_goals']}
Additional Information:
I am looking for free online resources, including:
Tutorials and courses
YouTube channels
Free books or eBooks
Blog posts and articles
Community forums or discussion groups
all this for each career pathway.generate 3 pathways
Format: Please present the resources in an organized list, categorizing each type for clarity and give it in json format.
"""
    response = model.generate_content(prompt)
    return response.text

print(get_carrier_guidance(user_data=user_data))
