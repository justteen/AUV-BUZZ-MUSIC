from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hello! Saya asisten music .\n\n ❗️ Rules:\n   - TIDAK SPAM CHAT \n\n 👉 **Kirim link group apabila asisten tidak dapat masuk.**\n\n ⚠️ PENGINGAT: JANGAN MENGIRIM PESAN PENTING DISINI\n    - JANGAN TAMBAHKAN KE GROUP PRIVASI ANDA.\n   - JANGAN BAGI INFORMASI PENTING DISINI\n\n")
  return                        
