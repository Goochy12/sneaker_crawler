import discord
import asyncio
import json
import os
from dotenv import load_dotenv
import sneaker_code

sneakers = []
changes = False
serverInfo = {}

raffle_message_true = "\U0001F911" + ' Raffles Live! ' + "\U0001F911"
raffle_message_false = "No Raffles!"
raffle_message_current = ""
server_file_string = "servers.json"

client = discord.Client()

async def check_sneakers():
    global serverInfo
    while True:
        print("LOOPING")
        changes = sneaker_code.checkForChanges()

        if changes["changes"] == True:
            if serverInfo:
                for server in serverInfo.values():
                    print(server)
                    await client.get_channel(server).send("New Sneakers Available")

        if changes["raffle"] == True:
            if serverInfo:
                for server in serverInfo.values():
                    print(server)
                    for sneaker in changes["raffle-details"]:
                        await client.get_channel(server).send("Raffle for: " + sneaker["name"] + "\n" + sneaker["link"])

        if changes["live_raffle"] == True:
            raffle_message_current = raffle_message_true
        else:
            raffle_message_current = raffle_message_false

        print(changes["changes"])
        print(changes["raffle"])
        print(changes["live_raffle"])
        print(raffle_message_current)

        await client.change_presence(activity=discord.Game(name=raffle_message_current))

        await asyncio.sleep(30)

def setChannel(channel_id, text_channel):
    global serverInfo

    serverInfo[channel_id] = text_channel
    print(serverInfo)

    saveFile(server_file_string, serverInfo)

def openFile(filename):
    serverInfo = {}
    try:
        with open(filename, "r") as f:
            serverInfo = json.load(f)
    except:
        serverInfo = {}

    return serverInfo

def saveFile(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)

@client.event
async def on_message(message):
    global serverInfo
    if message.content.startswith('~setchannel'):
        setChannel(channel_id=str(message.guild.id), text_channel=message.channel.id)
        await client.get_channel(message.channel.id).send("Default Channel changed to " + client.get_channel(message.channel.id).name)


@client.event
async def on_ready():
    global serverInfo
    print("Logged on as {0.user}".format(client))
    client.loop.create_task(check_sneakers())
    serverInfo = openFile(server_file_string)

if __name__ == "__main__":
    load_dotenv()
    client.run(os.getenv('TOKEN'))