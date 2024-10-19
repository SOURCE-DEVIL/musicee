import random
from pyrogram import Client, filters
from pyrogram import Client as app
from time import time
from config import OWNER, OWNER_NAME, VIDEO
from ESLAM.info import (is_served_chat, add_served_chat, is_served_user, add_served_user, get_served_chats, get_served_users, del_served_chat, joinch)
from ESLAM.Data import (get_dev, get_dev_name, get_bot_name, set_bot_name, get_logger, get_group, get_channel, get_groupsr, get_channelsr, get_userbot, set_dev_user, get_dev_user, get_video_source, set_video_source, get_msg_start, set_msg_start, get_for_s, set_for_s)
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


@Client.on_message(filters.command(["صاحب السورس", "اسلام", "سيمو", "المبرمج", "࿈ مبرمج السورس ࿈"], ""))
async def deev1(client: Client, message: Message):
     user = await client.get_chat("EFFB0T")
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`")
     except:
       pass
     await message.reply_photo(
     photo=photo,
     caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
        

@Client.on_message(filters.command(["المطور", "مطور", "࿈ المطور ࿈"], ""))
async def dev(client: Client, message: Message):
     bot_username = client.me.username
     dev = await get_dev(bot_username)
     user = await client.get_chat(dev)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور الأساسي**\n{chat_title}\nChat Id : `{message.chat.id}`")
     except:
        pass
     await message.reply_photo(
     photo=photo,
     caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass


@Client.on_message(filters.command(["• قسم التفعيل و التعطيل •"], ""))
async def tfeel3(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([["• تفعيل التواصل •", "• تعطيل التواصل •"], ["• تفعيل البوت بالصوره •", "• تعطيل البوت بالصوره •"], ["• رجوع للقائمة الرئيسيه •"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم التفعيل و التعطيل تحكم بالازار**", reply_markup=kep)


        
OFFPV = []

@Client.on_message(filters.command(["• تفعيل التواصل •", "• تعطيل التواصل •"], ""))
async def byyye(client, message):
    user = message.from_user.username
    dev = await get_dev(client.me.username)
    if user in OWNER or message.from_user.id == dev:
        text = message.text
        if text == "• تفعيل التواصل •":
          if not client.me.username in OFFPV:
             await message.reply_text("**التواصل مفعل من قبل .**")
          try:
            OFFPV.remove(client.me.username)
            await message.reply_text("تم تفعيل التواصل ✅")
            return
          except:
             pass
        if text == "• تعطيل التواصل •":
          if client.me.username in OFFPV:
             await message.reply_text("**التواصل معطل من قبل .**")
          try:
            OFFPV.append(client.me.username)
            await message.reply_text("تم تعطيل التواصل ✅")
            return
          except:
             pass

@Client.on_message(filters.command(["• تفعيل البوت بالصوره •"], ""))
async def byyggfye(client, message):
    bot_username = client.me.username
    user = message.from_user.username
    dev = await get_dev(client.me.username)
    if user in OWNER or message.from_user.id == dev:
         ADD_SUB = "تفعيل"
         await set_for_s(bot_username, ADD_SUB)
         await message.reply_text("**تم تفعيل البوت بالصوره .**")

@Client.on_message(filters.command(["• تعطيل البوت بالصوره •"], ""))
async def bycgfye(client, message):
    bot_username = client.me.username
    user = message.from_user.username
    dev = await get_dev(client.me.username)
    if user in OWNER or message.from_user.id == dev:
          ADD_SUB = "تعطيل"
          await set_for_s(bot_username, ADD_SUB)
          await message.reply_text("**تم تعطيل البوت بالصوره**")
        
@Client.on_message(filters.private)
async def botoot(client: Client, message: Message):
 if not client.me.username in OFFPV:
  if await joinch(message):
            return
  bot_username = client.me.username
  user_id = message.chat.id
  if not await is_served_user(client, user_id):
     await add_served_user(client, user_id)
  dev = await get_dev(bot_username)
  if message.from_user.id == dev or message.chat.username in OWNER or message.from_user.id == client.me.id:
    if message.reply_to_message:
     u = message.reply_to_message.forward_from
     try:
       await client.send_message(u.id, text=message.text)
       await message.reply_text(f"**تم ارسال رساتلك إلي {u.mention} بنجاح .☕ **")
     except Exception:
         pass
  else:
   try:
    await client.forward_messages(dev, message.chat.id, message.id)
    await client.forward_messages(OWNER[0], message.chat.id, message.id)
   except Exception as e:
     pass
 message.continue_propagation()

@Client.on_message(filters.new_chat_members)
async def welcome(client: Client, message):
   try:
    bot = client.me
    bot_username = bot.username
    if message.new_chat_members[0].username == "EFFB0T" or message.new_chat_members[0].username == "ll_NU":
      try:
         chat_id = message.chat.id
         user_id = message.new_chat_members[0].id
         await client.promote_chat_member(chat_id, user_id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(chat_id, user_id, "• اسلام •")
      except:
        pass
      return await message.reply_text(f"**انضم اسلام الكبير  الي هنا الان [.](https://t.me/EFFB0T)⚡**\n\n**يرجي من الاعضاء احترام وجوده 🥷**")
    dev = await get_dev(bot_username)
    if message.new_chat_members[0].id == dev:
      try:
         await client.promote_chat_member(message.chat.id, message.new_chat_members[0].id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(message.chat.id, message.new_chat_members[0].id, "• مطور البوت •")
      except:
        pass
      return await message.reply_text(f"**انضم مالك البوت الي هنا ❤️**\n**{message.new_chat_members[0].mention} : مرحبا بك **")
    mid = message.from_user.id
    if message.new_chat_members[0].id == mid:
      return await message.reply_text(f"**• لآ تسـيئ آللفظ وآن ضـآق بــك آلرد️**\n**ꪀᥲ️ꪔᥱ:- {message.new_chat_members[0].mention}\nυ᥉ᥱᖇ:- @{message.new_chat_members[0].username}\nᎥժ:- {message.new_chat_members[0].id} **")      
    if message.new_chat_members[0].id == bot.id:
      photo = bot.photo.big_file_id
      photo = await client.download_media(photo)
      chat_id = message.chat.id
      nn = await get_dev_name(client, bot_username)
      ch = await get_channel(bot_username)
      gr = await get_group(bot_username)
      button = [[InlineKeyboardButton(text="𝗖𝗵𝗮𝗻𝗻𝗲𝗹 ✘", url=f"{ch}"), InlineKeyboardButton(text="𝗚𝗿𝗼𝘂𝗽 ✘", url=f"{gr}")], [InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")],  [InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ⚡", url=f"https://t.me/{bot.username}?startgroup=True")]]
      await message.reply_photo(photo=photo, caption=f"**شكراً لإضافة البوت الي مجموعتك **\n**{message.chat.title} : تم تفعيل البوت في مجموعتك **\n**يمكنك الان تشغيل ما تريده .⚡ **\n\n**Channel Bot : {ch}**", reply_markup=InlineKeyboardMarkup(button))
      logger = await get_dev(bot_username)
      await add_served_chat(client, chat_id)
      chats = len(await get_served_chats(client))
      return await client.send_message(logger, f"New Group : [{message.chat.title}](https://t.me/{message.chat.username})\nId : {message.chat.id} \nBy : {message.from_user.mention} \nGroup Now: {chats}", disable_web_page_preview=True)
   except:
      pass
       
@Client.on_message(filters.left_chat_member)
async def bot_kicked(client: Client, message):
    bot = client.me
    bot_username = bot.username
    if message.left_chat_member.id == bot.id:
         logger = await get_dev(bot_username)
         chat_id = message.chat.id
         await client.send_message(logger, f"**Bot Is Kicked**\n**{message.chat.title}**\n**Id : `{message.chat.id}`**\n**By :** {message.from_user.mention}")
         return await del_served_chat(client, chat_id)

@Client.on_message(filters.command(["تفعيل"], "") & ~filters.private)
async def pipong(client: Client, message: Message):
   if len(message.command) == 1:
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    await message.reply_text("تم تفعيل البوت بنجاح ✅")
    return 

@Client.on_message(~filters.private)
async def booot(client: Client, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(client, chat_id):
       try:
        await add_served_chat(client, chat_id)
        chats = len(await get_served_chats(client))
        bot_username = client.me.username
        dev = await get_dev(bot_username)
        username = f"https://t.me/{message.chat.username}" if message.chat.username else None
        mention = message.from_user.mention if message.from_user else message.chat.title
        await client.send_message(dev, f"**تم تفعيل محادثة جديدة تلقائياً واصبحت {chats} محادثة**\nNew Group : [{message.chat.title}]({username})\nId : {message.chat.id} \nBy : {mention}", disable_web_page_preview=True)
        await client.send_message(chat_id, f"**تم تشغيل البوت بنجاح ايها العضو اللطيف 🧚‍♀️**")
        return 
       except:
          pass
    message.continue_propagation()

############################################################################################################################################################################################################################################################################################
############################################################################################################################################################################################################################################################################################
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from pyrogram.types import ForceReply,ChatPrivileges,InlineKeyboardButton,InlineKeyboardMarkup
from pyromod import listen

welcome_enabled = True

@Client.on_chat_member_updated()
async def welcome(client, chat_member_updated):
    if not welcome_enabled:
        return
    if str(chat_member_updated.new_chat_member.status) == "ChatMemberStatus.BANNED":
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user
        
        if kicked_by is not None and kicked_by.is_self:
            messagee = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة بواسطة البوت"
        else:
            if kicked_by is not None:
                message = f"• المستخدم [{user.first_name}](tg://user?id={user.id}) \n• تم طرده من الدردشة بواسطة [{kicked_by.first_name}](tg://user?id={kicked_by.id})\n• ولقد طردته بسبب هذا"
                try:
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                except Exception as e:
                    message += f"\n\nعذرًا، لم استطع حظر الإداري بسبب: {str(e)}"
            else:
                message = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة"
                await client.send_message(chat_member_updated.chat.id, message)
                
                
#f = filters.create(lambda _, __, message: "رفع ادمن" in message.text)
#@Client.on_message(f & filters.group)
#async def promote_by_id(client, message):
#    chat_id = message.chat.id
#    text = message.text.split()
#    
#    if len(text) == 3 and text[0] == "رفع" and text[1] == "مشرف":
#        try:
#            user_id = str(text[2])
#            await client.promote_chat_member(
#            chat_id,
#            user_id,
#            ChatPrivileges(
#            can_manage_chat=True,
#            can_delete_messages=True,
#            can_manage_video_chats=True,
#            can_restrict_members=True,
#            can_promote_members=True,
 #           can_change_info=True,
  #          can_post_messages=False,
   #         can_edit_messages=False,
    #        can_invite_users=True,
     #       can_pin_messages=True,
      #      is_anonymous=False
       #         )
        #    )
         #   await message.reply("تم رفع العضو مشرف بنجاح")
        #except ValueError:
         #   await message.reply("اكتب الايدي عدل يعلق")
            
            
@Client.on_message(filters.command("رفع مشرف",""),filters.group)
async def UhjAdmin(client, message):
	UserID = message.reply_to_message.from_user.id
	ChatID = message.chat.id
	
	Can_C = False
	Can_D = False
	Can_I = False
	Can_R = False
	Can_P = False
	Can_MV = False
	Can_PR = False
	
	R = await message.chat.get_member(message.from_user.id)
	
	if R.status == ChatMemberStatus.OWNER or R.status == ChatMemberStatus.ADMINISTRATOR:
		ask = await message.chat.ask("⇜ تمام الحين ارسل صلاحيات المشرف \n\n1 ⇠ صلاحيه تغيير المعلومات\n2 ⇠ صلاحيه حذف الرسائل\n3 ⇠ صلاحيه دعوه مستخدمين\n4 ⇠ صلاحيه حظر وتقيد المستخدمين \n5 ⇠ صلاحيه تثبيت الرسائل \n6 ⇠ صلاحيه ادارة المكالمات\n7 ⇜ صلاحيه رفع مشرفين اخرين\n* ⇠ لرفع كل الصلاحيات ما عدا رفع المشرفين \n** ⇠ لرفع كل الصلاحيات مع رفع المشرفين \n\n⇜ يمديك تختار الارقام مع بعض  \n\nمثال: 136 \n༄",
		reply_markup=ForceReply(),filters=filters.text)
		TexT = ask.text
		
		if str("1") in TexT:
			Can_C = True
		if str("2") in TexT:
			Can_D = True
		if str("3") in TexT:
			Can_I = True
		if str("4") in TexT:
			Can_R = True
		if str("5") in TexT:
			Can_P = True
		if str("6") in TexT:
			Can_MV = True
		if str("7") in TexT:
			Can_PR = True
		if str("*") in TexT:
			Can_C = True
			Can_D = True
			Can_I = True
			Can_R = True
			Can_P = True
			Can_MV = True
		if str("**") in TexT:
			Can_C = True
			Can_D = True
			Can_I = True
			Can_R = True
			Can_P = True
			Can_MV = True
			Can_PR = True
		try:
			await client.promote_chat_member(
			chat_id=ChatID,
			user_id=UserID,
			privileges=ChatPrivileges(
		    can_promote_members=Can_PR,
		    can_manage_video_chats=Can_MV,
		    can_pin_messages=Can_P,
		    can_invite_users=Can_I,
		    can_restrict_members=Can_R,
		    can_delete_messages=Can_D,
		    can_change_info=Can_C))
		except Exception as e:
			return await message.reply(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
			
		if any(i in ask.text for i in ['1','2','3', '4', '5', '6','7','*','**']):
			return await message.reply(f"**•「{message.from_user.mention}」\nتم رفعته مشرف**",reply_markup=
			InlineKeyboardMarkup
			([[InlineKeyboardButton(
			message.reply_to_message.from_user.first_name,
			user_id=
			message.reply_to_message.from_user.id)]]))
		else:
			return await message.reply("اتكلم بعدين و ارفع مشرف")
	
	else:
		return await message.reply("هذا الامر للمشرفين فقط")
            

@Client.on_message(filters.command("رفع ادمن", "") & filters.channel)
async def tom(client, message):
 user_id =  ' '.join(message.text.split()[2:])
 chat_id = message.chat.id
 await client.promote_chat_member(chat_id, user_id, ChatPrivileges(can_manage_chat=True))
 await message.reply("تم رفعه")
async def get_member_status(chat_id, user_id):
    member = await app.get_chat_member(chat_id, user_id)
    if member.status == "ChatMemberStatus.OWNER":
        return "Owner"
    elif member.status == "ChatMemberStatus.ADMINISTRATOR":
        return "Administrator"
    elif member.status == "ChatMemberStatus.MEMBER":
        return "Member"
    elif member.status == "ChatMemberStatus.RESTRICTED":
        return "Restricted"
    elif member.status == "ChatMemberStatus.LEFT":
        return "Left"
    elif member.status == "ChatMemberStatus.BANNED":
        return "Banned"
    else:
        return "Unknown"            