import pathlib
import textwrap

import google.generativeai as genai

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

genai.configure(api_key="AIzaSyD9LoQRcm0N_JeYk7TfJ6IT_JlG8vU8jWA")

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("What is the meaning of life?")

formatted_text = to_markdown(response.text)
print(formatted_text)
