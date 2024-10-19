from config import API_ID, API_HASH, MONGO_DB_URL, user, dev, call, logger, logger_mode, botname, GROUP as GROUPOWNER, CHANNEL as CHANNELOWNER, OWNER, OWNER_NAME
from pymongo import MongoClient
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, User, ChatPrivileges, ReplyKeyboardRemove, CallbackQuery
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_

mo = MongoClient()
mo = MongoClient(MONGO_DB_URL)
moo = mo["data"]
Bots = moo.simo
onoffdb = moo.onoffper
bot_name = moo.bot_name
dev_userr = moo.dev_userr
devuserr = {}
vid_so = moo.vid_so
vidso = {}
channeldb = moo.ch
CHANNEL = {}
groupdb = moo.gr
GROUP = {}
channeldbsr = moo.chsr
CHANNELsr = {}
groupdbsr = moo.grsr
GROUPsr = {}
msg_start = moo.msg_start
msgstart = {}
autoenddb = moo.autoend
autoend = {}
botss = Bots
dev = moo.dev
dev = {}
devname = {}
boot = {}
mustdb = moo.must
must = {}
sub_yn = moo.sub_yn
subyn = {}

def dbb():
    global db
    db = {}

dbb()

async def is_autoend() -> bool:
    chat_id = 123
    mode = autoend.get(chat_id)
    if not mode:
        user = await autoenddb.find_one({"chat_id": chat_id})
        if not user:
            autoend[chat_id] = False
            return False
        autoend[chat_id] = True
        return True
    return mode


# Developer Id
async def get_dev(bot_username):
  devv = dev.get(bot_username)
  if not devv:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         devo = i["dev"]
         dev[bot_username] = devo
         return devo
  return devv
async def force_stop_stream(chat_id: int):
        assistant = await get_userbot(chat_id, bot_username)
        try:
            check = db.get(chat_id)
            check.pop(0)
        except:
            pass
        await remove_active_video_chat(chat_id)
        await remove_active_chat(chat_id)
        try:
            await assistant.leave_group_call(chat_id)
        except:
            pass

# Developer Name
async def get_dev_name(client, bot_username):
  devv = devname.get(bot_username)
  if not devv:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         devo = i["dev"]
         devo = await client.get_chat(devo)
         devo = devo.first_name
         devname[bot_username] = devo
         return devo
  return devv


async def get_sudoers(bot_username) -> list:
    sudoers = sudoersdb.find_one({"sudo": "sudo"})
    if not sudoers:
        return []
    return sudoers["sudoers"]


async def add_sudo(bot_username, user_id: int) -> bool:
    sudoers = await get_sudoers(bot_username)
    sudoers.append(user_id)
    sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True


async def remove_sudo(bot_username, user_id: int) -> bool:
    sudoers = await get_sudoers(bot_username)
    sudoers.remove(user_id)
    sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True


async def get_for_s(bot_username):
      name = subyn.get(bot_username)
      if not name:
        subb = sub_yn.find_one({"bot_username": bot_username})
        if not subb:
            return "تعطيل"
        subyn[bot_username] = subb["sub_yn"]
        return subb["sub_yn"]
      return name

async def set_for_s(bot_username: dict, SUB_YN: str):
    subyn[bot_username] = SUB_YN
    sub_yn.update_one({"bot_username": bot_username}, {"$set": {"sub_yn": SUB_YN}}, upsert=True)



# Bot Name
async def get_bot_name(bot_username):
      name = botname.get(bot_username)
      if not name:
        bot = bot_name.find_one({"bot_username": bot_username})
        if not bot:
            return "لولا"
        botname[bot_username] = bot["bot_name"]
        return bot["bot_name"]
      return name

async def set_bot_name(bot_username: dict, BOT_NAME: str):
    botname[bot_username] = BOT_NAME
    bot_name.update_one({"bot_username": bot_username}, {"$set": {"bot_name": BOT_NAME}}, upsert=True)

#تعين رساله ستارت

