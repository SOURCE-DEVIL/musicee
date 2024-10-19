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




@Client.on_message(filters.command(["• قسم الإذاعة •", "• رجوع •"], ""))
async def cast(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.id == dev or message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([["• اذاعه عام •"], ["• اذاعه للمجموعات •", "• اذاعه للمستخدمين •"], ["• توجيه عام •"], ["• توجيه للمجموعات •", "• توجيه للمستخدمين •"], ["• رجوع للقائمة الرئيسيه •"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)



@Client.on_message(filters.command(["• اذاعه عام •", "• اذاعه للمجموعات •", "• اذاعه للمستخدمين •", "• توجيه عام •", "• توجيه للمستخدمين •", "• توجيه للمجموعات •"], ""))
async def cast1(client: Client, message):
   command = message.command[0]
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.id == dev or message.chat.username in OWNER:
    if command == "• اذاعه عام •":
     kep = ReplyKeyboardMarkup([["• اذاعه عام بالبوت •"], ["• اذاعه عام بالمساعد •"], ["• رجوع •"]], resize_keyboard=True)
     await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)
    elif command == "• اذاعه للمجموعات •":
     kep = ReplyKeyboardMarkup([["• اذاعه للمجموعات بالبوت •"], ["• اذاعه للمجموعات بالمساعد •"], ["• رجوع •"]], resize_keyboard=True)
     await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)
    elif command == "• اذاعه للمستخدمين •":
     kep = ReplyKeyboardMarkup([["• اذاعه للمستخدمين بالبوت •"], ["• اذاعه للمستخدمين بالمساعد •"], ["• رجوع •"]], resize_keyboard=True)
     await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)
    elif command == "• توجيه عام •":
     kep = ReplyKeyboardMarkup([["• توجيه عام بالبوت •"], ["• رجوع •"]], resize_keyboard=True)
     await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)
    elif command == "• توجيه للمستخدمين •":
     kep = ReplyKeyboardMarkup([["• توجيه للمستخدمين بالبوت •"], ["• رجوع •"]], resize_keyboard=True)
     await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)
    else:
     kep = ReplyKeyboardMarkup([["• توجيه للمجموعات بالبوت •"], ["• رجوع •"]], resize_keyboard=True)
     await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)


@Client.on_message(filters.command(["• اذاعه عام بالبوت •", "• اذاعه عام بالمساعد •", "• اذاعه للمجموعات بالبوت •", "• اذاعه للمجموعات بالمساعد •", "• اذاعه للمستخدمين بالبوت •", "• اذاعه للمستخدمين بالمساعد •", "• توجيه عام بالبوت •", "• توجيه عام بالمساعد •", "• توجيه للمجموعات بالبوت •", "• توجيه للمجموعات بالمساعد •", "• توجيه للمستخدمين بالبوت •", "• توجيه للمستخدمين بالمساعد •"], ""))
async def cast5(client: Client, message):
  command = message.command[0]
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   kep = ReplyKeyboardMarkup([["• الغاء •"], ["• رجوع •"], ["• رجوع للقائمة الرئيسيه •"]], resize_keyboard=True)
   ask = await client.ask(message.chat.id, "قم بإرسال الاذاعه الخاصه بك", reply_markup=kep)
   x = ask.id
   y = message.chat.id
   if ask.text == "• الغاء •":
     return await ask.reply_text("**تم الالغاء بنجاح ✅**")
   pn = await client.ask(message.chat.id, "هل تريد تثبيت الاذاعه\nارسل « نعم » او « لا »")
   await message.reply_text("**جاري الاذاعه انتظر بعض الوقت ..⚡**")
   text = ask.text
   dn = 0
   fd = 0
   if command == "• اذاعه عام بالبوت •":
     chats = await get_served_chats(client)
     users = await get_served_users(client)
     chat = []
     for user in users:
         chat.append(int(user["user_id"]))
     for c in chats:
         chat.append(int(c["chat_id"]))
     for i in chat:
         try:
           m = await client.send_message(chat_id=i, text=text)
           dn += 1
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
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "• اذاعه عام بالمساعد •":
     user = await get_userbot(bot_username)
     async for i in user.get_dialogs():
         try:
           m = await user.send_message(chat_id=i.chat.id, text=text)
           dn += 1
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
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "• اذاعه للمجموعات بالبوت •":
     chats = await get_served_chats(client)
     chat = []
     for c in chats:
         chat.append(int(c["chat_id"]))
     for i in chat:
         try:
           m = await client.send_message(chat_id=i, text=text)
           dn += 1
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
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "• اذاعه للمجموعات بالمساعد •":
     user = await get_userbot(bot_username)
     async for i in user.get_dialogs():
         if not i.chat.type == enums.ChatType.PRIVATE:
          try:
           m = await user.send_message(chat_id=i.chat.id, text=text)
           dn += 1
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
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "• اذاعه للمستخدمين بالبوت •":
     chats = await get_served_users(client)
     chat = []
     for c in chats:
         chat.append(int(c["user_id"]))
     for i in chat:
         try:
           i = i
           m = await client.send_message(chat_id=i, text=text)
           dn += 1
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
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "• اذاعه للمستخدمين بالمساعد •":
     client = await get_userbot(bot_username)
     async for i in client.get_dialogs():
         if i.chat.type == enums.ChatType.PRIVATE:
          try:
           m = await client.send_message(chat_id=i.chat.id, text=text)
           dn += 1
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
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "• توجيه عام بالبوت •":
     chats = await get_served_chats(client)
     users = await get_served_users(client)
     chat = []
     for user in users:
         chat.append(int(user["user_id"]))
     for c in chats:
         chat.append(int(c["chat_id"]))
     for i in chat:
         try:
           m = await client.forward_messages(i, y, x)
           dn += 1
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
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "• توجيه عام بالمساعد •":
     client = await get_userbot(bot_username)
     async for i in client.get_dialogs():
         try:
           m = await client.forward_messages(
               chat_id=i.chat.id,
               from_chat_id=message.chat.username,
               message_ids=int(x),
               )
           dn += 1
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
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "• توجيه للمجموعات بالبوت •":
     chats = await get_served_chats(client)
     chat = []
     for user in chats:
         chat.append(int(user["chat_id"]))
     for i in chat:
         try:
           m = await client.forward_messages(i, y, x)
           dn += 1
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
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "• توجيه للمجموعات بالمساعد •":
     client = await get_userbot(bot_username)
     async for i in client.get_dialogs():
         if not i.chat.type == enums.ChatType.PRIVATE:
          try:
           m = await client.forward_messages(i.chat.id, y, x)
           dn += 1
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
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "• توجيه للمستخدمين بالبوت •":
     chats = await get_served_users(client)
     chat = []
     for c in chats:
         chat.append(int(c["user_id"]))
     for i in chat:
         try:
           m = await client.forward_messages(i, y, x)
           dn += 1
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
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "• توجيه للمستخدمين بالمساعد •":
     client = await get_userbot(bot_username)
     async for i in client.get_dialogs():
         if i.chat.type == enums.ChatType.PRIVATE:
          try:
           m = await client.forward_messages(i.chat.id, y, x)
           dn += 1
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
          except:
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .⚡**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")    
