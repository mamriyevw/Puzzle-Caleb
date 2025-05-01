import asyncio
import json
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv("7685494696:AAHzN9vLLs8ejN9NqghjUtPdNnjtst6i5Yk")

bot = Bot(token=7685494696:AAHzN9vLLs8ejN9NqghjUtPdNnjtst6i5Yk)
dp = Dispatcher(bot)

with open("config.json", "r") as f:
    config = json.load(f)

with open("puzzles/level1.json", "r") as f:
    puzzle = json.load(f)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(config["welcome_message"])
    await asyncio.sleep(1)
    await message.answer("Loading puzzle...")
    await asyncio.sleep(2)
    await bot.send_photo(message.chat.id, open(puzzle["image"], "rb"))
    await message.answer(puzzle["question"])

@dp.message_handler()
async def check_answer(message: types.Message):
    user_answer = message.text.strip().lower()
    correct_answer = puzzle["answer"].strip().lower()

    if user_answer == correct_answer:
        await message.answer("Correct! Well done.")
    else:
        await message.answer("Try again!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
