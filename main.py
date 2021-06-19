import discord
import random
import os
from dotenv import load_dotenv

load_dotenv('.env')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

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
        command = msg[1:].lower()
        if command == "hello":
            await message.channel.send("Hello World!")
        elif command == "random":
            number = random.randrange(100000)
            await message.channel.send(f"Here's your random number: {number}")
        elif command == "nyan":
            nyan_len = random.randrange(1, 10)
            nyan = "nya"
            for i in range(nyan_len):
                nyan += "a"
            nyan += "n!"
            await message.channel.send(f"{nyan}")

client.run(DISCORD_TOKEN)