from aiogram import Bot, Dispatcher, executor, types

#Токен для подключения к телеграм API.
TOKEN_API = "1887379253:AAFYEPxXuqmk1cXUEBFKaKod_3pX2oQSuJU" 

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp)