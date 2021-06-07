from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""**HELLO!, Saya  {bn}, Adalah bot untuk memutar musik dalam obrolan suara group chat anda.\n\n Jangan lupa untuk menambahkan asisten musik juga, agar dapat memutar musiknya.\n\n /help untuk mengetahui perintah**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support⚡️", url="https://t.me/ossuport3"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Creator⚡️", url="https://t.me/psycho_syridwan"
                    ),
                    InlineKeyboardButton(
                        "Group⚡️", url="https://t.me/ossuport"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        "Tambahkan bot ke Group⚡️", url="http://t.me/auvbuzzbot?startgroup=true"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        "Tambahkan Asiten⚡️", url="http://t.me/asistenmusik2?startgroup=True"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
        "💁🏻‍♂️ apakah kamu ingin mencari lewat YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
