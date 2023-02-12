import asyncio
import importlib
from pyrogram import idle
from TheFunkyFox.modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Natasha.modules." + all_module)
    print("────────────BOT START────────────")
    await idle()
    print("GoodBye! Stopping Bot")


if __name__ == "__main__":
    loop.run_until_complete(sumit_boot())
