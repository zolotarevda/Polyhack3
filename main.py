import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
logging.basicConfig(level=logging.INFO)
bot = Bot(token="7642821483:AAG4s2igu88W-lLmLjJ3iMqE_sLuAohSwFc")
dp = Dispatcher()
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Введите назавание кингу автора, и я предложу тебе несколько других книг этого автора.")
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())