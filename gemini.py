# from google import genai


# client = genai.Client(api_key="AIzaSyBkHyn3XjLdxnp2fSptR7tmnoIhOUrnf24")

# # Send the request
# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="who is shahrukh khan"
# )

# # ✅ Correct way to access text
# for candidate in response.candidates:
#     for part in candidate.content.parts:
#         print(part.text)

# pip install google-genai
from google import genai

def aiProcess(command):
    # Initialize Gemini client
    client = genai.Client(api_key="AIzaSyBkHyn3XjLdxnp2fSptR7tmnoIhOUrnf24")

    # Combine system and user instruction into a single prompt
    prompt = f"""
You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud.
Give short responses please.

User: {command}
"""

    # Send the request to Gemini
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # You can also try gemini-1.5-flash or gemini-1.5-pro
        contents=prompt
    )

    # Extract and return the generated text
    result = [] 
    for candidate in response.candidates:
        for part in candidate.content.parts:
            result.append(part.text)

    return " ".join(result)  # Join multiple parts into a single string

print(aiProcess("who is shahrukh khan in hindi"))