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


@Client.on_message(
    filters.command(["/alive", "معلومات", "سورس", "السورس", "࿈ السورس ࿈", "• السورس •"], "")
)
async def alive(client: Client, message):
    bot_username = client.me.username
    LINK_SOURCEE = await get_video_source(bot_username)
    ch = await get_channel(bot_username)
    gr = await get_group(bot_username)
    bot_username = client.me.username
    DEVUS = await get_dev_user(bot_username)
    chat_id = message.chat.id

    keyboard = InlineKeyboardMarkup(
        [
            [ 
                 InlineKeyboardButton("اضف البوت الي مجموعتك ❤️", url="https://t.me/{app.username}?startgroup=true")
            ]
        ]
    )

    alive = f""""""

    await message.reply_photo(
        photo=f"{LINK_SOURCEE}",
        caption=alive,
        reply_markup=keyboard,
    )

@Client.on_message(filters.command(["/ping", "بنج"], ""))
async def ping_pong(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")
