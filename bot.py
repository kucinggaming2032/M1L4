import discord
from bot_logic import *
# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    if message.content.startswith('how are you'):
        await message.channel.send("im fine^_^,how about you?")
    if message.content.startswith('im fine '):
        await message.channel.send("nice^_^,have a nice day:)")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send(message.content)

client.run("MTIxODQyMTQ1NzQ3OTI3NDU1Ng.GCf9Vk.S7vEHhosXobWQglcc7zQIzhZxifXvsF_t2N8JU")
