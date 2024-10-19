from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen


bot = Client(
    "mo",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    BMBB4 = "anas55555555555"
    await bot.send_message(BMBB4, "**تم تفعيل بنجاح يا انس باشا**")
    print("[INFO]: الموعلم اسلام")
    await idle()
