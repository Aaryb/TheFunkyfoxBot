from bot import Bot
from config import OWNER_ID
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TheFunkyFox.helper_func import encode, get_message_id



@Bot.on_message(filters.private & filters.user(OWNER_ID) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "ғᴏʀᴡᴀʀᴅ ғɪʀsᴛ ᴍsɢ ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ (ᴡɪᴛʜ ǫᴜᴏᴛᴇs) \n\nᴏʀ sᴇɴᴅ ᴛʜᴇ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛ ʟɪɴᴋ", chat_id = update.message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ ᴇʀʀᴏʀ\n\nᴛʜɪs ғᴏʀᴡᴀʀᴅᴇᴅ ᴘᴏsᴛ ɪɴ ɴᴏᴛ ғʀᴏᴍ ᴍʏ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴛʜɪs ʟɪɴᴋ ɪs ɴᴏᴛ ᴛᴀᴋᴇɴ ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ.", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "ғᴏʀᴡᴀʀᴅ ʟᴀsᴛ ᴍsɢ ғʀᴏᴍ ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ (ᴡɪᴛʜ ǫᴜᴏᴛᴇs) \nᴏʀ sᴇɴᴅ ᴛʜᴇ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛ ʟɪɴᴋ", chat_id = update.message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ ᴇʀʀᴏʀ\n\nᴛʜɪs ғᴏʀᴡᴀʀᴅᴇᴅ ᴘᴏsᴛ ɪs ɴᴏᴛ ғʀᴏᴍ ᴍʏ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴛʜɪs ʟɪɴᴋ ɪs ɴᴏᴛ ᴛᴀᴋᴇɴ ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ.", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("♻️ ᴄᴏᴘʏ ᴜʀʟ ♻️", url=f'{link}')]])
    await second_message.reply_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ\n\n{link}", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(OWNER_ID) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴅʙ ᴄʜᴀɴɴᴇʟ (ᴡɪᴛʜ ǫᴜᴏᴛᴇs) \nᴏʀ sᴇɴᴅ ᴛʜᴇ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛ ʟɪɴᴋ", chat_id = update.message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ ᴇʀʀᴏʀ\n\nᴛʜɪs ғᴏʀᴡᴀʀᴅᴇᴅ ᴘᴏsᴛ ɪs ɴᴏᴛ ғʀᴏᴍ ᴍʏ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴛʜɪs ʟɪɴᴋ ɪs ɴᴏᴛ ᴛᴀᴋᴇɴ ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("♻️ ᴄᴏᴘʏ ᴜʀʟ ♻️", url=f'{link}')]])
    await channel_message.reply_text(f"<b>ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟɪɴᴋ</b>\n\n{link}", quote=True, reply_markup=reply_markup)
