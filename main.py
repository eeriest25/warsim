import random
import discord
from discord import Webhook
import aiohttp

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


'''async def foo():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discord.com/api/webhooks/1160286689302958151/D447xqp2F60scvSu-21_QbTgoXwSqz3QaFbsbs1Kr37FjVQRacwbsyKCzZ972GfieK_h)',
                                   session=session)
        await webhook.send('Hello World', username ='Foo')'''

@client.event
async def on_message():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discord.com/api/webhooks/1160286689302958151/D447xqp2F60scvSu-21_QbTgoXwSqz3QaFbsbs1Kr37FjVQRacwbsyKCzZ972GfieK_h)',
                                   session=session)
        await webhook.send('Hello World', username ='Foo')
    await Webhook.send(content='wassup')

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    '''if message.author != client.user:
        print(message.author)
        print(message.channel)
        print(message.content)
        response = input()
        if response == 'none':
            pass
        else:
            await message.channel.send(response)'''










client.run('MTE1NTczMTYyMzc1Nzc1NDM4OA.GiRDcJ.Np0CzAaUWvQKXsaxIhq8ZXbm-Wc4ZHUfSm4RPA')

