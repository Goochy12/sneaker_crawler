import discord
import asyncio

import sneaker_code

sneakers = []
changes = False
channel = None

raffle_message_true = "\U0001F911" + ' Raffles Live! ' + "\U0001F911"
raffle_message_false = "No Raffles!"
raffle_message_current = ""

client = discord.Client()

async def check_sneakers():
    global channel
    while True:
        print("LOOPING")
        changes = sneaker_code.checkForChanges()

        if changes["changes"] == True:
            if channel != None:
                await channel.send("New Sneakers Available")
            pass
        if changes["raffle"] == True:
            raffle_message_current = raffle_message_true
        else:
            raffle_message_current = raffle_message_false

        print(changes["changes"])
        print(changes["raffle"])
        print(raffle_message_current)

        await client.change_presence(activity=discord.Game(name=raffle_message_current))

        await asyncio.sleep(30)

@client.event
async def on_message(message):
    global channel
    if message.content.startswith('~setchannel'):
        channel = message.channel
        await channel.send("Default Channel changed to " + channel.name)

@client.event
async def on_ready():
    print("Logged on as {0.user}".format(client))
    client.loop.create_task(check_sneakers())

if __name__ == "__main__":
    client.run('OTQ2NzQxNDEwNzYwMTA1OTk0.YhjHpQ.P9dF620dtvXCT_-n_vxC671QkDM')