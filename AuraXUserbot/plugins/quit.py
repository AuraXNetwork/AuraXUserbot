"""
.kickme
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest
from AuraXUserbot import *
from AuraXBot.utils import *
from AuraXBot.utils import sudo_cmd

from AuraXBot.utils import admin_cmd


@borg.on(admin_cmd("kickme", outgoing=True))
@bot.on(sudo_cmd("kickme", allow_sudo=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**I Iz lev this Kensur grp**")
        time.sleep(1)
        if "-" in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("**Iz this even a grp???**")