async def get_msg_start(bot_username):
      DEVUS = await get_dev_user(bot_username)
      name = msgstart.get(bot_username)
      if not name:
        msg = msg_start.find_one({"bot_username": bot_username})
        if not msg:
            return "𝗁ᥱᥣᥣ᥆, ꪔY υ᥉ᥱᖇ ᖴᖇᎥᥱꪀժ, Ꭵ ᥲ️ꪔ ᥲ️ Ⴆ᥆ƚ ƚ𝗁ᥲ️ƚ ρᥣᥲ️Y᥉ ᥉᥆ꪀᘜ᥉ ƚ᥆ ᖴᎥꪀժ ᥆υƚ 𝗁᥆᭙ Y᥆υ ᥴᥲ️ꪀ υ᥉ᥱ ꪔᥱ ᥴ𝗁᥆᥆᥉ᥱ ƚ𝗁ᥱ ᥣᥲ️ꪀᘜυᥲ️ᘜᥱ Y᥆υ ᭙ᥲ️ꪀƚ ƚ᥆ ᥉ρᥱᥲ️k Ꭵꪀ ᥲ️ꪀժ ƚ𝗁ᥱꪀ ᥴ𝗁᥆᥆᥉ᥱ ƚ𝗁ᥱ ƚ𝗁Ꭵꪀᘜ Y᥆υ ᭙ᥲ️ꪀƚ 💕"
        msgstart[bot_username] = msg["msg_start"]
        return msg["msg_start"]
      return name

async def set_msg_start(bot_username: dict, MSG_START: str):
    msgstart[bot_username] = MSG_START
    msg_start.update_one({"bot_username": bot_username}, {"$set": {"msg_start": MSG_START}}, upsert=True)
 

 
#تعين فيديو السورس


async def get_video_source(bot_username):
      name = vidso.get(bot_username)
      if not name:
        vid = vid_so.find_one({"bot_username": bot_username})
        if not vid:
            return "https://telegra.ph/file/8d7a59eb9f344f106eb50.jpg"
        vidso[bot_username] = vid["vid_so"]
        return vid["vid_so"]
      return name

async def set_video_source(bot_username: dict, VID_SO: str):
    vidso[bot_username] = VID_SO
    vid_so.update_one({"bot_username": bot_username}, {"$set": {"vid_so": VID_SO}}, upsert=True)
  
 
 
 
 
#تغير يوزر خاص بمطور السورس 
 
async def get_dev_user(bot_username):
      name = devuserr.get(bot_username)
      if not name:
        dev = dev_userr.find_one({"bot_username": bot_username})
        if not dev:
            return "LLL3P"
        devuserr[bot_username] = dev["dev_userr"]
        return dev["dev_userr"]
      return name

async def set_dev_user(bot_username: dict, DEV_USERR: str):
    devuserr[bot_username] = DEV_USERR
    dev_userr.update_one({"bot_username": bot_username}, {"$set": {"dev_userr": DEV_USERR}}, upsert=True)



# Bot group
async def get_group(bot_username):
      name = GROUP.get(bot_username)
      if not name:
        bot = groupdb.find_one({"bot_username": bot_username})
        if not bot:
            return GROUPOWNER 
        GROUP[bot_username] = bot["group"]
        return bot["group"]
      return name

async def set_group(bot_username: dict, group: str):
    GROUP[bot_username] = group
    groupdb.update_one({"bot_username": bot_username}, {"$set": {"group": group}}, upsert=True)

# Bot channel
async def get_channel(bot_username):
      name = CHANNEL.get(bot_username)
      if not name:
        bot = channeldb.find_one({"bot_username": bot_username})
        if not bot:
            return CHANNELOWNER 
        CHANNEL[bot_username] = bot["channel"]
        return bot["channel"]
      return name

async def set_channel(bot_username: dict, channel: str):
    CHANNEL[bot_username] = channel
    channeldb.update_one({"bot_username": bot_username}, {"$set": {"channel": channel}}, upsert=True)


# sr group
async def get_groupsr(bot_username):
      name = GROUPsr.get(bot_username)
      if not name:
        bot = groupdbsr.find_one({"bot_username": bot_username})
        if not bot:
            return GROUPOWNER 
        GROUPsr[bot_username] = bot["groupsr"]
        return bot["groupsr"]
      return name

async def set_groupsr(bot_username: dict, groupsr: str):
    GROUPsr[bot_username] = groupsr
    groupdbsr.update_one({"bot_username": bot_username}, {"$set": {"groupsr": groupsr}}, upsert=True)

# sr channel
async def get_channelsr(bot_username):
      name = CHANNELsr.get(bot_username)
      if not name:
        bot = channeldbsr.find_one({"bot_username": bot_username})
        if not bot:
            return CHANNELOWNER
        CHANNELsr[bot_username] = bot["channelsr"]
        return bot["channelsr"]
      return name

