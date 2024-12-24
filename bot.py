import asyncio
import json

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '7973000607:AAFjpa3fLDmRJWYkQK1rpP1shz9UrRqMsHw'  # Укажи свой токен
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Обработчик команд
async def send_welcome(message: types.Message):
    await message.answer(
        f"Привет {message.from_user.username}! Отправь мне номер емкости и через пробел уровень и я скажу объем")


async def send_help(message: types.Message):
    await message.answer("Отправь мне номер емкости и через пробел уровень и я скажу объем")


async def button(message: types.Message):
    split_text = message.text.split()
    if len(split_text) == 2:
        with open("data.json", "r") as data:
            data_k = json.loads(data.read())
        try:
            volume = data_k[split_text[0]][split_text[1]]
            await message.answer(f"Ваш объем в {split_text[0]} равен {volume}")
        except:
            await message.answer(f"Такого уровня или емкости нет")

    else:
        await message.answer("текст не соотвествует")


async def main():
    # Регистрируем обработчик команды /start с помощью фильтра Command
    dp.message.register(send_welcome, Command(commands=["start"]))
    dp.message.register(button)
    # Удаляем старые обновления и запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
