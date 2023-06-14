from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

HELP_COMMANDS = """
/help - Список комманд
/start - Начать работу с ботом
"""

#Токен для подключения к телеграм API.
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMANDS)
    await message.delete()

@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='Добро пожаловать в мой телеграмм бот!')
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp)