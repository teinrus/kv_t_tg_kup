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
        f"👋 Привет, {message.from_user.username}!\n\n"
        "📋 Отправь мне:\n"
        "🔹 Номер ёмкости через пробел уровень или наоборот\n\n"
        "🎯 Я подскажу тебе объём или уровень. 🚀"
    )


async def send_help(message: types.Message):
    await message.answer("Отправь мне номер емкости и через пробел уровень и я скажу объем")


async def button(message: types.Message):
    split_text = message.text.split()
    if len(split_text) == 2:
        with open("data.json", "r") as data:
            data_k = json.loads(data.read())
        try:
            normalized_text = split_text[0][0].lower().replace("е", "e")
            print(normalized_text)
            if "e" in normalized_text:
                print(split_text[0].lower())
                volume = data_k[split_text[0].lower().replace("е", "e")][split_text[1]]
                await message.answer(
                    f"🛢️ Объём в ёмкости {split_text[0]} равен: {volume} 📊"
                )
            else:

                data = data_k[split_text[1].lower().replace("е", "e")]
                target_value = int(split_text[0]) # Целевое значение

                # Поиск ближайшего ключа
                closest_key = min(data, key=lambda k: abs(data[k] - target_value))

                await message.answer(
                    f"📏 Ваш ближайший уровень: {closest_key} см\n"
                    f"🔍 Для значения: {target_value} дал"
                )

        except:
            await message.answer(
                "❌ Упс! Такого уровня или ёмкости нет.\n"
                "📋 Пожалуйста, проверьте данные и попробуйте снова. 😊"
            )


    else:
        await message.answer(
            "⚠️ Текст не соответствует ожидаемому формату.\n"
            "📋 Пожалуйста, проверьте данные и отправьте сообщение в правильной форме. 😊"
        )


async def main():
    # Регистрируем обработчик команды /start с помощью фильтра Command
    dp.message.register(send_welcome, Command(commands=["start"]))
    dp.message.register(button)
    # Удаляем старые обновления и запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
