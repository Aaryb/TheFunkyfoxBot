import os
import logging
from logging.handlers import RotatingFileHandler


# ---------------------- ᴄᴏɴғɪɢ ---------------------- #

API_ID = int(os.environ.get("API_ID", "15523618"))
API_HASH = os.environ.get("API_HASH", "8979514968543c31a37a3ed8a0726d83")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5600320195:AAEFUZsFWeMK8TtQRDBRjROIdllyz9_GZAI")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001682891018"))
OWNER_ID = int(os.environ.get("OWNER_ID", "6196151348")) 
DB_URI = os.environ.get("DATABASE_URL", "postgres://rtzsspzt:DLuJvx8TQGqYqt0XKR9CDnLZmRs6UMr3@berry.db.elephantsql.com/rtzsspzt")
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001637830162"))
BOT_WORKERS = int(os.environ.get("BOT_WORKERS", "4"))


default_custom_caption = """
 {file_caption}
━━━━━━━━━━━━━━━━━━━━━━
ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴠɪᴅᴇᴏ 
ʙɪɴ ᴄʜᴀɴɴᴇʟ » [ᴄʟɪᴄᴋ](https://t.me/+A8o3BtG6FlA4YzQ1)
ᴘᴀɪᴅ ʙᴏᴛs ᴄʜᴀɴɴᴇʟ » [ᴄʟɪᴄᴋ](https://t.me/TeleBotsUpdates)
ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴠɪᴅᴇᴏ ᴛʜᴀɴ ᴘʟᴇᴀsᴇ 
ᴀᴅᴅ sᴏᴍᴇ ᴍᴇᴍʙᴇʀ ᴀɴᴅ sʜᴀʀᴇ ᴛʜᴇ ʟɪɴᴋ
━━━━━━━━━━━━━━━━━━━━━━
"""
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", default_custom_caption)

# --» sᴇᴛ ᴛʀᴜᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘʀᴇᴠᴇɴᴛ ᴜsᴇʀs ғʀᴏᴍ ғᴏʀᴡᴀʀᴅɪɴɢ ғɪʟᴇs ғʀᴏᴍ ʙᴏᴛ
if os.environ.get("PROTECT_CONTENT", None) == 'True':
    PROTECT_CONTENT = True
else:
    PROTECT_CONTENT = False


# --> sᴇᴛ ᴛʀᴜᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪsᴀʙʟᴇ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛs sʜᴀʀᴇ ʙᴜᴛᴛᴏɴ
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
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
