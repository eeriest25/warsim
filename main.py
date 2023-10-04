import random
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



enemy_force = 0
enemy_mult = 0
own_force = 0
own_mult = 0


'''def runsim():
    enemy = random.randint(1, enemy_force * enemy_mult)
    own = random.randint(1, own_force * own_mult)
    if own > enemy:
        print('You win')
        win_lose = 1
    else:
        print('You lose')
        win_lose = 0

    def digittest():
        enemy_copy = enemy
        own_copy = own
        count_enemy = 0
        count_own = 0
        while enemy_copy > 0:
            count_enemy = count_enemy + 1
            enemy_copy = enemy_copy // 10
        while own_copy > 0:
            count_own = count_own + 1
            own_copy = own_copy // 10
        if win_lose == 1:
            add_digits = count_own - count_enemy
            return add_digits
        else:
            add_digits = count_enemy - count_own
            return add_digits

    def casualtyroll():
        if digittest() == 0: #try and get the minus two rule
            roll1 = random.randint(1, 5)
            roll2 = random.randint(1, 5)
            lowroll = 0
            highroll = 0

            while roll1 == roll2:
                roll2 = random.randint(1, 5)
            if roll1 > roll2:
                if roll1 <= 2:
                    highroll = roll1
                    lowroll = 0
                    return highroll, lowroll
                if roll1 == 3:
                    highroll = 3
                    lowroll = 1
                    return highroll, lowroll
                if roll1 >= 4:
                    while roll1 - roll2 == 1:
                        roll2 = random.randint(1, roll1 - 2)
                    highroll = roll1
                    lowroll = roll2
                    return highroll, lowroll
            if roll1 < roll2:
                if roll2 <= 2:
                    highroll = roll2
                    lowroll = 0
                    return highroll, lowroll
                if roll2 == 3:
                    highroll = 3
                    lowroll = 1
                    return highroll, lowroll
                if roll2 >= 4:
                    while roll2 - roll1 <= 1:
                        roll1 = random.randint(1, roll2 - 2)
                    highroll = roll2
                    lowroll = roll1
                    return highroll, lowroll
        if digittest() == 1:
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 4)
            lowroll = 0
            highroll = 0

            while roll1 == roll2:
                roll2 = random.randint(1, 4)
            if roll1 > roll2:
                if roll1 <= 2:
                    highroll = roll1
                    lowroll = 0
                    return highroll, lowroll
                if roll1 == 3:
                    highroll = 3
                    lowroll = 1
                    return highroll, lowroll
                if roll1 >= 4:
                    while roll1 - roll2 == 1:
                        roll2 = random.randint(1, roll1 - 2)
                    highroll = roll1
                    lowroll = roll2
                    return highroll, lowroll
            if roll1 < roll2:
                if roll2 <= 2:
                    highroll = roll2
                    lowroll = 0
                    return highroll, lowroll
                if roll2 == 3:
                    highroll = 3
                    lowroll = 1
                    return highroll, lowroll
                if roll2 >= 4:
                    while roll2 - roll1 <= 1:
                        roll1 = random.randint(1, roll2 - 2)
                    highroll = roll2
                    lowroll = roll1
                    return highroll, lowroll
        if digittest() == 2:
            roll1 = random.randint(1, 7)
            roll2 = random.randint(1, 3)
            lowroll = 0
            highroll = 0

            while roll1 == roll2:
                roll2 = random.randint(1, 3)
            if roll1 > roll2:
                if roll1 <= 2:
                    highroll = roll1
                    lowroll = 0
                    return highroll, lowroll
                if roll1 == 3:
                    highroll = 3
                    lowroll = 1
                    return highroll, lowroll
                if roll1 >= 4:
                    while roll1 - roll2 == 1:
                        roll2 = random.randint(1, roll1 - 2)
                    highroll = roll1
                    lowroll = roll2
                    return highroll, lowroll
            if roll1 < roll2:
                if roll2 <= 2:
                    highroll = roll2
                    lowroll = 0
                    return highroll, lowroll
                if roll2 == 3:
                    highroll = 3
                    lowroll = 1
                    return highroll, lowroll
                if roll2 >= 4:
                    while roll2 - roll1 <= 1:
                        roll1 = random.randint(1, roll2 - 2)
                    highroll = roll2
                    lowroll = roll1
                    return highroll, lowroll
        if digittest() == 3:
            roll1 = random.randint(1, 8)
            roll2 = random.randint(1, 2)
            lowroll = 0
            highroll = 0

            while roll1 == roll2:
                roll2 = random.randint(1, 2)
            if roll1 > roll2:
                if roll1 <= 2:
                    highroll = roll1
                    lowroll = 0
                    return highroll, lowroll
                if roll1 == 3:
                    highroll = 3
                    lowroll = 1
                    return highroll, lowroll
                if roll1 >= 4:
                    while roll1 - roll2 == 1:
                        roll2 = random.randint(1, roll1 - 2)
                    highroll = roll1
                    lowroll = roll2
                    return highroll, lowroll
            if roll1 < roll2:
                if roll2 <= 2:
                    highroll = roll2
                    lowroll = 0
                    return highroll, lowroll
                if roll2 == 3:
                    highroll = 3
                    lowroll = 1
                    return highroll, lowroll
                if roll2 >= 4:
                    while roll2 - roll1 <= 1:
                        roll1 = random.randint(1, roll2 - 2)
                    highroll = roll2
                    lowroll = roll1
                    return highroll, lowroll
        if digittest() == 4:
            roll1 = random.randint(1, 9)
            roll2 = random.randint(1, 1)
            lowroll = 0
            highroll = 0

            while roll1 == roll2:
                roll2 = random.randint(1, 2)
            if roll1 > roll2:
                if roll1 <= 2:
                    highroll = roll1
                    lowroll = 0
                    return highroll, lowroll
                if roll1 == 3:
                    highroll = 3
                    lowroll = 1
                    return highroll, lowroll
                if roll1 >= 4:
                    while roll1 - roll2 == 1:
                        roll2 = random.randint(1, roll1 - 2)
                    highroll = roll1
                    lowroll = roll2
                    return highroll, lowroll
            if roll1 < roll2:
                if roll2 <= 2:
                    highroll = roll2
                    lowroll = 0
                    return highroll, lowroll
                if roll2 == 3:
                    highroll = 3
                    lowroll = 1
                    return highroll, lowroll
                if roll2 >= 4:
                    while roll2 - roll1 <= 1:
                        roll1 = random.randint(1, roll2 - 2)
                    highroll = roll2
                    lowroll = roll1
                    return highroll, lowroll
        if digittest() >= 5:
            highroll = random.randint(1, 10)
            lowroll = 0
            return highroll, lowroll

    def casualtydo(highroll, lowroll, ownforce, enemyforce, winlose):
        if winlose == 1:
            owncas = lowroll
            enemycas = highroll
            ownforce = ((10 - owncas) / 10) * ownforce
            enemyforce = ((10 - enemycas) / 10) * enemyforce
            print('Own force: ' + str(ownforce) + '\n Enemy Force: ' + str(enemyforce))
        if winlose == 0:
            owncas = highroll
            enemycas = lowroll
            ownforce = ((10 - owncas) / 10) * ownforce
            enemyforce = ((10 - enemycas) / 10) * enemyforce
            print('Own force: ' + str(ownforce) + '\nEnemy Force: ' + str(enemyforce))




    digittest()
    highroll, lowroll = casualtyroll()
    print('(' + str(highroll) + ', ' + str(lowroll) + ')')
    casualtydo(highroll, lowroll, own_force, enemy_force, win_lose)'''



