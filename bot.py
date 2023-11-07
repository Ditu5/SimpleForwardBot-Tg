import os
try:
    os.remove('forwardbot.session')
except:
    pass

import logging
import logging.config
from pyrogram import Client
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from pytz import timezone
from datetime import datetime
from plugins import web_server
from user import User
import pyromod.listen



logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)



class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            Config.BOT_SESSION,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            plugins={
                "root": "plugins"
            },
            workers=10,
            bot_token=Config.BOT_TOKEN
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
    
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, Config.PORT).start()
        self.USER, self.USER_ID = await User().start()

        print(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")

        try:
            await self.send_message(Config.OWNER_ID, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
        
        except:
            pass 

        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(Config.LOG_CHANNEL, f"**__{me.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`\n\n🉐 Vᴇʀsɪᴏɴ : `v{__version__} (Layer {layer})`</b>")
            except:
                print("Pʟᴇᴀꜱᴇ Mᴀᴋᴇ Tʜɪꜱ Iꜱ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢ Cʜᴀɴɴᴇʟ")

                
    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped ⛔")

bot = Bot()
bot.run()
