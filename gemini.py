from google.api_core.exceptions import ResourceExhausted
import google.generativeai as genai
import os
import PIL.Image

from dotenv import load_dotenv, find_dotenv


def ask(question, filename):
    load_dotenv(find_dotenv())
    img = PIL.Image.open(filename)

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    try:
        response = model.generate_content([question, img], stream=True)
    except ResourceExhausted:
        return "Quota exceeded."
    response.resolve()
    aianswer = response.text
    aianswerclean = aianswer.replace("*", "")
    return aianswerclean
