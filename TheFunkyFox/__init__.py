import sys
import config
import asyncio
import logging
import time
import pyromod.listen
from pyrogram import Client, enums
from pyrogram.enums import ParseMode
from datetime import datetime
from importlib import import_module
from os import environ, getenv, listdir, path



loop = asyncio.get_event_loop()
boot = time.time()


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)



TheFunkyFox = Client(
    ":TheFunkyFox:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=config.BOT_TOKEN,
    workers=config.BOT_WORKER
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


