from config import Config
from pyrogram import Client, __version__
import logging
import logging.config
BOT_USERNAME=Config.BOT_USERNAME


logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


class User(Client):
    def __init__(self):
        super().__init__(
            Config.SESSION,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            workers=10
        )

    async def start(self):
        await super().start()
        if BOT_USERNAME:
            await User.send_message(self, chat_id=BOT_USERNAME, text="/forward")
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped ⛔")
        