@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    global own_force
    if message.author == client.user:
        return

    if message.content.startswith('run sim'):
        await message.channel.send('What are your forces?')

        try:
            own_force = await client.wait_for('message')
            own_force = int(own_force.content)
        except:
            await message.channel.send('Invalid entry. Command cancelled.')
            return

        await message.channel.send('What are the enemy forces?')

        try:
            enemy_force = await client.wait_for('message')
            enemy_force = int(enemy_force.content)
        except:
            await message.channel.send('Invalid entry. Command cancelled.')
            return

        await message.channel.send('What is your multiplier?')

        try:
            own_mult = await client.wait_for('message')
            own_mult = int(own_mult.content)
        except:
            await message.channel.send('Invalid entry. Command cancelled.')
            return

        await message.channel.send('What is the enemy multiplier?')

        try:
            enemy_mult = await client.wait_for('message')
            enemy_mult = int(enemy_mult.content)
        except:
            await message.channel.send('Invalid entry. Command cancelled.')
            return

        original_own_force = own_force
        original_enemy_force = enemy_force
        enemy = random.randint(1, enemy_force * enemy_mult)
        own = random.randint(1, own_force * own_mult)
        global resultroll
        resultroll = 'e'
        global resultforce
        resultforce = 'e'

        def runsim(): #
            while own_force >= (original_own_force * 0.1) and enemy_force >= (original_enemy_force * 0.1):
                if own > enemy:
                    print('You win')
                    win_lose = 1
                    result = 'You win'
                else:
                    print('You lose')
                    win_lose = 0
                    result = 'You lose'

                def digittest():
                    enemy_copy = enemy
                    own_copy = own
                    count_enemy = 0
                    count_own = 0
                    while enemy_copy > 0:
                        count_enemy = count_enemy + 1
                        enemy_copy = enemy_copy // 10
                    while own_copy > 0:
                        count_own = count_own + 1
                        own_copy = own_copy // 10
                    if win_lose == 1:
                        add_digits = count_own - count_enemy
                        return add_digits
                    else:
                        add_digits = count_enemy - count_own
                        return add_digits

                def casualtyroll():
                    if digittest() == 0:  # try and get the minus two rule
                        roll1 = random.randint(1, 5)
                        roll2 = random.randint(1, 5)
                        lowroll = 0
                        highroll = 0
                        global resultroll
                        resultroll = 'e'

                        while roll1 == roll2:
                            roll2 = random.randint(1, 5)
                        if roll1 > roll2:
                            if roll1 <= 2:
                                highroll = roll1
                                lowroll = 0
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll1 == 3:
                                highroll = 3
                                lowroll = 1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll1 >= 4:
                                while roll1 - roll2 == 1:
                                    roll2 = random.randint(1, roll1 - 2)
                                highroll = roll1
                                lowroll = roll2
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                        if roll1 < roll2:
                            if roll2 <= 2:
                                highroll = roll2
                                lowroll = 0
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll2 == 3:
                                highroll = 3
                                lowroll = 1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll2 >= 4:
                                while roll2 - roll1 <= 1:
                                    roll1 = random.randint(1, roll2 - 2)
                                highroll = roll2
                                lowroll = roll1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                    if digittest() == 1:
                        roll1 = random.randint(1, 6)
                        roll2 = random.randint(1, 4)
                        lowroll = 0
                        highroll = 0

                        while roll1 == roll2:
                            roll2 = random.randint(1, 4)
                        if roll1 > roll2:
                            if roll1 <= 2:
                                highroll = roll1
                                lowroll = 0
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll1 == 3:
                                highroll = 3
                                lowroll = 1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll1 >= 4:
                                while roll1 - roll2 == 1:
                                    roll2 = random.randint(1, roll1 - 2)
                                highroll = roll1
                                lowroll = roll2
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                        if roll1 < roll2:
                            if roll2 <= 2:
                                highroll = roll2
                                lowroll = 0
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll2 == 3:
                                highroll = 3
                                lowroll = 1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll2 >= 4:
                                while roll2 - roll1 <= 1:
                                    roll1 = random.randint(1, roll2 - 2)
                                highroll = roll2
                                lowroll = roll1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                    if digittest() == 2:
                        roll1 = random.randint(1, 7)
                        roll2 = random.randint(1, 3)
                        lowroll = 0
                        highroll = 0

                        while roll1 == roll2:
                            roll2 = random.randint(1, 3)
                        if roll1 > roll2:
                            if roll1 <= 2:
                                highroll = roll1
                                lowroll = 0
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll1 == 3:
                                highroll = 3
                                lowroll = 1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll1 >= 4:
                                while roll1 - roll2 == 1:
                                    roll2 = random.randint(1, roll1 - 2)
                                highroll = roll1
                                lowroll = roll2
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                        if roll1 < roll2:
                            if roll2 <= 2:
                                highroll = roll2
                                lowroll = 0
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll2 == 3:
                                highroll = 3
                                lowroll = 1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll2 >= 4:
                                while roll2 - roll1 <= 1:
                                    roll1 = random.randint(1, roll2 - 2)
                                highroll = roll2
                                lowroll = roll1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                    if digittest() == 3:
                        roll1 = random.randint(1, 8)
                        roll2 = random.randint(1, 2)
                        lowroll = 0
                        highroll = 0

                        while roll1 == roll2:
                            roll2 = random.randint(1, 2)
                        if roll1 > roll2:
                            if roll1 <= 2:
                                highroll = roll1
                                lowroll = 0
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll1 == 3:
                                highroll = 3
                                lowroll = 1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll1 >= 4:
                                while roll1 - roll2 == 1:
                                    roll2 = random.randint(1, roll1 - 2)
                                highroll = roll1
                                lowroll = roll2
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                        if roll1 < roll2:
                            if roll2 <= 2:
                                highroll = roll2
                                lowroll = 0
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll2 == 3:
                                highroll = 3
                                lowroll = 1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll2 >= 4:
                                while roll2 - roll1 <= 1:
                                    roll1 = random.randint(1, roll2 - 2)
                                highroll = roll2
                                lowroll = roll1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                    if digittest() == 4:
                        roll1 = random.randint(1, 9)
                        roll2 = random.randint(1, 1)
                        lowroll = 0
                        highroll = 0

                        while roll1 == roll2:
                            roll2 = random.randint(1, 2)
                        if roll1 > roll2:
                            if roll1 <= 2:
                                highroll = roll1
                                lowroll = 0
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll1 == 3:
                                highroll = 3
                                lowroll = 1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll1 >= 4:
                                while roll1 - roll2 == 1:
                                    roll2 = random.randint(1, roll1 - 2)
                                highroll = roll1
                                lowroll = roll2
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                        if roll1 < roll2:
                            if roll2 <= 2:
                                highroll = roll2
                                lowroll = 0
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll2 == 3:
                                highroll = 3
                                lowroll = 1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                            if roll2 >= 4:
                                while roll2 - roll1 <= 1:
                                    roll1 = random.randint(1, roll2 - 2)
                                highroll = roll2
                                lowroll = roll1
                                resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                                return highroll, lowroll
                    if digittest() >= 5:
                        highroll = random.randint(1, 10)
                        lowroll = 0
                        resultroll = '(' + str(highroll) + ', ' + str(lowroll) + ')'
                        return highroll, lowroll


                def casualtydo(highroll, lowroll, ownforce, enemyforce, winlose):
                    global own_force
                    if winlose == 1:
                        owncas = lowroll
                        enemycas = highroll
                        own_force = ((10 - owncas) / 10) * ownforce
                        enemyforce = ((10 - enemycas) / 10) * enemyforce
                        print('Own force: ' + str(own_force) + '\nEnemy Force: ' + str(enemyforce))
                        global resultforce
                        resultforce = 'Own force: ' + str(own_force) + '\nEnemy Force: ' + str(enemyforce)
                        return own_force, enemyforce
                    if winlose == 0:
                        owncas = highroll
                        enemycas = lowroll
                        own_force = ((10 - owncas) / 10) * ownforce
                        enemyforce = ((10 - enemycas) / 10) * enemyforce
                        print('Own force: ' + str(own_force) + '\nEnemy Force: ' + str(enemyforce))
                        resultforce = 'Own force: ' + str(own_force) + '\nEnemy Force: ' + str(enemyforce)
                        return own_force, enemyforce



                digittest()
                highroll, lowroll = casualtyroll()
                print('(' + str(highroll) + ', ' + str(lowroll) + ')')
                ownforce, enemyforce = casualtydo(highroll, lowroll, own_force, enemy_force, win_lose)


                return result, resultroll, resultforce, ownforce, enemyforce

        result, resultroll, resultforce, ownforce, enemyforce = runsim()
        '''while ownforce >= (original_own_force * 0.1) and enemyforce >= (original_enemy_force * 0.1):
            runsim()'''
        '''if own_force > enemyforce:
            await message.channel.send('You win' + '\n' + str(ownforce))
            print(ownforce,original_own_force)
        else:
            await message.channel.send('You lose' + '\n' + str(enemyforce))
            print(enemyforce, original_enemy_force)'''
        await message.channel.send(result + '\n' + resultroll + '\n' + resultforce)











client.run('MTE1NTczMTYyMzc1Nzc1NDM4OA.GiRDcJ.Np0CzAaUWvQKXsaxIhq8ZXbm-Wc4ZHUfSm4RPA')

