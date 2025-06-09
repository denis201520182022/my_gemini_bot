import os
import google.generativeai as genai

class GeminiClient:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-2.0-flash-exp")

    def generate_text(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text
