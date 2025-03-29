import pandas as pd
from datasets import load_dataset
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)
bot = Bot(token="7642821483:AAG4s2igu88W-lLmLjJ3iMqE_sLuAohSwFc")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Введите назавание книги, и я предложу тебе несколько других книг этого автора.")

books = pd.DataFrame(load_dataset("slon-hk/BooksSummarizationRU", split='train'))

@dp.message(book_name)
async def recommender(book_name, message:types.Message):
    s = ''
    book_name = book_name.lower()
    book_names = [book.lower() for book in books.Title]
    if book_name in book_names:
        author = books.loc[book_names.index(book_name), "Author"]
        for book in set(books.Title[books.Author == author]):
            if book.lower() != book_name:
                s += book+',\n'
            await message.answer(s)


async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
