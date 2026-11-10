
import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")
WELCOME_CHANNEL_ID = 1569379483020959935

intents = discord.Intents.default()
intents.members = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if channel:
        message = (
            f"୨୧・₊✧ **WELCOME, {member.mention}!!** ♡\n\n"
            "Hiii!! So happy to have you here! ദ്ദി ˉ͈̀꒳ˉ͈́ )✧\n\n"
            "This little community was created by **Nini**, "
            "a small Roblox streamer!\n"
            "Find her at **@colignda** on Roblox. 🎀\n\n"
            "Make yourself at home and have fun!! 🌷"
        )
        await channel.send(message)

bot.run(TOKEN)
