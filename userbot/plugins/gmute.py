from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio
from AuraXBot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
from telethon import events


@bot.on(admin_cmd(pattern=r"gmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"gmute ?(\d+)?", allow_sudo=True))
async def blowjob(event):
    private = False
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    user_id = reply.sender_id
    if user_id == (await borg.get_me()).id:	
        await edit_or_reply(event, "I guess you need some rest. You are trying to gmute yourself😌")	
        	
        return
    elif event.is_private:
        await edit_or_reply(event, "`𝘽𝙖𝙨 𝙫𝙝𝙪𝙩 𝙗𝙤𝙡 𝙡𝙞𝙮𝙖 𝙖𝙗 𝙩𝙝𝙤𝙙𝙖 𝙧𝙚𝙨𝙩 𝙠𝙖𝙧𝙡𝙤 𝙬𝙖𝙧𝙣𝙖 𝙧𝙚𝙨𝙩 𝙞𝙣 𝙥𝙚𝙖𝙘𝙚 𝙝𝙤 𝙟𝙖𝙤𝙜𝙚...!!💦")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(event, "I need a user to gmute. Please reply or get his uid")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await edit_or_reply(event, "This retard cant speak. Was already gmutted earlier")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "Successfully Fucked this user's mouth.")


@bot.on(admin_cmd(pattern=r"ungmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"ungmute ?(\d+)?", allow_sudo=True))
async def cumshot(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await edit_or_reply(event, "Today's sex done. Now son can speak✌️🚶")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(event, "Please reply to a user or add them into the command to ungmute them.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(event, "𝙏𝙝𝙞𝙨 𝙪𝙨𝙚𝙧 𝙘𝙖𝙣 𝙖𝙡𝙧𝙚𝙖𝙙𝙮 𝙨𝙥𝙚𝙖𝙠 𝙛𝙧𝙚𝙚𝙡𝙮✌️😃")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "Ok! Today's sex is done now. Son can speak🔥🔥")
        
@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
