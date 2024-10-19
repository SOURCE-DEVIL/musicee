from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from pyrogram.enums import ChatMemberStatus

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
