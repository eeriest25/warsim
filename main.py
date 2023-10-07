import random
import discord


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    if message.author != client.user:
        print(message.author)
        print(message.channel)
        print(message.content)
        response = input()
        if response == 'none':
            pass
        else:
            await message.channel.send(response)










client.run('MTE1NTczMTYyMzc1Nzc1NDM4OA.GiRDcJ.Np0CzAaUWvQKXsaxIhq8ZXbm-Wc4ZHUfSm4RPA')