async def set_channelsr(bot_username: dict, channelsr: str):
    CHANNELsr[bot_username] = channelsr
    channeldbsr.update_one({"bot_username": bot_username}, {"$set": {"channelsr": channelsr}}, upsert=True)

@Client.on_message(filters.command("• تعين قناة البوت •", ""))
async def set_botch(client: Client, message):
  if message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل رابط القناه البوت الجديدة", filters=filters.text)
   channel = NAME.text
   bot_username = client.me.username
   await set_channel(bot_username, channel)
   await message.reply_text("**تم تعين قناه البوت بنجاح -🖱️**")
   return

@Client.on_message(filters.command("• تعين مجموعة البوت •", ""))
async def set_botgr(client: Client, message):
  if message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل رابط الجروب الجديد", filters=filters.text)
   group = NAME.text
   bot_username = client.me.username
   await set_group(bot_username, group)
   await message.reply_text("**تم تعين مجموعه البوت بنجاح -🖱️**")
   return


@Client.on_message(filters.command("• تعين قناة السورس •", ""))
async def set_botchsr(client: Client, message):
  if message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل رابط القناه البوت الجديدة", filters=filters.text)
   channelsr = NAME.text
   bot_username = client.me.username
   await set_channelsr(bot_username, channelsr)
   await message.reply_text("**تم تعين قناه السورس بنجاح -🖱️**")
   return

@Client.on_message(filters.command("• تعين مجموعة السورس •", ""))
async def set_botgrsr(client: Client, message):
  if message.chat.username in OWNER:
   NAME = await client.ask(message.chat.id, "ارسل رابط الجروب الجديد", filters=filters.text)
   groupsr = NAME.text
   bot_username = client.me.username
   await set_groupsr(bot_username, groupsr)
   await message.reply_text("**تم تعين مجموعه السورس بنجاح -🖱️**")
   return


#Mongo db
async def get_data(client):
   mongodb = _mongo_client_(MONGO_DB_URL)
   bot_username = client.me.username
   mongodb = mongodb[bot_username]
   return mongodb


# Assistant Client
async def get_userbot(bot_username):
  userbot = user.get(bot_username)
  if not userbot:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         session = i["session"]
         userbot = Client("ESLAM", api_id=API_ID, api_hash=API_HASH, session_string=session)
         user[bot_username] = userbot
         return userbot
  return userbot

# Call Client
async def get_call(bot_username):
  calll = call.get(bot_username)
  if not calll:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         userbot = await get_userbot(bot_username)
         callo = PyTgCalls(userbot, cache_duration=100)
         await callo.start()
         call[bot_username] = callo
         return callo
  return calll

# app Client
async def get_app(bot_username):
  app = boot.get(bot_username)
  if not app:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         token = i["token"]
         app = Client("ESLAM", api_id=API_ID, api_hash=API_HASH, bot_token=token, plugins=dict(root="ESLAM"))
         boot[bot_username] = app
         return app
  return calll


# Logger
async def get_logger(bot_username):
  loggero = logger.get(bot_username)
  if not loggero:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         loggero = i["logger"]
         logger[bot_username] = loggero
         return loggero
  return loggero


async def get_logger_mode(bot_username):
  logger = logger_mode.get(bot_username)
  if not logger:
   Bots = botss.find({})
   for i in Bots:
       bot = i["bot_username"]
       if bot == bot_username:
         logger = i["logger_mode"]
         logger_mode[bot_username] = logger
         return logger
  return logger

async def must_join(bot_username):
      name = must.get(bot_username)
      if not name:
        bot = mustdb.find_one({"bot_username": bot_username})
        if not bot:
            return "معطل"
        must[bot_username] = bot["getmust"]
        return bot["getmust"]
      return name

async def set_must(bot_username: dict, m: str):
    if m == "• تعطيل الاشتراك الإجباري •":
      ii = "معطل"
    else:
      ii = "مفعل"
    must[bot_username] = ii
    mustdb.update_one({"bot_username": bot_username}, {"$set": {"getmust": ii}}, upsert=True)


@Client.on_message(filters.command(["• قسم الاشتراك الاجباري •"], ""))
async def eshy3(client: Client, message):
   bot_username = client.me.username
   if message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([["• تفعيل الاشتراك الإجباري •"], ["• تعطيل الاشتراك الإجباري •"], ["• رجوع للقائمة الرئيسيه •"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاشتراك الاجباري تحكم بالازار**", reply_markup=kep)


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
