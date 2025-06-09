# Проєкт Podcast Aggregator

## 📝 Опис завдання

Цей проєкт є реалізацією багаторівневого бекенд-застосунку для агрегації подкастів, керування епізодами, генерації альтернативних заголовків та описів за допомогою LLM, обробки webhook-запитів, парсингу RSS та інтеграції з Telegram-ботом.

Бекенд побудовано з використанням **FastAPI** з інтеграцією **Groq API**, **feedparser**, **requests** та **Telegram Bot API**.

---

## ✅ Реалізовані рівні завдання

| Рівень | Опис | Статус |
|--------|------|--------|
| Level 1 | CRUD для епізодів подкастів | ✅ |
| Level 2 | Генерація альтернативних заголовків/описів за допомогою LLM | ✅ |
| Level 3 | Інтеграція з Telegram-ботом | ✅ |
| Level 4 | Інтеграція Webhook | ✅ |
| Level 5 | Інтеграція RSS парсингу | ✅ |

---

## ⚙ Використані технології

- Python 3.11
- FastAPI
- Pydantic
- Groq API (LLM)
- feedparser + requests (парсинг RSS)
- Telegram Bot API
- Uvicorn

---

## 🔑 Змінні середовища

Створіть файл `.env` у корені проєкту та додайте в нього:

```env
GROQ_API_KEY=your_groq_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token


1️⃣ Встановіть залежності:

pip install -r requirements.txt

2️⃣ Запустіть FastAPI сервер:

uvicorn main:app --reload
(Або з доступом через мережу: --host 0.0.0.0 --port 8000)

3️⃣ Запустіть Telegram-бота:

python telegram_bot.py