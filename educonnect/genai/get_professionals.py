import requests

# Replace with your actual API key from Proxycurl
api_key = '3-RlKcTLbZ_INQGUy2d9CQ'
headers = {'Authorization': 'Bearer ' + api_key}

# Proxycurl API endpoint for person search
api_endpoint = 'https://nubela.co/proxycurl/api/v2/search/person'

# Define parameters for the search query based on student skills and interests
params = {
    'country': 'IN',  # Location (India as an example)
    'skills': 'Python, Java',  # Pass dynamic skills
    'interests': 'AI, Backend Development',  # Pass dynamic interests
    'current_role_title': 'software engineer',  # Example role
    'page_size': '5',  # Number of results to fetch
    'enrich_profiles': 'enrich',  # Request enriched profiles
}

# Make the API request
response = requests.get(api_endpoint, params=params, headers=headers)

# Check if the response is successful
if response.status_code == 200:
    # Parse the JSON response
    people_data = response.json()
    
    # Extract only the required information
    extracted_data = []
    for person in people_data:
        person_info = {
            'name': person.get('full_name', 'N/A'),
            'linkedin_url': person.get('linkedin_profile_url', 'N/A'),
            'job_title': person.get('current_role', {}).get('title', 'N/A'),
            'company_name': person.get('current_company', {}).get('name', 'N/A'),
            'company_linkedin_url': person.get('current_company', {}).get('linkedin_profile_url', 'N/A'),
            'social_accounts': person.get('social_accounts', []),
        }
        extracted_data.append(person_info)
    
    # Print the extracted information
    for idx, person in enumerate(extracted_data):
        print(f"Person {idx + 1}:")
        print(f"Name: {person['name']}")
        print(f"LinkedIn Profile: {person['linkedin_url']}")
        print(f"Current Job Title: {person['job_title']}")
        print(f"Company Name: {person['company_name']}")
        print(f"Company LinkedIn: {person['company_linkedin_url']}")
        print(f"Social Accounts: {person['social_accounts']}")
        print("----------")
else:
    print(f"Error: {response.status_code}, {response.text}")
