from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>tambahkan saya menjadi admin. jika anda pertama kali menggunakan bot ini maka harus cek /help</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "AUV-BUZZ MUSIC"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Saya bergabung atas permintaan anda\n\n🤗 tambahkan saya sebagai admin, untuk dapat memulai VCG 🤗")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asisten telah bergabung dalam chat</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} Asisten musik tidak dapat masuk ke grup! Pastikan Asisten musik tidak dalam blokir grup."
            "\n\nOr manual tambahkan @auvbuzzbot ke grup & coba kembali</b>",
        )
        return
    await message.reply_text(
            "<b>Asisten musik telah bergabung</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Asisten tidak dapat keluar dari grup karena sedang delay."
            "\n\nOr manual kick dari grup</b>",
        )
        return
