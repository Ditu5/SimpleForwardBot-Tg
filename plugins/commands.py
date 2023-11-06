import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import asyncio
import sys
from plugins.text import script
from database import userDb
from utils import is_subscribed, force_sub

buttons=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="abt")
            ],
            [
                InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/+mCdsJ7mjeBEyZWQ1"),
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url="https://t.me/+HzGpLAZXTxoyYTNl")
            ]
        ]
        )


# Force Sub Handler
@Client.on_message(filters.private)
async def _(bot: Client, cmd):
    if not await is_subscribed(bot, cmd):
        return await force_sub(bot, cmd)

    await cmd.continue_propagation()


@Client.on_message(filters.private & filters.command('start'))
async def start(client, message:Message):


    await userDb.add_user(message.from_user.id, client, message)
    await client.send_message(
        chat_id=message.chat.id,
        text=script.START_MSG.format(
                message.from_user.first_name),
        reply_markup=buttons,
        parse_mode="html")


@Client.on_message(filters.command("stop"))
async def stop_button(bot, message):

    if str(message.from_user.id) not in Config.OWNER_ID:
        return
    msg = await bot.send_message(
        text="Stoping all processes...",
        chat_id=message.chat.id
    )
    await asyncio.sleep(1)
    await msg.edit("All Processes Stopped and Restarted")
    os.execl(sys.executable, sys.executable, *sys.argv)


@Client.on_message(filters.private & filters.command('help'))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=script.HELP_MSG,
        parse_mode="html")



@Client.on_callback_query(filters.regex(r'^back$'))
async def back_btn(bot,cb):
    await cb.message.edit_text(text=script.START_MSG.format(
                cb.from_user.first_name),
        reply_markup=buttons,
        parse_mode="html")

@Client.on_callback_query(filters.regex(r'^help$'))
async def cb_help(bot, cb):
    await cb.message.edit_text(script.HELP_MSG,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⟸ Bᴀᴄᴋ", callback_data='back')]]))



@Client.on_callback_query(filters.regex(r'^abt$'))   
async def cb_abt(bot, cb):
    await cb.message.edit_text(text=script.ABOUT_TXT, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⟸ Bᴀᴄᴋ", callback_data='back')]]))