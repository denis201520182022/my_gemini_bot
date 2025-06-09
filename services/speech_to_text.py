import subprocess
import whisper

async def convert_ogg_to_wav(input_path: str, output_path: str):
    subprocess.run([
        "ffmpeg", "-i", input_path,
        "-ar", "16000",  # частота дискретизации 16 кГц
        "-ac", "1",      # моно
        output_path
    ], check=True)

# Загружаем модель один раз при импорте
model = whisper.load_model("small")

async def transcribe_audio(audio_path: str) -> str:
    result = model.transcribe(audio_path)
    return result.get("text", "")
