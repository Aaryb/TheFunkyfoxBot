import asyncio
from bot import Bot
from pyrogram import filters, Client, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from config import CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from TheFunkyFox.helper_func import encode



@Bot.on_message(filters.command(['start','users','broadcast','batch','genlink'], prefixes=["/", "!"]))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...!", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ...!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("💲 ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ 💲", url=f'{link}')]])

    await reply_text.edit(f"<b>ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ</b>\n\n{link}", reply_markup=reply_markup, disable_web_page_preview = True)

    
@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):
   

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("♻️ ᴄᴏᴘʏ ᴜʀʟ ♻️", url=f'{link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
