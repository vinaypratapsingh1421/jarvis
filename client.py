from openai import OpenAI
from google import genai

# client = OpenAI(
#   api_key="AIzaSyBkHyn3XjLdxnp2fSptR7tmnoIhOUrnf24"
# )

# response = client.responses.create(
#   model="gemini-2.5-flash",
#   input="write a haiku about ai",
#   store=True,
# )

# print(response.output_text)

# from google import genai

# Initialize client
# client = genai.Client(api_key="AIzaSyBkHyn3XjLdxnp2fSptR7tmnoIhOUrnf24")

# # Send the request
# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="What is coading"
# )

# # ✅ Correct way to access text
# for candidate in response.candidates:
#     for part in candidate.content.parts:
#         print(part.text)


# from google import genai

# Initialize the client with your API key
client = genai.Client(api_key="AIzaSyBkHyn3XjLdxnp2fSptR7tmnoIhOUrnf24")

# Send a prompt
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works in a few words"
)

print(response.output_text)



# import requests
# import json

# url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
# api_key = "AIzaSyBkHyn3XjLdxnp2fSptR7tmnoIhOUrnf24"  # Replace with your actual API key

# headers = {
#     "Content-Type": "application/json",
#     "X-goog-api-key": api_key
# }

# data = {
#     "contents": [
#         {
#             "parts": [
#                 {
#                     "text": "what is the capital of india"
#                 }
#             ]
#         }
#     ]
# }

# response = requests.post(url, headers=headers, data=json.dumps(data))

# # Print full response
# print(response.status_code)
# print(response.json())



# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="what is the capital of india"
# )
# print(response.text)