from google import genai

user_input = input('Enter a question: ')

client = genai.Client(api_key='API_KEY')

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=user_input + ' Explain in a few words.'
)
print(response.text)