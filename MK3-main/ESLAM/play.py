from pyrogram import Client, filters
from youtubesearchpython.__future__ import VideosSearch 
import os
import aiohttp
import requests
import random

from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (AlreadyJoinedError,
                                  NoActiveGroupCall,
                                  TelegramServerError)
from pytgcalls.types import (JoinedGroupCallParticipant,
                             LeftGroupCallParticipant, Update)
from config import OWNER
from asyncio import QueueEmpty
 
import asyncio
import yt_dlp
from datetime import datetime, timedelta
from youtube_search import YoutubeSearch
import pytgcalls
from pytgcalls.types.input_stream.quality import (HighQualityAudio,
                                                  HighQualityVideo,
                                                  LowQualityAudio,
                                                  LowQualityVideo,
                                                  MediumQualityAudio,
                                                  MediumQualityVideo)
from typing import Union
from pyrogram import Client, filters 
from pyrogram import Client as client
from pyrogram.errors import (ChatAdminRequired,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (AlreadyJoinedError,
                                  NoActiveGroupCall,
                                  TelegramServerError)
from pytgcalls.types import (JoinedGroupCallParticipant,
                             LeftGroupCallParticipant, Update)

from datetime import datetime
import asyncio
from datetime import datetime, timedelta
from typing import Union

from pyrogram import Client
from pyrogram.errors import (ChatAdminRequired,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (AlreadyJoinedError,
                                  NoActiveGroupCall,
                                  TelegramServerError)
from pytgcalls.types import (JoinedGroupCallParticipant,
                             LeftGroupCallParticipant, Update)
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.stream import StreamAudioEnded
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.stream import StreamAudioEnded
from config import API_ID, API_HASH, MONGO_DB_URL, PHOTO, OWNER, OWNER_NAME, LOGS, GROUP, CHANNEL
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from bot import bot as man
from ESLAM.info import (is_active_chat, db, add, is_served_call, add_active_video_chat, add_served_call, add_active_chat, gen_thumb, download, remove_active, joinch, Call, get_served_users, add_served_user, get_served_chats, add_served_chat, is_served_user, is_served_chat, remove_active_chat)
from ESLAM.Data import (is_autoend, get_logger, get_dev, get_userbot, get_call, get_logger_mode, get_group, get_channel, get_dev_user)
import asyncio
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (AlreadyJoinedError,
                                  NoActiveGroupCall,
                                  TelegramServerError)
from pytgcalls.types import (JoinedGroupCallParticipant,
                             LeftGroupCallParticipant, Update)
             
mongodb = _mongo_client_(MONGO_DB_URL)
pymongodb = MongoClient(MONGO_DB_URL)
Bots = pymongodb.Bots


async def join_assistant(client, chat_id, message_id, userbot, file_path):
        join = None
        try:
            try:                
                user = userbot.me
                user_id = user.id
                get = await client.get_chat_member(chat_id, user_id)
            except ChatAdminRequired:
                await client.send_message(chat_id, f"**قم بترقية البوت مشرف .✘**", reply_to_message_id=message_id)
                get = await client.get_chat_member(chat_id, user_id)
            if get.status == ChatMemberStatus.BANNED:
                await client.send_message(chat_id, f"**قم بالغاء الحظر عن الحساب المساعد لتفعيل البوت**.\n\n @{user.username} : **الحساب المساعد **✘.\n** قم بتنظيف قايمه المستدخمين تمت ازالتهم ✘.**\n\n** @EFFB0T : او تواصل مع المطور من هنا ✘.**", reply_to_message_id=message_id)
            else:
              join = True
        except UserNotParticipant:
            chat = await client.get_chat(chat_id)
            if chat.username:
                try:
                    await userbot.join_chat(chat.username)
                    join = True
                except UserAlreadyParticipant:
                    join = True
                except Exception:
                 try:
                  invitelink = (await client.export_chat_invite_link(chat_id))
                  if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
                  await asyncio.sleep(3)
                  await userbot.join_chat(invitelink)
                  join = True
                 except ChatAdminRequired:
                    return await client.send_message(chat_id, f"**قم اعطاء البوت صلاحيه اضافه المستخدمين عبر الرابط .✘**", reply_to_message_id=message_id)
                 except Exception as e:
                   await client.send_message(chat_id, f"** حدث خطأ حاول مرا آخري لاحقا**\n**{GROUP} : او تواصل مع الدعم من هنا .✘**", reply_to_message_id=message_id)
            else:
                try:
                    try:
                       invitelink = chat.invite_link
                       if invitelink is None:
                          invitelink = (await client.export_chat_invite_link(chat_id))
                    except Exception:
                        try:
                          invitelink = (await client.export_chat_invite_link(chat_id))
                        except ChatAdminRequired:
                          await client.send_message(chat_id, f"**قم اعطاء البوت صلاحيه اضافه مستخدمين عبر الرابط .✘**", reply_to_message_id=message_id)
                        except Exception as e:
                          await client.send_message(chat_id, f"** حدث خطأ حاول مرا آخري لاحقا**\n**{GROUP} : او تواصل مع الدعم من هنا .✘**", reply_to_message_id=message_id)
                    m = await client.send_message(chat_id, "**انتظر قليلاً جاري تفعيل البوت .✘**")
                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
                    await userbot.join_chat(invitelink)
                    join = True
                    await m.edit(f"**{user.mention} : انضم الحساب المساعد **\n**وتم تفعيل البوت يمكنك التشغيل الان .✘**")
                except UserAlreadyParticipant:
                    join = True
                except Exception as e:
                    await client.send_message(chat_id, f"** حدث خطأ حاول مرا آخري لاحقا**\n**{GROUP} : او تواصل مع الدعم من هنا .✘**", reply_to_message_id=message_id)
        return join   
autoend = {}     
AUTO_END_TIME = 5  
async def join_call(
        client,
        message_id,
        chat_id,
        bot_username,
        file_path,
        link,
        vid: Union[bool, str] = None):
        userbot = await get_userbot(bot_username)
        Done = None
        try:
          call = await get_call(bot_username)
        except:
          return Done
        file_path = file_path
        audio_stream_quality = MediumQualityAudio()
        video_stream_quality = MediumQualityVideo()
        stream = (AudioVideoPiped(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) if vid else AudioPiped(file_path, audio_parameters=audio_stream_quality))
        try:
            await call.join_group_call(chat_id, stream, stream_type=StreamType().pulse_stream)
            Done = True
        except NoActiveGroupCall:
                 h = await join_assistant(client, chat_id, message_id, userbot, file_path)
                 if h:
                  try:
                   await call.join_group_call(chat_id, stream, stream_type=StreamType().pulse_stream)
                   Done = True
                  except Exception:
                      await client.send_message(chat_id, "**قم بتشغيل المكالمة أولاً .✘**", reply_to_message_id=message_id)
        except AlreadyJoinedError:
             await client.send_message(chat_id, "**قم بكتابه \n /restart  او  ريستارت او ريلود او /reload \n لاعاده رسترت البوت ثم اعد تشغيل**", reply_to_message_id=message_id)
        except TelegramServerError:
             await client.send_message(chat_id, "**قم بإعادة تشغيل المكالمة ..✘**", reply_to_message_id=message_id)
             if await is_autoend():
              counter[chat_id] = {}
              users = len(await userbot.get_participants(chat_id))
              if users == 1:
                autoend[chat_id] = datetime.now() + timedelta(
                    seconds=AUTO_END_TIME
                )
        except Exception as a:
            print(a)
            return Done
        return Done
from asyncio import Queue as _Queue
from asyncio import QueueEmpty as Empty
from typing import Dict
from asyncio import QueueEmpty

class Queue(_Queue):
    _queue: list = []

    def clear(self):
        self._queue.clear()

queues: Dict[int, Queue] = {}

def clear(chat_id: int):
    if chat_id in queues:
        if queues[chat_id].empty():
            raise Empty
        else:
            queues[chat_id].clear()
    raise Empty
    
def seconds_to_min(seconds):
    if seconds is not None:
        seconds = int(seconds)
        d, h, m, s = (
            seconds // (3600 * 24),
            seconds // 3600 % 24,
            seconds % 3600 // 60,
            seconds % 3600 % 60,
        )
        if d > 0:
            return "{:02d}:{:02d}:{:02d}:{:02d}".format(d, h, m, s)
        elif h > 0:
            return "{:02d}:{:02d}:{:02d}".format(h, m, s)
        elif m > 0:
            return "{:02d}:{:02d}".format(m, s)
        elif s > 0:
            return "00:{:02d}".format(s)
    return "-"


async def logs(bot_username, client, message):
  try:
   if await get_logger_mode(bot_username) == "OFF":
     return
   logger = await get_logger(bot_username)
   log = LOGS
   if message.chat.type == ChatType.CHANNEL:
     chat = f"[{message.chat.title}](t.me/{message.chat.username})" if message.chat.username else message.chat.title
     name = f"{message.author_signature}" if message.author_signature else chat
     text = f"**Playing History **\n\n**Chat : {chat}**\n**Chat Id : {message.chat.id}**\n**User Name : {name}**\n\n**Played : {message.text}**"
   else:
     chat = f"[{message.chat.title}](t.me/{message.chat.username})" if message.chat.username else message.chat.title
     user = f"User Username : @{message.from_user.username}" if message.from_user.username else f"User Id : {message.from_user.id}"
     text = f"**Playing History **\n\n**Chat : {chat}**\n**Chat Id : {message.chat.id}**\n**User Name : {message.from_user.mention}**\n**{user}**\n\n**Played : {message.text}**"
   await client.send_message(logger, text=text, disable_web_page_preview=True)
   return await man.send_message(log, text=f"[ @{bot_username} ]\n{text}", disable_web_page_preview=True)
  except:
    pass    

@Client.on_message(filters.command(["/play", "play", "/vplay", "شغل", "تشغيل", "فيد", "فيديو"], ""))
async def play(client: Client, message):
  if await joinch(message):
            return
  ESLAM = message
  bot_username = client.me.username
  devooo = await get_dev(bot_username)
  DEVUS = await get_dev_user(bot_username)
  chat_id = message.chat.id
  user_id = message.from_user.id if message.from_user else "CMCC3"
  message_id = message.id 
  gr = await get_group(bot_username)
  ch = await get_channel(bot_username)
  button = [[InlineKeyboardButton(text="⸢ 𝙀𝙉𝘿 ⸥", callback_data=f"stop"), InlineKeyboardButton(text="⸢ 𝙍𝙀𝙎𝙐𝙈𝙀 ⸥", callback_data=f"resume"), InlineKeyboardButton(text="⸢ 𝙋𝘼𝙐𝙎𝙀 ⸥", callback_data=f"pause")], [InlineKeyboardButton(text="ᥴ𝗁ᥲ️ꪀꪀᥱᥣ", url=f"{ch}"), InlineKeyboardButton(text="ᘜᖇ᥆υρ", url=f"{gr}")], [InlineKeyboardButton(text=f"{OWNER_NAME}", url=f"https://t.me/{DEVUS}")], [InlineKeyboardButton(text="✘ اضف البوت الي مجموعتك او قناتك ✘", url=f"https://t.me/{bot_username}?startgroup=True")]]
  if message.chat.type == ChatType.PRIVATE:
       return await message.reply_text("**لا يمكنك التشغيل هنا للأسف **\n** قم بإضافة البوت اللي مجموعتك للتشغيل**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"اضف البوت لمجموعتك ✘", url=f"https://t.me/{bot_username}?startgroup=True")]]))
  if message.sender_chat:
     if not message.chat.type == ChatType.CHANNEL:
      return await message.reply_text("**يمكنك التشغيل ب الحساب الشخصي فقط .✘**")
  if not len(message.command) == 1:
    rep = await message.reply_text("**جاري التشغيل انتظر قليلاً ..✘**")
  try:
          call = await get_call(bot_username)
  except:
          await remove_active(bot_username, chat_id)
  try:
       await call.get_call(message.chat.id)
  except pytgcalls.exceptions.GroupCallNotFound:
       await remove_active(bot_username, chat_id)
  if not message.reply_to_message:
     if len(message.command) == 1:
      if message.chat.type == ChatType.CHANNEL:
        return await message.reply_text("**قم بكتابه شي ليتم تشغيله .✘**")
      try:
       name = await client.ask(message.chat.id, text="**عايز تشغل اي ؟**", reply_to_message_id=message.id, filters=filters.user(message.from_user.id), timeout=7)
       name = name.text
       rep = await message.reply_text("**جاري التشغيل انتظر قليلاً ..✘**")
      except:
       return
     else:
       name = message.text.split(None, 1)[1]
     try:
      results = VideosSearch(name, limit=1)
     except Exception:
      return await rep.edit("**لم يتم العثور علي نتائج .✘**")
     for result in (await results.next())["result"]:
         title = result["title"]
         duration = result["duration"]
         videoid = result["id"]
         yturl = result["link"]
         thumbnail = result["thumbnails"][0]["url"].split("?")[0]
     if "v" in message.command[0] or "ف" in message.command[0]:
       vid = True
     else:
       vid = None
     results = YoutubeSearch(name, max_results=5).to_dict()
     link = f"https://youtube.com{results[0]['url_suffix']}"
     if await is_served_call(client, message.chat.id):
         chat_id = message.chat.id
         title = title.title()
         file_path = None
         await add(message.chat.id, bot_username, file_path, link, title, duration, videoid, vid, user_id)
         chat = f"{bot_username}{chat_id}"
         position = len(db.get(chat)) - 1
         chatname = f"[{message.chat.title}](https://t.me/{message.chat.username})" if message.chat.username else f"{message.chat.title}"
         chatname = f"{message.author_signature}" if message.author_signature else chatname
         requester = chatname if ESLAM.views else f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
         if message.from_user:
          if message.from_user.photo:
           ahmed = await client.get_chat(f"{devooo}")
           photo_id = ahmed.photo.big_file_id
           photo = await client.download_media(photo_id)
          elif message.chat.photo:
           photo_id = message.chat.photo.big_file_id
           photo = await client.download_media(photo_id)
          else:
           ahmed = await client.get_chat("EFFB0T")
           ahmedphoto = ahmed.photo.big_file_id
         elif message.chat.photo:
          photo_id = message.chat.photo.big_file_id
          photo = await client.download_media(photo_id)
         else:
          ahmed = await client.get_chat("EFFB0T")
          ahmedphoto = ahmed.photo.big_file_id
          photo = await client.download_media(ahmedphoto)
         photo = await gen_thumb(videoid, photo)
         await message.reply_photo(photo=photo, caption=f"**Add Track To Playlist » {position}**\n\n**Song Name : {title[:18]}**\n**Duration Time : {duration}**\n**Requests By : {requester}**", reply_markup=InlineKeyboardMarkup(button))
         await logs(bot_username, client, message)
     else:
         chat_id = message.chat.id
         title = title.title()
         await add_active_chat(chat_id)
         await add_served_call(client, chat_id)
         if vid:
           await add_active_video_chat(chat_id)
         file_path = await download(bot_username, link, vid)
         await add(message.chat.id, bot_username, file_path, link, title, duration, videoid, vid, user_id)
         c = await join_call(client, message_id, chat_id, bot_username, file_path, link, vid)
         if not c:
            await remove_active(bot_username, chat_id)
            return await rep.delete()
         chatname = f"[{message.chat.title}](https://t.me/{message.chat.username})" if message.chat.username else f"{message.chat.title}"
         chatname = f"{message.author_signature}" if message.author_signature else chatname
         requester = chatname if ESLAM.views else f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
         if message.from_user:
          if message.from_user.photo:
           ahmed = await client.get_chat(f"{devooo}")
           photo_id = ahmed.photo.big_file_id
           photo = await client.download_media(photo_id)
          elif message.chat.photo:
           photo_id = message.chat.photo.big_file_id
           photo = await client.download_media(photo_id)
          else:
           ahmed = await client.get_chat("CMCC3")
           ahmedphoto = ahmed.photo.big_file_id
         elif message.chat.photo:
          photo_id = message.chat.photo.big_file_id
          photo = await client.download_media(photo_id)
         else:
          ahmed = await client.get_chat("CMCC3")
          ahmedphoto = ahmed.photo.big_file_id
          photo = await client.download_media(ahmedphoto)
         photo = await gen_thumb(videoid, photo)
         await message.reply_photo(photo=photo, caption=f"**Starting Playing Now**\n\n**Song Name : {title[:18]}**\n**Duration Time : {duration}**\n**Requests By : {requester}**", reply_markup=InlineKeyboardMarkup(button))
         await logs(bot_username, client, message)
     await rep.delete()
  else:
       if not message.reply_to_message.media:
         return
       rep = await message.reply_text("**جاري تشغيل الملف  ✘**") 
       photo = "Uploaded to https://telegra.ph/file/8d7a59eb9f344f106eb50.jpg"
       if message.reply_to_message.video or message.reply_to_message.document:
           vid = True
       else:
           vid = None
       file_path = await message.reply_to_message.download()
       if message.reply_to_message.audio:
         file_name = message.reply_to_message.audio
       elif message.reply_to_message.voice:
         file_name = message.reply_to_message.voice
       elif message.reply_to_message.video:
         file_name = message.reply_to_message.video
       else:
         file_name = message.reply_to_message.document
       title = file_name.file_name
       duration = seconds_to_min(file_name.duration)
       link = None
       if await is_served_call(client, message.chat.id):
         chat_id = message.chat.id
         videoid = None
         await add(message.chat.id, bot_username, file_path, link, title, duration, videoid, vid, user_id)
         chat = f"{bot_username}{chat_id}"
         position = len(db.get(chat)) - 1
         chatname = f"[{message.chat.title}](https://t.me/{message.chat.username})" if message.chat.username else f"{message.chat.title}"
         chatname = f"{message.author_signature}" if message.author_signature else chatname
         requester = chatname if ESLAM.views else f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
         await message.reply_photo(photo=photo, caption=f"**Add Track To Playlist » {position}**\n\n**Song Name : {title}**\n**Duration Time {duration}**\n**Requests By : {requester}**", reply_markup=InlineKeyboardMarkup(button))
         await logs(bot_username, client, message)
       else:
         chat_id = message.chat.id
         videoid = None
         await add_active_chat(chat_id)
         await add_served_call(client, chat_id)
         if vid:
            await add_active_video_chat(chat_id)
         await add(message.chat.id, bot_username, file_path, link, title, duration, videoid, vid, user_id)
         c = await join_call(client, message_id, chat_id, bot_username, file_path, link, vid)
         if not c:
            await remove_active(bot_username, chat_id)
            return await rep.delete()
         chatname = f"[{message.chat.title}](https://t.me/{message.chat.username})" if message.chat.username else f"{message.chat.title}"
         chatname = f"{message.author_signature}" if message.author_signature else chatname
         requester = chatname if ESLAM.views else f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
         await message.reply_photo(photo=photo, caption=f"**Starting Playing Now**\n\n**Song Name : {title}**\n**Duration Time {duration}**\n**Requests By : {requester}**", reply_markup=InlineKeyboardMarkup(button))
         await logs(bot_username, client, message)
  try:
     os.remove(file_path)
     os.remove(photo)
  except:
     pass
  await rep.delete()    

                             
@Client.on_message(filters.command(["ريستارت", "/restart", "ريلود", "/reload"], "") & filters.group)
async def stop_cmd(c: Client, message):
    bot_username = c.me.username
    devooo = await get_dev(bot_username)
    a = await c.get_chat_member(message.chat.id, message.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.from_user.id == devooo:
       if not message.from_user.username in OWNER:
        return await message.reply_text("**يجب انت تكون ادمن للقيام بذلك  !**")
    bot_username = c.me.username
    call = await get_call(bot_username)
    if message.sender_chat:
        return await message.reply_text(
            "ادمن مجهول\n│\nقم الغاء صلاحيه التخفي."
        )
    chat_id = message.chat.id
    checking = message.from_user.mention
    try:
        clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_chat(chat_id)
    try:
        await call.leave_group_call(chat_id)
    except:
        pass
    await message.reply_text(
        f"تم رسترت هذه المجموعه » {message.chat.title}\n│ ROCK STAR @EFFB0T\nبواسطه » {checking}")
        
@Client.on_message(filters.command(["ريستارت", "/restart", "ريلود", "/reload"], "") & filters.channel)
async def stop_cmmmd(c: Client, message):
    bot_username = c.me.username
    devooo = await get_dev(bot_username)
    bot_username = c.me.username
    call = await get_call(bot_username)
    chat_id = message.chat.id

    try:
        clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_chat(chat_id)
    try:
        await call.leave_group_call(chat_id)
    except:
        pass
    await message.reply_text(
        f"تم رسترت هذه المجموعه » {message.chat.title}\n│ ROCK STAR @EFFB0T")
        

    
    
