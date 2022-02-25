import discord
import asyncio

import sneaker_code
from sneaker_code import *

client = discord.Client()

def getStatus():
    if sneaker_code.checkForRaffles() is not []:
        return "\U0001F911" + ' Raffles Live! ' + "\U0001F911"
    return "No Raffles"

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name=getStatus()))
        await asyncio.sleep(300)

@client.event
async def on_ready():
    print("Logged on as {0.user}".format(client))
    client.loop.create_task(status_task())

if __name__ == "__main__":
    client.run('OTQ2NzQxNDEwNzYwMTA1OTk0.YhjHpQ.W_Y3LDawzeebNfERCk9xYoIr7iE')