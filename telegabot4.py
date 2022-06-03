# import the module
import python_weather
import asyncio
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="5567541172:AAEKdSoGWruW7S3URJoRT9RPOYPncqJ1i0k")

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")

    # fetch a weather forecast from a city
    weather = await client.find("Москва")

    celsius = (weather.current.temperature - 32) * 5/9

    # returns the current day's forecast temperature (int)
    print(round(celsius))

    print(weather.current.sky_text)

    print(weather.location_name)

    # get the weather forecast for a few days
    #for forecast in weather.forecasts:
        #print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())