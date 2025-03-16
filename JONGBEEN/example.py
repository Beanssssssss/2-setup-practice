import os
from dotenv import load_dotenv
# Load the .env file
load_dotenv()
# Get the API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
hubspot_api_key = os.getenv("HUBSPOT_API_KEY")
# Print the API key
print(openai_api_key)