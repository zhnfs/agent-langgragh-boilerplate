#A basic main.py that loads environment variables and initializes a basic LLM.

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
# fast_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
# large_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
standard_model = ChatGoogleGenerativeAI(model="gemma-4-31b-it")
fallback_model = ChatGoogleGenerativeAI(model="gemma-4-26b-a4b-it")

# Simple test prompt to validate Gemma model
prompt = "Hello, what model are you and how are you doing today?"
response = standard_model.invoke(prompt)
print(f"Prompt: {prompt}\nGemma response: {response}")