from aiogram import Bot, Dispatcher, executor, types
import python_weather

bot = Bot(token="5544620807:AAF0TC3OgrYQ3OolPkI4UvQjw6lOIxWr2Vw")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")

@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celsius = (weather.current.temperature - 32) * 5 / 9
    resp_msg = weather.location_name + "\n"
    resp_msg += f"Текущая температура: {round(celsius)}\n"
    resp_msg += f"Состояние погоды: {weather.current.sky_text}\n"

    if celsius <=10:
        resp_msg +="\n\nПрохладно! Одевайтесь теплее!"
    else:
        resp_msg +="\n\nТепло! Одевайтесь легко!"
    await message.answer(resp_msg)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)