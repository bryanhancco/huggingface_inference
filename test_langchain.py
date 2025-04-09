from langchain_google_genai import GoogleGenerativeAI

api_key = "AIzaSyD9LoQRcm0N_JeYk7TfJ6IT_JlG8vU8jWA"

llm = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)
print(
    llm.invoke(
        "What are some of the pros and cons of Python as a programming language?"
    )
)

