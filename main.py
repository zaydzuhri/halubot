import discord
import random

DISCORD_TOKEN = "ODU1ODE4Nzk2MDAxNjU2ODMy.YM4BXQ.buHDJpcUpOJLelVaD3g9zVEuiXk"
client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    if msg.startswith('>'):
        command = msg[1:]
        if command == "hello":
            await message.channel.send("Hello World!!")
        elif command == "random":
            number = random.randrange(100000)
            await message.channel.send(f"Here's your random number: {number}")
            
client.run(DISCORD_TOKEN)