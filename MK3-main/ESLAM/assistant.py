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



@Client.on_message(filters.command("• قسم التحكم في المساعد •", ""))
async def helpercn(client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   userbot = await get_userbot(bot_username)
   me = userbot.me
   i = f"@{me.username} : {me.id}" if me.username else me.id
   b = await client.get_chat(me.id)
   b = b.bio if b.bio else "لا يوجد بايو"
   if message.chat.id == dev or message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([["• فحص المساعد •"], ["• تغير الاسم الاول •", "• تغير الاسم التاني •"], ["• تغير البايو •"], ["• تغير اسم المستخدم •"], ["• اضافه صوره •", "• ازالة الصور •"], ["• دعوه المساعد الي الانضمام •"], ["• رجوع للقائمة الرئيسيه •"]], resize_keyboard=True)
    await message.reply_text(f"**أهلا بك عزيزي المطور **\n**هنا قسم الحساب المساعد**\n**{me.mention}**\n**{i}**\n**{b}**", reply_markup=kep)
   


@Client.on_message(filters.command("• فحص المساعد •", ""))
async def userrrrr(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.id == dev or message.chat.username in OWNER:
    client = await get_userbot(bot_username)
    mm = await message.reply_text("Collecting stats")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = client.me
    usere = Meh.mention
    async for dialog in client.get_dialogs():
        type = dialog.chat.type
        if enums.ChatType.PRIVATE == type:
            u += 1
        elif enums.ChatType.BOT == type:
            b += 1
        elif enums.ChatType.GROUP == type:
            g += 1
        elif enums.ChatType.SUPERGROUP == type:
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status == enums.ChatMemberStatus.ADMINISTRATOR or user_s.status == enums.ChatMemberStatus.OWNER:
                a_chat += 1
        elif enums.ChatType.CHANNEL == type:
            c += 1
        else:
          print(type)

    end = datetime.now()
    ms = (end - start).seconds
    await mm.edit_text(
        """**ꜱᴛᴀᴛꜱ ꜰᴇᴀᴛᴄʜᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ ⚡**
⚡**ʏᴏᴜ ʜᴀᴠᴇ {} ᴘʀɪᴠᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ᴄʜᴀɴɴᴇʟꜱ.**
🏷️**ʏᴏᴜ ᴀʀᴇ ᴀᴅᴍɪɴꜱ ɪɴ {} ᴄʜᴀᴛꜱ.**
🏷️**ʙᴏᴛꜱ ɪɴ ʏᴏᴜʀ ᴘʀɪᴠᴀᴛᴇ = {}**
⚠️**ꜰᴇᴀᴛᴄʜᴇᴅ ʙʏ ᴜꜱɪɴɢ {} **""".format(
            ms, u, g, sg, c, a_chat, b, usere
        )
    )

@Client.on_message(filters.command("• تغير الاسم الاول •", ""))
async def changefisrt(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    name = await client.ask(message.chat.id, "• ارسل الان الاسم الجديد •")
    name = name.text
    client = await get_userbot(bot_username)
    await client.update_profile(first_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح .⚡**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم \n {es}")


@Client.on_message(filters.command("• تغير الاسم التاني •", ""))
async def changelast(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    name = await client.ask(message.chat.id, "• ارسل الان الاسم الجديد •")
    name = name.text
    client = await get_userbot(bot_username)
    await client.update_profile(last_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح .⚡**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم \n {es}")


@Client.on_message(filters.command("• تغير البايو •", ""))
async def changebio(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    name = await client.ask(message.chat.id, "• ارسل الان البايو الجديد •")
    name = name.text
    client = await get_userbot(bot_username)
    await client.update_profile(bio=name)
    await message.reply_text("**تم تغير البايو بنجاح .⚡**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير البايو \n {es}")


@Client.on_message(filters.command("• تغير اسم المستخدم •", ""))
async def changeusername(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    name = await client.ask(message.chat.id, "• ارسل الان اسم المستخدم الجديد •")
    name = name.text
    client = await get_userbot(bot_username)
    await client.set_username(name)
    await message.reply_text("**تم تغير اسم المستخدم بنجاح .⚡**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير اسم المستخدم \n {es}")


@Client.on_message(filters.command(["• اضافه صوره •"], ""))
async def changephoto(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    m = await client.ask(message.chat.id, "قم بإرسال الصوره الجديده الان")
    photo = await m.download()
    client = await get_userbot(bot_username)
    await client.set_profile_photo(photo=photo)
    await message.reply_text("**تم تغير صوره الحساب المساعد بنجاح .⚡**") 
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الصوره \n {es}")

@Client.on_message(filters.command(["• ازاله صوره •"], ""))
async def changephotos(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
       try:
        client = await get_userbot(bot_username)
        photos = await client.get_profile_photos("me")
        await client.delete_profile_photos([p.file_id for p in photos[1:]])
        await message.reply_text("**تم ازاله صوره بنجاح .⚡**")
       except Exception as es:
         await message.reply_text(f" حدث خطأ أثناء ازاله الصوره \n {es}")


@Client.on_message(filters.command("• دعوه المساعد الي الانضمام •", ""))
async def joined(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    name = await client.ask(message.chat.id, "• ارسل الان الرابط •")
    name = name.text
    if "https" in name:
     if not "+" in name: 
       name = name.replace("https://t.me/", "")
    client = await get_userbot(bot_username)
    await client.join_chat(name)
    await message.reply_text("**تم انضمام الحساب المساعد بنجاح .⚡**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء الانضمام \n {es}")
