import asyncio
import random
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



enemy_force = 0
enemy_mult = 0
own_force = 0
own_mult = 0





@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    weak_troop_own = 0
    medium_troop_own = 0
    strong_troop_own = 0
    weak_plane_own = 0
    medium_plane_own = 0
    strong_plane_own = 0
    weak_ship_own = 0
    medium_ship_own = 0
    strong_ship_own = 0
    weak_tank_own = 0
    medium_tank_own = 0
    strong_tank_own = 0
    weak_artillery_own = 0
    medium_artillery_own = 0
    strong_artillery_own = 0
    weak_troop_enemy = 0
    medium_troop_enemy = 0
    strong_troop_enemy = 0
    weak_plane_enemy = 0
    medium_plane_enemy = 0
    strong_plane_enemy = 0
    weak_ship_enemy = 0
    medium_ship_enemy = 0
    strong_ship_enemy = 0
    weak_tank_enemy = 0
    medium_tank_enemy = 0
    strong_tank_enemy = 0
    weak_artillery_enemy = 0
    medium_artillery_enemy = 0
    strong_artillery_enemy = 0


    if message.author == client.user:
        return

    if message.content.startswith('Test'):
        if message.content.__contains__('\n'):
            await message.channel.send('success')
        else:
            await message.channel.send('failure')

    if message.content.startswith('Run sim'):

        await message.channel.send('Is this a land, air, or naval battle?')
        massage = await client.wait_for('message')
        massage = massage.content
        print(massage)

        if massage == 'Land':
            await message.channel.send('Input your forces like this: (only the number) \nWeak Troops:\nMedium Troops:\n'
                                       'Strong Troops:\nWeak Planes:\nMedium Planes:\nStrong Planes:\nWeak '
                                       'Ships bombarding:\nMedium Ships bombarding:\nStrong Ships bombarding:'
                                       '\nWeak Tanks:\nMedium Tanks:\nStrong Tanks:\n20 KM Artillery:\n40/60 Artillery:'
                                       '\n100 KM Artillery:')
            owninput = await client.wait_for('message')
            owninput = str(owninput.content)
            owninput = owninput.rsplit(sep='\n')
            try:
                weak_troop_own = int(owninput[0])
            except:
                pass
            try:
                medium_troop_own = int(owninput[1])
            except:
                pass
            try:
                strong_troop_own = int(owninput[2])
            except:
                pass
            try:
                weak_plane_own = int(owninput[3])
            except:
                pass
            try:
                medium_plane_own = int(owninput[4])
            except:
                pass
            try:
                strong_plane_own = int(owninput[5])
            except:
                pass
            try:
                weak_ship_own = int(owninput[6])
            except:
                pass
            try:
                medium_ship_own = int(owninput[7])
            except:
                pass
            try:
                strong_ship_own = int(owninput[8])
            except:
                pass
            try:
                weak_tank_own = int(owninput[9])
            except:
                pass
            try:
                medium_tank_own = int(owninput[10])
            except:
                pass
            try:
                strong_tank_own = int(owninput[11])
            except:
                pass
            try:
                weak_artillery_own = int(owninput[12])
            except:
                pass
            try:
                medium_artillery_own = int(owninput[13])
            except:
                pass
            try:
                strong_artillery_own = int(owninput[14])
            except:
                pass

            await message.channel.send('Input your enemys forces like this: (only the number) \nWeak Troops:\n'
                                       'Medium Troops:\nStrong Troops:\nWeak Planes:\nMedium Planes:\nStrong Planes:'
                                       '\nWeak Ships bombarding:\nMedium Ships bombarding:\nStrong Ships bombarding:'
                                       '\nWeak Tanks:\nMedium Tanks:\nStrong Tanks:\n20 KM Artillery:\n40/60 Artillery:'
                                       '\n100 KM Artillery:')
            enemyinput = await client.wait_for('message')
            enemyinput = str(enemyinput.content)
            enemyinput = enemyinput.rsplit(sep='\n')
            try:
                weak_troop_enemy = int(enemyinput[0])
            except:
                pass
            try:
                medium_troop_enemy = int(enemyinput[1])
            except:
                pass
            try:
                strong_troop_enemy = int(enemyinput[2])
            except:
                pass
            try:
                weak_plane_enemy = int(enemyinput[3])
            except:
                pass
            try:
                medium_plane_enemy = int(enemyinput[4])
            except:
                pass
            try:
                strong_plane_enemy = int(enemyinput[5])
            except:
                pass
            try:
                weak_ship_enemy = int(enemyinput[6])
            except:
                pass
            try:
                medium_ship_enemy = int(enemyinput[7])
            except:
                pass
            try:
                strong_ship_enemy = int(enemyinput[8])
            except:
                pass
            try:
                weak_tank_enemy = int(enemyinput[9])
            except:
                pass
            try:
                medium_tank_enemy = int(enemyinput[10])
            except:
                pass
            try:
                strong_tank_enemy = int(enemyinput[11])
            except:
                pass
            try:
                weak_artillery_enemy = int(enemyinput[12])
            except:
                pass
            try:
                medium_artillery_enemy = int(enemyinput[13])
            except:
                pass
            try:
                strong_artillery_enemy = int(enemyinput[14])
            except:
                pass
        elif massage == 'Air':
            await message.channel.send('air baby')
        elif massage == 'Naval':
            await message.channel.send('naval baby')
        else:
            await message.channel.send('uh oh')

        own = weak_troop_own + (medium_troop_own * 3) + (strong_troop_own * 5) + (weak_plane_own * 50) + \
              (medium_plane_own * 150) + (strong_plane_own * 250) + (weak_tank_own * 20) + (medium_tank_own * 60) + \
              (strong_tank_own * 100) + (weak_ship_own * 100) + (medium_ship_own * 300) + (strong_ship_own * 500) + \
              (weak_artillery_own * 30) + (medium_artillery_own * 90) + (strong_artillery_own * 150)
        enemy = weak_troop_enemy + (medium_troop_enemy * 3) + (strong_troop_enemy * 5) + (weak_plane_enemy * 50) + \
                (medium_plane_enemy * 150) + (strong_plane_enemy * 250) + (weak_tank_enemy * 20) + \
                (medium_tank_enemy * 60) + (strong_tank_enemy * 100) + (weak_ship_enemy * 100) + \
                (medium_ship_enemy * 300) + (strong_ship_enemy * 500) + (weak_artillery_enemy * 30) + \
                (medium_artillery_enemy * 90) + (strong_artillery_enemy * 150)
        await message.channel.send(own)
        await message.channel.send(enemy)












client.run('MTE1NTczMTYyMzc1Nzc1NDM4OA.GiRDcJ.Np0CzAaUWvQKXsaxIhq8ZXbm-Wc4ZHUfSm4RPA')

