from aiogram import Router, types
from aiogram.filters import CommandStart
from services.gemini_client import GeminiClient
from config import GEMINI_API_KEY

router = Router()
gemini = GeminiClient(GEMINI_API_KEY)

@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Привет! Я бот с поддержкой Gemini 🤖")

@router.message()
async def echo_handler(message: types.Message):
    prompt = message.text
    response = gemini.generate_text(prompt)
    await message.answer(response)
