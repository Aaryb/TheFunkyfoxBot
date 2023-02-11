import asyncio
import logging
import time
import pyrogram
from importlib import import_module
from os import environ, getenv, listdir, path
#from dotenv import load_dotenv
from pyrogram import Client
#from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, SUDO_USERS
import config

loop = asyncio.get_event_loop()
#pyrogram.dotenv.load_dotenv()
boot = time.time()


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)



TheFunkyFox = Client(
    ":TheFunkyFox:",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
)


async def TheFunkyFox_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await TheFunkyFox.start()
    getme = await TheFunkyFox.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name


loop.run_until_complete(TheFunkyFox_bot())


