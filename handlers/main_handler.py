import os
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from services.gemini_client import GeminiClient
from services.speech_to_text import transcribe_audio, convert_ogg_to_wav
from config import GEMINI_API_KEY
from services.user_history import add_message, get_history

router = Router()
gemini = GeminiClient(GEMINI_API_KEY)

# При старте
@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Привет! Я бот с поддержкой Gemini и распознавания голоса 🤖")

# Обработка текстовых сообщений
@router.message(F.text)
async def text_handler(message: types.Message):
    prompt = message.text
    response = gemini.generate_text(prompt)
    await message.answer(response)

# Обработка голосовых сообщений
@router.message(F.voice)
async def voice_handler(message: types.Message):
    voice = message.voice
    file = await message.bot.get_file(voice.file_id)
    file_path = file.file_path

    os.makedirs("downloads", exist_ok=True)
    ogg_path = f"downloads/{voice.file_unique_id}.ogg"
    wav_path = f"downloads/{voice.file_unique_id}.wav"

    await message.bot.download_file(file_path, ogg_path)
    await convert_ogg_to_wav(ogg_path, wav_path)

    text = await transcribe_audio(wav_path)

    if not text.strip():
        await message.answer("Не удалось распознать голосовое сообщение.")
        return

    response = gemini.generate_text(text)
    await message.answer(response)

    # Очистка временных файлов (если нужно)
    try:
        os.remove(ogg_path)
        os.remove(wav_path)
    except Exception:
        pass
