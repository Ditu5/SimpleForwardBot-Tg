class script(object):
    START_MSG = """Hi {},
This is a simple bot to forward all messages from one channel to other

⚠️Warning
Your account may get banned if you forward more files(from private channels). Use at Own Risk!!"""

    HELP_MSG = """Available commands:-
➜ /index - To index a channel
➜ /forward - To start forwarding
➜ /total - Count total messages in DB
➜ /status - Check Current status
➜ /help - Help data
➜ /stop - To stop all running processes. 

Use /index to index messages from a channel to database.

After indexing you can start forwarding by using /forward.

<b>⦿ Note:</b>
You will require the following data to index a channel:-

☛ <b>Channel Invite Link</b>:- If channel is a Private channel User needs to join channel to acces the messages. Please note that do not leave channel until forwarding completes.

☛ <b>Channel ID</b>:- If channel is a private channel you may need to enter Channel ID. Get it from @MissRose_bot.

☛ <b>SKIP_NO</b>:-From where you want to start Forwarding files.Give 0 if from starting

☛ <b>Caption</b>:- Custom Caption for forwarded files. Use 0 to use default captions.
After fowarding completes use the /cleardb command to clean your database."""

    ABOUT_TXT = """<b>╭───────────⍟
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/Snowball_Official>Sɴᴏᴡʙᴀʟʟ</a>
├👑 Instagram : <a href=https://www.instagram.com/ritesh6_>C-Insta</a> 
├☃️ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/+HzGpLAZXTxoyYTNl>Rᴏᴏғɪᴠᴇʀsᴇ</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├🌀 ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>
╰───────────────⍟ """