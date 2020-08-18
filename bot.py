import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

# [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
await client.change_presence(status=discord.Status.online)

await client.change_presence(activity=discord.Game(name="관리 하는중"))
#await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
#await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
#await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))

print("파엠커뮤니티:",client.user.name,"697449476603904011:",client.user.id,"1:",discord.__version__)


client.run(os.environ['Njk3NDQ5NDc2NjAzOTA0MDEx.Xo3ccQ.Pcebl-LdA3rVjxD5ijYdYeHIq-E'])













