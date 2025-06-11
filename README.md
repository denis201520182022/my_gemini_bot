# 🤖 Telegram Voice Assistant с Google Gemini и Whisper

Это Telegram-бот на Python, который понимает **голосовые** и **текстовые** сообщения и отвечает на них с помощью **Google Gemini AI**.  
Проект использует **нейросетевое распознавание речи** (Whisper) и **модель генерации текста** от Google (Gemini 2.0 Flash).

---

## 🧠 Что делает этот бот?

- Принимает **текстовые** и **голосовые** сообщения от пользователя.
- Если сообщение голосовое:
  - Скачивает файл `.ogg` от Telegram.
  - Конвертирует его в `.wav` с помощью `ffmpeg` (16000 Гц, моно).
  - Распознаёт речь с помощью модели **Whisper** (OpenAI).
- Полученный текст (или исходный текст сообщения) отправляется в **Google Gemini 2.0 Flash**.
- Бот возвращает сгенерированный ответ пользователю.

---

## 🧱 Архитектура проекта

project/
├── main.py # Запуск Telegram-бота
├── config.py # Переменные среды (токены и ключи API)
│
├── handlers/
│ └── main_handler.py # Логика обработки команд, текста и голосовых
│
├── services/
│ ├── gemini_client.py # Класс-клиент для работы с Google Gemini API
│ ├── speech_to_text.py # Конвертация и распознавание аудио через Whisper
│ └── user_history.py # (опционально) сохранение истории переписки
│
├── downloads/ # Временные файлы аудио от пользователей
└── requirements.txt # Зависимости проекта



---

## 🛠 Используемые технологии

| Технология       | Назначение |
|------------------|------------|
| [Python 3.10+](https://www.python.org/) | Основной язык проекта |
| [aiogram](https://docs.aiogram.dev/en/latest/) | Асинхронный Telegram Bot API |
| [Google Generative AI SDK](https://ai.google.dev/) | Интеграция с Gemini (модель `gemini-2.0-flash-exp`) |
| [Whisper](https://github.com/openai/whisper) | Распознавание речи из голосовых сообщений |
| [ffmpeg](https://ffmpeg.org/) | Конвертация аудио из `.ogg` в `.wav` |
| asyncio | Асинхронное выполнение задач (скачивание, обработка, ответы) |
| os / subprocess | Работа с файлами и вызов внешних команд (`ffmpeg`) |

---

## 💡 Принцип работы

1. Пользователь отправляет сообщение (текст или голос).
2. Бот обрабатывает сообщение:
   - Если это текст — сразу отправляется в Gemini.
   - Если это голос:
     - Скачивается `.ogg` файл.
     - Конвертируется в `.wav` через `ffmpeg`.
     - Распознаётся через `whisper.load_model("small")`.
     - Результат передаётся в Gemini.
3. Ответ от Gemini отправляется обратно пользователю.

---
---

## 📦 Зависимости проекта

Установи зависимости с помощью `pip`:
Содержимое:
aiogram==3.4.1
google-generativeai==0.5.2
openai-whisper
ffmpeg-python

```bash
pip install -r requirements.txt



## 🧑‍💻 Автор

Разработано студентом-программистом **Денисом**.

📬 Telegram: [@denis20152018](https://t.me/denis20152018)  
💻 GitHub: [github.com/your_username](https://github.com/denis201520182022)
📧 Email: den14kotlyarov@yandex.ru

С радостью отвечу на вопросы и предложения по проекту!
