import random
from pyrogram import Client, filters
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



        
@Client.on_message(filters.command(["/start"], ""))
async def startpvVv(client: Client, message):
 if message.chat.type == enums.ChatType.PRIVATE:
    if await joinch(message):
            return
 bot_username = client.me.username
 MSGSTART = await get_msg_start(bot_username)
 dev = await get_dev(bot_username)
 nn = await get_dev_name(client, bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
   await message.reply_text("**لعرض كيب المطور الخاص بالميوزك قم بارسال \n\n /rock**")
@Client.on_message(filters.command(["/rock", "• رجوع للقائمة الرئيسيه •"], ""))
async def statrt(client: Client, message):
 if not message.chat.type == enums.ChatType.PRIVATE:
    if await joinch(message):
            return
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 nn = await get_dev_name(client, bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
   kep = ReplyKeyboardMarkup([["• حذف الكيبورد •"], ["• السورس •"], ["• قسم الحقوق •", "• قسم المميزات •"], ["• قسم الاشتراك الاجباري •"], ["• قسم الاحصائيات •"], ["• قسم الإذاعة •"], ["• قسم التحكم في المساعد •"], ["• قسم السجل •"], ["• قسم التفعيل و التعطيل •"]], resize_keyboard=True)
   await message.reply_text("**مرحباً بك عزيزي المطور**\n**يمكنك التحكم ف البوت من خلال الازرار**", reply_markup=kep)


    
@Client.on_message(filters.regex("࿈ حذف الكيبورد ࿈"))
async def down(client: Client, message):
    m = await message.reply("**تم حذف كيبورد الميوزك بنجاح \n اكتب /rock  لو بدك يظهر ثاني **", reply_markup= ReplyKeyboardRemove(selective=True))        