from os import getenv
import logging
from logging.handlers import RotatingFileHandler


# ---------------------- ᴄᴏɴғɪɢ ---------------------- #

API_ID = int(getenv("API_ID", "18719789"))
API_HASH = getenv("API_HASH", "a03c27be3e14aac40f62cb4e95207fae")
BOT_TOKEN = getenv("BOT_TOKEN", "6056505972:AAGTyNuBPfiDsOEVPUO6L3_HqRh8bOt6_Xc")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001898451453"))
OWNER_ID = list(map(int, getenv("SUDO_USERS", "5917071362 6018550523 5807975896").split()))
DB_URI = getenv("DATABASE_URL", "postgres://rtzsspzt:DLuJvx8TQGqYqt0XKR9CDnLZmRs6UMr3@berry.db.elephantsql.com/rtzsspzt")
FORCE_SUB_CHANNEL = int(getenv("FORCE_SUB_CHANNEL", "-1001637830162"))
BOT_WORKERS = int(getenv("BOT_WORKERS", "4"))


default_custom_caption = """
 {file_caption}
━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ••• ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴠɪᴅᴇᴏ •••


ᴘᴀɪᴅ ʙᴏᴛs ᴄʜᴀɴɴᴇʟ » @TeleBotsUpdates
ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴠɪᴅᴇᴏ ᴛʜᴀɴ ᴘʟᴇᴀsᴇ 
ᴀᴅᴅ sᴏᴍᴇ ᴍᴇᴍʙᴇʀ ᴀɴᴅ sʜᴀʀᴇ ᴛʜᴇ ʟɪɴᴋ
━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
CUSTOM_CAPTION = getenv("CUSTOM_CAPTION", default_custom_caption)

# --» sᴇᴛ ᴛʀᴜᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘʀᴇᴠᴇɴᴛ ᴜsᴇʀs ғʀᴏᴍ ғᴏʀᴡᴀʀᴅɪɴɢ ғɪʟᴇs ғʀᴏᴍ ʙᴏᴛ
if getenv("PROTECT_CONTENT", None) == 'True':
    PROTECT_CONTENT = True
else:
    PROTECT_CONTENT = False


# --> sᴇᴛ ᴛʀᴜᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪsᴀʙʟᴇ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛs sʜᴀʀᴇ ʙᴜᴛᴛᴏɴ
if getenv("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False




LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
