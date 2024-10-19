import random
from pyrogram import Client, filters
from pyrogram import Client as app
from time import time
from config import OWNER, OWNER_NAME, VIDEO
from ESLAM.info import (is_served_chat, add_served_chat, is_served_user, add_served_user, get_served_chats, get_served_users, del_served_chat, joinch)
from ESLAM.Data import (get_dev, get_dev_name, get_bot_name, set_bot_name, get_logger, get_group, get_channel, get_groupsr, get_channelsr, get_userbot, set_dev_user, get_dev_user, get_video_source, set_video_source, get_msg_start, set_msg_start)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, User, ChatPrivileges, ReplyKeyboardRemove, CallbackQuery
from pyrogram import enums
from pyrogram.errors import FloodWait
from pyrogram.enums import ChatType, ChatMemberStatus, ChatMembersFilter
import os
import re
import textwrap
import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch





@Client.on_message(filters.command(["• قسم الحقوق •", "• رجوع •"], ""))
async def casttt(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([["• تعين مطور السورس •"], ["• تعين صوره السورس •"], ["• تعين مجموعة السورس •", "• تعين قناة السورس •"], ["• تعين قناة البوت •", " تعين مجموعة البوت •"], ["• رجوع للقائمة الرئيسيه •"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الحقوق تحكم بالازار**", reply_markup=kep)

@Client.on_message(filters.command("• تعين اسم البوت •", ""))
async def set_bot(client: Client, message):
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل اسم البوت الجديد", filters=filters.text, timeout=30)
   BOT_NAME = NAME.text
   bot_username = client.me.username
   await set_bot_name(bot_username, BOT_NAME)
   await message.reply_text("**تم تعين اسم البوت بنجاح -✘**")

@Client.on_message(filters.command("• تعين رساله ستارت •", ""))
async def set_msgg_startt(client: Client, message):
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 if message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل رساله ستارت الجديده", filters=filters.text, timeout=30)
   MSG_START = NAME.text
   bot_username = client.me.username
   await set_msg_start(bot_username, MSG_START)
   await message.reply_text("**تم تعين رساله ستارت بنجاح -✘**")




@Client.on_message(filters.command("• تعين صوره السورس •", ""))
async def set_vi_so(client: Client, message):
 bot_username = client.me.username
 if message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل رابط صوره السورس \nمثال:-\n https://t.me/anmii288/113", filters=filters.text, timeout=30)
   VID_SO = NAME.text
   await set_video_source(bot_username, VID_SO)
   await message.reply_text("**تم تعين صوره السورس  بنجاح -✘**")
   
   
   
@Client.on_message(filters.command("• تعين مطور السورس •", ""))
async def set_dev_username(client: Client, message):
 bot_username = client.me.username
 if message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل معرف المطور بدون @", filters=filters.text, timeout=30)
   CH_DEV_USER = NAME.text
   bot_username = client.me.username
   await set_dev_user(bot_username, CH_DEV_USER)
   await message.reply_text("**تم تعين مطور السورس بنجاح -✘**")   