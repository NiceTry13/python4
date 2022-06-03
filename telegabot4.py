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
    resp_msg += f"Текущая температура: {celsius}\n"
    resp_msg += f"Состояние погоды: {weather.current.sky_text}\n"
    await message.answer(resp_msg)

if  __name__ == "__telegabot4__":
    executor.start_polling(dp, skip_updates=True)
    #await client.close()





#async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    #client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")

    # fetch a weather forecast from a city
    #weather = await client.find("Москва")

    #celsius = (weather.current.temperature - 32) * 5/9

    # returns the current day's forecast temperature (int)
    #print(round(celsius))

    #print(weather.current.sky_text)

    #print(weather.location_name)

    # get the weather forecast for a few days
    #for forecast in weather.forecasts:
        #print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    #await client.close()

#if __name__ == "__main__":
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(getweather())