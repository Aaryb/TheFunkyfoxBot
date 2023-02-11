import os
from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "TheNatasha1Bot")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "5881219743"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5881219743").split()))
MONGO_URI = getenv("MONGO_URI", "mongodb+srv://MrsFallenBot:MrsFallenBot@cluster0.hsedwn2.mongodb.net/?retryWrites=true&w=majority")
