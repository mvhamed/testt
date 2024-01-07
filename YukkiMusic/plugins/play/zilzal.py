import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["/help", "ميوزك", "/start"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg",
caption=f"""**- اضغـط الـزر بالاسفـل لـ تصفـح اوامـر الميـوزك 🥁**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "Arbic 🇾🇪", callback_data="arbic"
                ),
                ],
            ]
        ),
    )


