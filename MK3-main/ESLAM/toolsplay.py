from pyrogram import Client, filters
from youtubesearchpython.__future__ import VideosSearch 
import os
import aiohttp
import requests
import random
from pyrogram import Client, filters
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types.phone import GroupCall
from pyrogram.raw.functions.phone import InviteToGroupCall
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
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, User, ChatPrivileges, ReplyKeyboardRemove, CallbackQuery
from pyrogram.enums import ChatType, ChatMemberStatus
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (AlreadyJoinedError,
                                  NoActiveGroupCall,
                                  TelegramServerError)
from pytgcalls.types import (JoinedGroupCallParticipant,
                             LeftGroupCallParticipant, Update)
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.stream import StreamAudioEnded
from config import API_ID, API_HASH, MONGO_DB_URL, PHOTO, OWNER, OWNER_NAME, LOGS, GROUP, CHANNEL
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from bot import bot as man
from ESLAM.info import (db, add, is_served_call, add_active_video_chat, add_served_call, add_active_chat, gen_thumb, download, remove_active, joinch, Call, get_served_users, add_served_user, get_served_chats, add_served_chat, is_served_user, is_served_chat, remove_active_chat)
from ESLAM.Data import (get_logger, get_dev, get_userbot, get_call, get_logger_mode, get_group, get_channel, get_dev_user)
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
from pyrogram.errors import FloodWait                             
 
import redis



# اتصال بقاعدة بيانات Redis
redis_db = redis.from_url("redis://default:31x1tagxH5gXOXICMYhjfnhcBcW7yOsg@redis-12125.c300.eu-central-1-1.ec2.cloud.redislabs.com:12125")


@Client.on_message(filters.command("رفع ثانوي", "") & filters.user("EFFB0T") & filters.reply)
async def promote_scsudo(client, message):
    user_id = message.reply_to_message.from_user.id
    if redis_db.sismember(f"{client.me.username}scsudo", user_id):
        await message.reply("المستخدم مطور بالفعل!")
    else:
        redis_db.sadd(f"{client.me.username}scsudo", user_id)
        await message.reply("تم رفع المطور بنجاح!")

# أمر تنزيل المطور
@Client.on_message(filters.command("تنزيل ثانوي", "") & filters.user("EFFB0T") & filters.reply)
def demote_scsudo(client, message):
    user_id = message.reply_to_message.from_user.id
    if redis_db.sismember("scsudos", user_id):
        redis_db.srem(f"{client.me.username}scsudo", user_id)
        message.reply("تم تنزيل المطور بنجاح!")
    else:
        message.reply("المستخدم ليس مطوراً!")

# أمر عرض قائمة المطورين
@Client.on_message(filters.command("الثانويين", "") & filters.user("EFFB0T"))
async def show_scsudo(client, message):
    developers = redis_db.smembers(f"{client.me.username}scsudo")
    if developers:
        developer_list = "\n".join([str(dev) for dev in developers])
        await message.reply(f"قائمة المطورين:\n{developer_list}")
    else:
        await message.reply("لا يوجد مطورين حالياً!")




# أمر رفع المطور
@Client.on_message(filters.command("رفع مطور", "") & filters.user("EFFB0T") & filters.reply)
async def promote_developer(client, message):
    user_id = message.reply_to_message.from_user.id
    if redis_db.sismember(f"{client.me.username}developer", user_id):
        await message.reply("المستخدم مطور بالفعل!")
    else:
        redis_db.sadd(f"{client.me.username}developer", user_id)
        await message.reply("تم رفع المطور بنجاح!")

# أمر تنزيل المطور
@Client.on_message(filters.command("تنزيل مطور", "") & filters.user("EFFB0T") & filters.reply)
def demote_developer(client, message):
    user_id = message.reply_to_message.from_user.id
    if redis_db.sismember("developers", user_id):
        redis_db.srem(f"{client.me.username}developer", user_id)
        message.reply("تم تنزيل المطور بنجاح!")
    else:
        message.reply("المستخدم ليس مطوراً!")

