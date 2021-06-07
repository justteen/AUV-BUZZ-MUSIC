from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""❤ Perintah dan cara menggunakan ❤
**Untuk Semua Group**
- `/play <song name>` - play lagu yang direquest
- `/dplay <song name>` - play lagu yang direquest via deezer
- `/splay <song name>` - play lagu yang direquest via jio saavn
- `/playlist` - Menampilkan lagu yang akan diputar
- `/current` - Menampilkan yang sedang diputar
- `/song <song name>` - download lagu
- `/search <query>` - mencari lagu melalui youtube
- `/deezer <song name>` - download lagu via deezer
- `/saavn <song name>` - download lagu via saavn
- `/video <song name>` - download video

**Admins only**
- `/player` - membuka pengaturan musik
- `/pause` - menjeda pemutaran
- `/resume` - memainkan ulang
- `/skip` - skip lagu berikutnya
- `/end` - stop pemutaran
- `/userbotjoin` - mengundang asisten bot musik
- `/userbotleave` - mengeluarkan asisten musik bot
- `/admincache` - Refresh admin""")

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""❤ Perintah dan cara menggunakan ❤
**Untuk Semua Group**
- `/play <song name>` - play lagu yang direquest
- `/dplay <song name>` - play lagu yang direquest via deezer
- `/splay <song name>` - play lagu yang direquest via jio saavn
- `/playlist` - Menampilkan lagu yang akan diputar
- `/current` - Menampilkan yang sedang diputar
- `/song <song name>` - download lagu
- `/search <query>` - mencari lagu melalui youtube
- `/deezer <song name>` - download lagu via deezer
- `/saavn <song name>` - download lagu via saavn
- `/video <song name>` - download video

**Admins only**
- `/player` - membuka pengaturan musik
- `/pause` - menjeda pemutaran
- `/resume` - memainkan ulang
- `/skip` - skip lagu berikutnya
- `/end` - stop pemutaran
- `/userbotjoin` - mengundang asisten bot musik
- `/userbotleave` - mengeluarkan asisten musik bot
- `/admincache` - Refresh admin""")
