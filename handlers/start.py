from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""**HELLO!**, Saya  **š¼į“¬įµā±½ā»į“®įµį¶»į¶» į“¹įµĖ¢į“µį¶ š¼**, Adalah bot untuk memutar musik dalam obrolan suara group chat anda.\n\nš§ Jangan lupa untuk menambahkan asisten musik juga, agar dapat memutar musiknya. š§\n\n|| /help untuk mengetahui perintah ||""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support š§", url="https://t.me/Kabaridevbot_bot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Creator š±ļø", url="https://t.me/psycho_syridwan"
                    ),
                    InlineKeyboardButton(
                        "Group š§", url="https://t.me/ossuport"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        "Tambahkan bot ke Group š§ļø", url="http://t.me/auvbuzzbot?startgroup=true"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        "Tambahkan Asiten š§ļø", url="http://t.me/asistenmusik2?startgroup=True"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
        "šš»āāļø apakah kamu ingin mencari lewat YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ā Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ā", callback_data="close"
                    )
                ]
            ]
        )
    )
