from datetime import datetime
from pytz import timezone
from config import Config
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def send_log(b, u):
    try:
        if Config.LOG_CHANNEL is not None:
            curr = datetime.now(timezone("Asia/Kolkata"))
            date = curr.strftime('%d %B, %Y')
            time = curr.strftime('%I:%M:%S %p')
            Bot = await b.get_me()
            await b.send_message(
                Config.LOG_CHANNEL,
                f"**--Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ--**\n\nUꜱᴇʀ: {u.from_user.mention}\nIᴅ: `{u.from_user.id}`\nUɴ: @{u.from_user.username}\n\nDᴀᴛᴇ: {date}\nTɪᴍᴇ: {time}\n\nBy: {Bot.username}"
            )
    except Exception as e:
        print(e)

async def is_subscribed(bot, query):
    try:
        user = await bot.get_chat_member(Config.AUTH_CHANNEL, query.from_user.id)
    except UserNotParticipant:
        pass
    except Exception as e:
        logger.exception(e)
    else:
        if user.status != "banned":
            return True

    return False


async def force_sub(bot, cmd):
    invite_link = await bot.create_chat_invite_link(int(Config.AUTH_CHANNEL))
    buttons = [[InlineKeyboardButton(
        text="📢 Cont. Owner to add you in Channel 📢", url="https://t.me/V_Ditu")]]
    text = "**Sᴏʀʀy Dᴜᴅᴇ Yᴏᴜ'ʀᴇ Nᴏᴛ Jᴏɪɴᴇᴅ My Cʜᴀɴɴᴇʟ 😐. Sᴏ Pʟᴇᴀꜱᴇ Jᴏɪɴ Oᴜʀ Uᴩᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Cᴄᴏɴᴛɪɴᴜᴇ**"

    return await cmd.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))