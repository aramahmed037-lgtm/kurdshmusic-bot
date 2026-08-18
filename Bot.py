import logging
import os
import time
from pyrogram import Client, filters
from pyrogram.types import Message
from YukkiMusic import app
from YukkiMusic.Helpers import get_url, get_music

logging.basicConfig(level=logging.INFO)

@app.on_message(filters.command("play") & filters.group)
async def play_music(client: Client, message: Message):
    try:
        query = message.text.split(" ", 1)[1]
    except IndexError:
        await message.reply_text("لە تکایە ناوی گۆرانی بڵێ")
        return
    
    try:
        await message.reply_text(f"🔍 گەڕان بۆ: {query}")
        url = get_url(query)
        music = await get_music(url)
        await message.reply_text(f"🎵 ئێستا لەدەنگدان: {music.title}")
    except Exception as e:
        await message.reply_text(f"❌ هەڵە: {e}")
