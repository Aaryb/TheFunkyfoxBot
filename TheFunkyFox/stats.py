import aiohttp
import logging
from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import URL_SHORTNER_API_KEY, URL_SHORTNER_API
from TheFunkyFox.helper_func import get_readable_time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


USER_REPLY_TEXT = """<code> ᴀʀᴇ ʙʜᴀɪʏᴀ.. ᴀᴀᴘ ᴋᴏɴ ᴄʜʟᴇ ᴊᴀᴀᴏ ʏʜᴀ sᴇ ᴍᴜᴊʜᴇ ᴀᴀᴘsᴇ ʙᴀᴀᴛ ɴʜɪ ᴋʀɴɪ. </code>"""


@Bot.on_message(filters.private)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)