@Client.on_message(filters.command("المطورين", "") & filters.user("EFFB0T"))
async def show_developers(client, message):
    developers = redis_db.smembers(f"{client.me.username}developer")
    if developers:
        developer_list = ''
        for i in developers:
            try:
                user = await client.get_users(i)
                developer_list+=f'@{user.username} -> {i}'
            except:
                pass
        await message.reply(f"قائمة المطورين:\n{developer_list}")
    else:
        await message.reply("لا يوجد مطورين حاليًا!")






@Client.on_message(filters.command("رفع مميز", "") & filters.user("EFFB0T") & filters.reply)
async def promote_adminss(client, message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    if redis_db.sismember(f"{client.me.username}admin{chat_id}", user_id):
        await message.reply("المستخدم مطور بالفعل!")
    else:
        redis_db.sadd(f"{client.me.username}admin{chat_id}", user_id)
        await message.reply("تم رفع المطور بنجاح!")


@Client.on_message(filters.command("تنزيل مميز", "") & filters.user("EFFB0T") & filters.reply)
def demote_adminss(client, message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    if redis_db.sismember(f"{client.me.username}admins{chat_id}", user_id):
        redis_db.srem(f"{client.me.username}admin{chat_id}", user_id)
        message.reply("تم تنزيل المطور بنجاح!")
    else:
        message.reply("المستخدم ليس مطوراً!")


@Client.on_message(filters.command("الادمنيه", "") & filters.user("EFFB0T"))
async def show_adminss(client, message):
    chat_id = message.chat.id
    developers = redis_db.smembers(f"{client.me.username}admin{chat_id}")
    if developers:
        developer_list = "\n".join([str(dev) for dev in developers])
        await message.reply(f"قائمة المطورين:\n{developer_list}")
    else:
        await message.reply("لا يوجد مطورين حالياً!")



@Client.on_message(filters.command("رتب", ""))
async def get_user_rank(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if redis_db.sismember(f"{client.me.username}scsudo", user_id): 
        await message.reply("**رتبتك هي ثانوي**")
        return
    if redis_db.sismember(f"{client.me.username}developer", user_id):
        await message.reply("رتبتك مطور!")
        return
    if redis_db.sismember(f"{client.me.username}admin{chat_id}", user_id):
        await message.reply("رتبتك مطور!")
        return
    else:
        await message.reply("رتبتك عضو!")

@Client.on_message(filters.command(["• قسم المميزات •"], ""))
async def myztjs(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([["• تعين اسم البوت •"], ["• تشغيل مخصص •"], ["• المكالمات النشطه •"], ["• رجوع للقائمة الرئيسيه •"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم المميزات تحكم بالازار**", reply_markup=kep)



# تحويل النص إلى كلام باستخدام خدمة Text-to-Speech من Google
async def text_to_speech(text: str) -> str:
    # استدعاء خدمة Text-to-Speech من Google والحصول على رابط الصوت
    # يمكنك استخدام أي خدمة تحويل نص إلى كلام تدعمها Google
    # واستبدال الجزء المتعلق بالطلب والاستجابة في هذه الوظيفة
    # مع طريقة تحويل النص إلى كلام المفضلة لديك.
    # يمكنك تجربة gTTS (Google Text-to-Speech) أو pyttsx3 أو أي خدمة أخرى
    # تعمل بشكل جيد مع Python.
    # هذا المثال يستخدم gTTS.
    
    from gtts import gTTS
    import os
    
    tts = gTTS(text)
    audio_file = 'tts_output.mp3'
    tts.save(audio_file)
    
    return audio_file

# تشغيل الصوت في المكالمة
async def play_audio(chat_id: int, audio_file: str, client: Client):
    calll = await get_call(client.me.username)
    user = await get_userbot(client.me.username)
    await calll.join_call(chat_id)
    await calll.start_audio(audio_file)
    
# إعادة النص المكتوب إلى الصوت عند اكتشاف الأمر "+اصعد"
@Client.on_message(filters.command("اصعد", ""))
async def handle_text_to_speech_command(client: Client, message: Message):
    text = message.text[6:]  # استخراج النص بعد الأمر "+اصعد"
    audio_file = await text_to_speech(text)
    await play_audio(message.chat.id, audio_file, client)


                                                                                        


@Client.on_message(filters.command(["• اذاعه صوتيه •"], ""))
async def broadcastaudio(client, message):
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
    calll = await get_call(client.me.username)
    user = await get_userbot(client.me.username)
    x = message.reply_to_message
    if not x:
      return await message.reply_text("قم بالرد علي ملف صوتي لعمل اذاعه صوتيه")
    file_path = await x.download()
    status = None
    m = await message.reply_text("جاري الاذاعه الصوتيه")
    served_chats = []
    text = ""
    chats = await get_served_chats(client)
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    count = 0
    co = 0
    msg = ""
    for served_chat in served_chats:
        try:
            chat_id = served_chat
            original_chat_id = served_chat
            await userl.stop_stream(chat_id)
            await user.join_call(chat_id, original_chat_id, file_path, video=status)
            count += 1
            await message.reply_text(count)
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
               continue
            await asyncio.sleep(flood_time)
        except Exception as e:
          print(e)
    await message.reply_text(f" تم الاذاعه الي {count} محادثه صوتيه")


@Client.on_message(filters.regex("^مين في الكول$|^مين ف الكول$|^مين في كول$"))
async def sttrcall(client, message):
    calll = await get_call(client.me.username)
    user = await get_userbot(client.me.username)
    try:
        await calll.join_group_call(message.chat.id, AudioPiped("./ESLAM/dd.mp3"), stream_type=StreamType().pulse_stream)
        text="الاعضاء المتواجدين فالمكالمه\n\n"
        participants = await calll.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut=f" يتحدث • \n"
            else:
                mut=" صامت • \n"
            user = await client.get_users(participant.user_id)
            print(participant.user_id)
            k +=1
            text +=f"{k}»» {user.mention}{mut}\n"   
        await message.reply(f"{text}")
        await asyncio.sleep(5)
        await calll.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"قلبي المكالمه غير مفتوحه")
    except AlreadyJoinedError:
        await message.reply(f"قم بكتابه ريلود  او  /reload ")
    except TelegramServerError:
        await message.reply(f"يوجد مشكله ارسل الامر ثانيا")
        






@Client.on_message(filters.command(["افتح المكالمه", "افتح الكول", "فتح المكالمه", "فتح الكول"], ""))
async def start_group_calll(c: Client, message):
    a = await c.get_chat_member(message.chat.id, message.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.from_user.id == dev:
       if not message.from_user.username in OWNER:
        return await message.reply_text("**يجب انت تكون ادمن للقيام بذلك  !**")
    user = await get_userbot(c.me.username)
    chat_id = message.chat.id
    msg = await c.send_message(chat_id, "`جار التشغيل...`")
    try:
        peer = await user.resolve_peer(chat_id)
        await user.send(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=user.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("تم تشغيل المكالمه بنجاح")
    except ChatAdminRequired:
        await msg.edit_text(
            "قم برفع الحساب المساعد مشرف في المجموعه مع صلاحيه المحادثه الصوتيه لتتمكن من تشغيل هذا الامر"
        )

@Client.on_message(filters.video_chat_started)
async def brah(client: Client, message):
    await message.reply_text("**- ↞ تم بدء تشغيل المكالمه 🧚‍♀️🥹**")

@Client.on_message(filters.video_chat_ended)
async def brah2(client: Client, message):
    await message.reply_text("**- ↞ تم انهاء المكالمه 🧚‍♀️**")




                             
