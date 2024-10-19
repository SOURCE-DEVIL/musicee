from pyrogram import Client, filters, raw, utils
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message
from config import logger as log, logger_mode as logm, OWNER
from ESLAM.info import (get_served_chats, get_served_users, del_served_chat, del_served_user, activecall, add_active_chat, add_served_call, add_active_video_chat)
from ESLAM.Data import Bots
from ESLAM.play import (logs, join_call)
from ESLAM.Data import (get_userbot, get_dev, get_call, get_group, get_channel)
import aiohttp
import asyncio
from datetime import datetime
from pyrogram.errors import FloodWait
from pyrogram import enums
from typing import Union, List, Iterable

BASE = "https://batbin.me/"


async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data


async def base(text):
    resp = await post(f"{BASE}api/v2/paste", data=text)
    if not resp["success"]:
        return
    link = BASE + resp["message"]
    return link




@Client.on_message(filters.command("• المكالمات النشطه •", ""))
async def geetmeactive(client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   m = await message.reply_text("**جاري جلب المكالمات النشطه ..🚦**")
   count = 0
   text = ""
   for i in activecall[client.me.username]:
       try:
          chat = await client.get_chat(i)
          count += 1
          text += f"{count}- [{chat.title}](https://t.me/{chat.username}) : {chat.id}" if chat.username else f"{chat.title} : {chat.id}"
       except Exception:
            title = "Not Found" 
            count += 1
            text += f"{count}:- {title} {chat.id}\n"
   if count == 0:
      return await m.edit(" لا يوجد مكالمات نشطه الان 🤔")
   else:
      try:
        await message.reply_text(text, disable_web_page_preview=True)
      except: 
         link = await base(text)
         await message.reply_text(link)
      return await m.delete()


@Client.on_message(filters.command(["• قسم السجل •"], ""))
async def sgel27(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([["• تغير مكان سجل التشغيل •"], ["• تفعيل سجل التشغيل •"], ["• تعطيل سجل التشغيل •"], ["• رجوع للقائمة الرئيسيه •"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم السجل تحكم بالازار**", reply_markup=kep)


@Client.on_message(filters.command(["• تغير مكان سجل التشغيل •", "• تفعيل سجل التشغيل •", "• تعطيل سجل التشغيل •"], ""))
async def set_history(client: Client, message):
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
  if message.command[0] == "• تغير مكان سجل التشغيل •":
   ask = await client.ask(message.chat.id, "** قم بارسال يوزرنيم أو ايدي الذي تريد تعيينه **", timeout=30)
   logger = ask.text
   if "@" in logger:
     logger = logger.replace("@", "")
  Botts = Bots.find({})
  for i in Botts:
      bot = client.me
      if i["bot_username"] == bot.username:
        dev = i["dev"]
        token = i["token"]
        session = i["session"]
        bot_username = i["bot_username"]
        loogger = i["logger"]
        logger_mode = i["logger_mode"]
        if message.command[0] == "• تغير مكان سجل التشغيل •":
         if i["logger"] == logger:
           return await ask.reply_text("**هذا هو مكان السجل بالفعل .⚡**")
         else:
          try:
           user = await get_userbot(bot_username)
           await client.send_message(logger, "**جاري الفحص ...**")
           await user.send_message(logger, "**جاري تغير مكان السجل ..**")
           d = {"bot_username": bot_username}
           Bots.delete_one(d)
           asyncio.sleep(2)
           aha = {"bot_username": bot_username, "token": token, "session": session, "dev": dev, "logger": logger, "logger_mode": logger_mode}
           Bots.insert_one(aha)
           log[bot_username] = logger
           await ask.reply_text("**تم تغير سجل التشغيل بنجاح ✅**")
          except Exception:
            await ask.reply_text("**تاكد من اضافه البوت والمساعد وترقيتهم مشرف**")
        else:
         mode = "ON" if message.command[0] == "• تفعيل سجل التشغيل •" else "OFF"
         if i["logger_mode"] == mode:
           m = "مفعل" if message.command[0] == "• تفعيل سجل التشغيل •" else "معطل"
           return await message.reply_text(f"**سجل التشغيل {m} من قبل .⚡**")
         else:
          try:
           hh = {"bot_username": bot_username}
           Bots.delete_one(hh)
           h = {"bot_username": bot_username, "token": token, "session": session, "dev": dev, "logger": loogger, "logger_mode": mode}
           Bots.insert_one(h)
           logm[bot_username] = mode
           m = "تفعيل" if message.command == "• تفعيل سجل التشغيل •" else "تعطيل"
           await message.reply_text(f"**تم {m} سجل التشغيل بنجاح ✅**")
          except Exception as es:
            await message.reply_text("**حدث خطأ راسل المطور ..**")
