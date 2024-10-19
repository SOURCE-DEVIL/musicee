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


@Client.on_message(filters.command(["• قسم الاحصائيات •"], ""))
async def statskes3(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([["• الاحصائيات •"], ["• المجموعات •", "• المستخدمين •"], ["• رجوع للقائمة الرئيسيه •"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاحصائيات تحكم بالازار**", reply_markup=kep)


@Client.on_message(filters.command(["الاحصائيات", "• الاحصائيات •"], ""))
async def analysis(client: Client, message: Message):
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
   chats = len(await get_served_chats(client))
   user = len(await get_served_users(client))
   return await message.reply_text(f"**✅ احصائيات البوت**\n**⚡ المجموعات {chats} مجموعة  **\n**⚡ المستخدمين {user} مستخدم**")

@Client.on_message(filters.command(["• المجموعات •"], ""))
async def chats_func(client: Client, message: Message):
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
    m = await message.reply_text("⚡")
    served_chats = []
    text = ""
    chats = await get_served_chats(client)
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    count = 0
    co = 0
    msg = ""
    for served_chat in served_chats:
        if f"{served_chat}" in text:
          await del_served_chat(client, served_chat)
        else:
         try:
            chat = await client.get_chat(served_chat)
            title = chat.title
            username = chat.username
            count += 1
            txt = f"{count}:- Chat : [{title}](https://t.me/{username}) Id : `{served_chat}`\n" if username else f"{count}:- Chat : {title} Id : `{served_chat}`\n"
            text += txt
         except Exception:
            title = "Not Found" 
            count += 1
            text += f"{count}:- {title} {served_chat}\n"
    if count == 0:
      return await m.edit("الاحصائيات صفر 🤔")
    else:
      try:
        await message.reply_text(text, disable_web_page_preview=True)
      except: 
         link = await base(text)
         await message.reply_text(link)
      return await m.delete()



@Client.on_message(filters.command(["• المستخدمين •"], ""))
async def users_func(client: Client, message: Message):
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
    m = await message.reply_text("⚡")
    served_chats = []
    text = ""
    chats = await get_served_users(client)
    for chat in chats:
        served_chats.append(int(chat["user_id"]))
    count = 0
    co = 0
    msg = ""
    for served_chat in served_chats:
        if f"{served_chat}" in text:
           await del_served_user(client, served_chat)
        else:
         try:
            chat = await client.get_chat(served_chat)
            title = chat.first_name
            username = chat.username
            count += 1
            txt = f"{count}:- Chat : [{title}](https://t.me/{username}) Id : `{served_chat}`\n" if username else f"{count}:- Chat : {title} Id : `{served_chat}`\n"
            text += txt
         except Exception:
            title = "Not Found" 
            count += 1
            text += f"{count}:- {title} {served_chat}\n"
    if count == 0:
      return await m.edit("الاحصائيات صفر 🤔")
    else:
      try:
        await message.reply_text(text, disable_web_page_preview=True)
      except: 
         link = await base(text)
         await message.reply_text(link)
      return await m.delete()