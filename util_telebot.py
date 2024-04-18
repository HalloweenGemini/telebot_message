import telegram # pip install python-telegram-bot
import asyncio
import os
from dotenv import load_dotenv

load_dotenv() 

mc = os.getenv("mc")
token = os.getenv("token")

bot = telegram.Bot(token)

async def send_message(message):
    bot = telegram.Bot(token=token)
    await bot.sendMessage(mc,message)

async def send_photo(photo):
    bot = telegram.Bot(token=token)
    await bot.sendPhoto(mc,photo)

#ex) asyncio.run(send_message("Hello, World!"))