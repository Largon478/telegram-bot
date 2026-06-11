from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from deep_translator import GoogleTranslator
import asyncio

TOKEN = "8915229377:AAHnaSD3EeI0xAoyj-eladqskBMkPemBWQw"

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_lang = {}

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🌐 Бот-перекладач\n\n"
        "/uk - Українська\n"
        "/en - English\n"
        "/pl - Polski\n"
        "/de - Deutsch\n\n"
        "Вибери мову та надсилай текст."
    )

@dp.message(Command("uk"))
async def uk(message: Message):
    user_lang[message.chat.id] = "uk"
    await message.answer("🇺🇦 Обрана українська")

@dp.message(Command("en"))
async def en(message: Message):
    user_lang[message.chat.id] = "en"
    await message.answer("🇬🇧 Обрана англійська")

@dp.message(Command("pl"))
async def pl(message: Message):
    user_lang[message.chat.id] = "pl"
    await message.answer("🇵🇱 Обрана польська")

@dp.message(Command("de"))
async def de(message: Message):
    user_lang[message.chat.id] = "de"
    await message.answer("🇩🇪 Обрана німецька")

@dp.message(F.text)
async def translate(message: Message):
    lang = user_lang.get(message.chat.id, "uk")

    try:
        translated = GoogleTranslator(
            source="auto",
            target=lang
        ).translate(message.text)

        await message.answer(f"🌐 Переклад:\n\n{translated}")

    except Exception as e:
        await message.answer(f"❌ Помилка: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())