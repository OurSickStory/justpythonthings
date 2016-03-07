##########################################################################
#import the things needed for the game.
#You can PLAY the game here: http://sobieski.codes/rpg/
#if you just want to have some giggles without downloading/looking at code
##########################################################################
import random
import math
##########################################################################
#menu variables
###############################################`###########################
menucommands = ["status", "debug", "fight", "rest", "buy", "help", "inventory", "eat apple"]
##########################################################################
#player variables
##########################################################################
charname = input('What\'s your name?')
charname = str(charname)
player_state = 'normal'
##########################################################################
#battle  variables
##########################################################################
enemy_list = ["chicken", "goblin", "werewolf"]
enemy_list_2 = ["boar", "lion", "lizard"]
enemy_list_3 = ["fairy", "unicorn", "troll"]
enemy_list_4 = ["baby dragon", "centar", "sphynx"]
enemy_list_5 = ["phoenix", "king dragon"]
enemy_name = random.choice(enemy_list)
player_health = 10
max_health = 15
enemy_health = random.randint(1,int(player_health))
enemy_starting_health = 1
player_damage_percent = math.ceil(enemy_starting_health * .50)
player_max_hit = random.randint(0,int(player_damage_percent))
player_hit = random.randint(0,int(player_max_hit))
enemy_damage_percent = math.ceil(max_health * .25)
enemy_max_hit = random.randint(0,int(enemy_damage_percent))
enemy_hit = random.randint(0,int(enemy_max_hit))
killCount = 0
currentGold = 100
goldEarned = random.randint(1,int(enemy_starting_health))
fleecheck = random.randint(1,100)
fleestatus = 'yes'
enemy_damage = 0
player_damage = 0
currentFightLength = 0
##########################################################################
#resting  variables
##########################################################################
max_heal = max_health - player_health
player_rest = random.randint(1,int(max_heal))
RestorFight = random.randint(1,100)
##########################################################################
#level  variables
##########################################################################
exp = 1
currentLevel = 1
needExp = 5
addXp = random.randint(1,int(enemy_starting_health))
gainedXP = 1
tilLevel = needExp - exp
nextLevel = 2
##########################################################################
#buy menu variables
##########################################################################
buyMenu = ["food", "buy","help","main menu","armor","weapons", "buy wooden sword", "buy iron sword", "buy leather chest", "buy iron plate", "necklaces", "buy amulet of life", "buy apple"]
weapons = ["wooden sword", "iron sword"]
armor = ["leather chest", "iron plate"]
food = ["apple"]
woodenSword = 0
ironSword = 0
leatherChest = 0
ironPlate = 0
amuletLife = 0
haveweapon = 0
havearmor = 0
apple = 0
ininventory = 0

##########################################################################
#start of the game
##########################################################################
def char_name():
    print('Welcome to the woods ' + charname + '.\nUse "help" to get started.')
    main_menu()
##########################################################################
#main menu and things related to the main menu.
##########################################################################
def main_menu():
    mainmenu = ""
    while mainmenu != "quit":
        mainmenu = input("\nWhat would you like to do?:")
        if mainmenu in menucommands:
            if mainmenu == "fight":
                global player_state
                player_state = 'fight'
                monstername()
            if mainmenu == "rest":
                rest()
            if mainmenu == "status":
                status()
            if mainmenu == "debug":
                debug()
            if mainmenu == "inventory":
                inventory()
            if mainmenu == "buy":
                print('Use "help" to get started.')
                buy_menu()
            if mainmenu == "help":
                help()
            if mainmenu == "eat apple":
                eatapple()
        else:
            print('That\'s not a valid command, ' + charname + '.')
#defines the help menu
def help():
    print('\nUsable commands are:\n->Help\n->Rest\n->Status\n->Inventory\n->Buy (currently in progress)\n->Fight\n->Debug (only used for testing)')
    return
#defines the status function in main menu
def status():
    print('->Current State: {}\n->Current health: {}\n->Kill Count: {}\n->Gold on hand: {}'.format(player_state, player_health,killCount,currentGold))
    print('->You currently are level: {}\n-->You need {} exp to get to level {}.\n->Your max health is {}'.format(currentLevel,needExp,nextLevel,max_health))
    return
#defines the rest/heal function in main menu
def rest():
    global player_health
    player_health = player_health
    global RestorFight
    RestorFight = random.randint(1,100)

    if player_health >= max_health:
        print('You seem to be fully healed')
        return

    if RestorFight >= 75:
        print('\n->Looks like I\'m not sleeping now! A {} has attacked! He has {} health.'.format(enemy_name,enemy_health))
        fightstart()

    if player_health < max_health:
        global max_heal
        max_heal = max_health - player_health
        
        global player_rest
        player_rest = random.randint(1,int(max_heal))
        
        player_health = player_health + player_rest
        print('Your health has been restore, your current health is {}.'.format(player_health))
        return
#inventory
def inventory():
    if ininventory == 0:
        print('You have nothing in your inventory..')
    if ininventory >= 1:
        if ininventory == 1:
            print('You currently only have one thing in your inventory')

        else:
            print('You currently have {} things in your inventory.'.format(ininventory))
                
        if woodenSword == 1:
            print('You currently have a Wooden Sword.')
        if ironSword == 1:
            print('You currently have an Iron Sword.')
        if leatherChest == 1:
            print('You currently have a Leather Chest.')
        if ironPlate == 1:
            print('You currently have an Iron Plate.')
        if amuletLife >= 1:
            print('You currently have {} amulets.'.format(amuletLife))
        if apple >= 1:
            print('You currently have {} apples.'.format(apple))
    return     
##########################################################################
#end of main menu things
##########################################################################	
##########################################################################
#buy menu and things related to the buy menu.
##########################################################################
def buy_menu():
    global currentGold
    currentGold = currentGold
    global ininventory
    ininventory = ininventory
    global amuletLife
    amuletLife = amuletLife
    global apple
    apple = apple
    
    buymenu = ""
    while buymenu != "quit":
        buymenu = input('\nWhat would you like to buy?:')
        if buymenu in buyMenu:
            if buymenu == "buy":
                print('Buy what? You didn\'t list anything. ex: buy wooden sword')
                
            if buymenu == "buy wooden sword":
                print('You bought a Wooden Sword for 100 gold, your current gold is {}.'.format(currentGold))
                
            if buymenu == "buy iron sword":
                print('You bought an Iron Sword for 300 gold, your current gold is {}.'.format(currentGold))

            if buymenu == "buy leather chest":
                print('You bought a Leather Chest for 200 gold, your current gold is {}.'.format(currentGold))

            if buymenu == "buy iron plate":
                print('You bought an Iron Plate for 500 gold, your current gold is {}.'.format(currentGold))

            if buymenu == "buy amulet of life":
                if currentGold >= 100:
                    if amuletLife == 5:
                        print('You already have too many Amulets.')  
                    currentGold = currentGold - 100
                    amuletLife = amuletLife + 1
                    ininventory = ininventory + 1
                    print('You bought an Amulet of Life for 100 gold, your current gold is {}.'.format(currentGold))
                
                else:
                   print('You don\'t have enough gold, you currently have {} gold.'.format(currentGold))
                   
            if buymenu == "buy apple":
                if currentGold >= 50:
                    if apple == 5:
                        print('You have enough apples!')
                    if apple < 5:
                        currentGold = currentGold - 50
                        apple = apple + 1
                        ininventory = ininventory + 1
                        print('You purchased an apple for 50 gold, you currently have {} gold.'.format(currentGold))
                else:
                    print('You don\'t have enough gold, you currently have {} gold.'.format(currentGold))

                
            if buymenu == "help":
                print('\nYou can check what weapons and armour are available by typing "weapons" or "armor" in the buy menu.\nYou can only have one of each.\nUse "main menu" to return to the main menu.')

            if buymenu == "armor":
                print('Current armor is:\n->Leather chest\n-->Price: 200 gold\n-->Blocks: up to 3 damage.\n->Iron Plate\n-->Price: 500 gold\n-->Blocks up to 5 damage.')
                print('Type "buy item name" to buy.') 
                
            if buymenu == "weapons":
                print('Current weapon\'s are:\n->Wooden Sword\n-->Price: 100 gold\n--Adds: up to 3 damage.\nIron Sword\n-->Price: 300 gold\n-->Adds up to 5 damage.')
                print('Type "buy item name" to buy.')

            if buymenu == "food":
                print('Current foods are\n->Apple\n-->Price: 50 gold\n-->Heals 5 health.')
                
            if buymenu == "necklaces":
                print('Current necklaces are:\n->Amulet of life\n->Price: 100 gold\n->Has a chance to escape a critcal hit.')
                print('Type "buy item name" to buy.')
                
            if buymenu == "main menu":
                return
        else:
            print('That\'s not a valid command, ' + charname + '. Use help to see what\'s available.')           
#eat da apple.
def eatapple():
    global player_health
    player_health = player_health
    global apple
    apple = apple
    global ininventory
    ininventory = ininventory
    global max_health
    max_health = max_health
    if apple >= 1:
        if player_health <= max_health: 
            player_health = player_health + 5
            apple = apple - 1
            ininventory = ininventory - 1
            print('You have eaten an apple and restored some health!\n->Current health {}.'.format(player_health))
            return
        else:
            print('Your health is already full..')
            return
    if apple == 0:
        print('you don\'t have an apple to eat?')
        return
##########################################################################
#end of buy menu things
##########################################################################	
##########################################################################
#amulet of life define
##########################################################################
def amulet():
    global amuletLife
    amuletLife = amuletLife
    global player_health
    player_health = player_health
    global ininventory
    ininventory = ininventory
    if amuletLife >= 1:
        amuletLife = amuletLife - 1
        ininventory = ininventory - 1
        player_health = player_health + 1
        print('\nYou have used an amulet to escape death!\nYou have {} amulet(s) left.'.format(amuletLife))
        main_menu()
    else:
        death()
##########################################################################
#monsternames
##########################################################################
def monstername():
    global player_health
    player_health = player_health
    global enemy_name
    enemy_name = random.choice(enemy_list)
    global max_health
    max_health = max_health
    global enemy_health
    enemy_health = random.randint(1,int(player_health))
    global enemy_starting_health
    enemy_starting_health = enemy_health
    global goldEarned
    goldEarned = random.randint(1,int(enemy_starting_health))
    global player_damage_percent
    player_damage_percent = math.ceil(enemy_starting_health * .50)
    global player_max_hit
    player_max_hit = random.randint(0,int(player_damage_percent))
    global enemy_damage_percent
    enemy_damage_percent = math.ceil(max_health * .25)
    global enemy_max_hit
    enemy_max_hit = random.randint(0,int(enemy_damage_percent))                
    global player_hit
    player_hit = random.randint(0,int(player_max_hit))
    global enemy_hit
    enemy_hit = random.randint(0,int(enemy_max_hit))
           
    if max_health < 25:
        enemy_name = random.choice(enemy_list)
        enemy_health = random.randint(1,int(player_health))
        enemy_starting_health = enemy_health
        print('\nYou have started a fight with a {}. He has {} health.'.format(enemy_name,enemy_health))
        fightstart()

    if max_health >= 25:
        enemy_name = random.choice(enemy_list_2)
        enemy_health = random.randint(10,int(player_health))
        enemy_starting_health = enemy_health
        print('\nYou have started a fight with a {}. He has {} health.'.format(enemy_name,enemy_health))
        fightstart()
    else:
         print('debug monstername')
##########################################################################
#end of monsters
##########################################################################
##########################################################################
#fight related things
##########################################################################
def fightstart():
#define globals to edit as the fight happens.
    global player_health
    player_health = player_health
    global enemy_health
    enemy_health = enemy_health
    global max_health
    max_health = max_health
    global player_damage_percent
    player_damage_percent = math.ceil(enemy_starting_health * .50)
    global player_max_hit
    player_max_hit = random.randint(0,int(player_damage_percent))
    global enemy_damage_percent
    enemy_damage_percent = math.ceil(max_health * .25)
    global enemy_max_hit
    enemy_max_hit = random.randint(0,int(enemy_damage_percent))                
    global player_hit
    player_hit = random.randint(0,int(player_max_hit))
    global enemy_hit
    enemy_hit = random.randint(0,int(enemy_max_hit))
    global fleestatus
    fleestatus = fleestatus
        
    if enemy_hit >= player_health:
        amulet()
        
    if player_health <= enemy_health:
        if fleestatus == "yes":
            flee()
			
    if player_health >= 0:
       playerHealth()
	   
    if player_health <= 0:
        death()
        
    if enemy_health <= 0:
        win()
        
#fight length
def fightlength():
    global currentFightLength
    currentFightLength = currentFightLength
    global player_health
    player_health = player_health
    global enemy_health
    enemy_health = enemy_health
    global player_damage 
    player_damage = player_damage
    global enemy_damage
    enemy_damage = enemy_damage
    
    while True:
        currentFightLength >= 5
        player_health = player_health - enemy_hit
        enemy_health = enemy_health - player_hit
        enemy_damage = enemy_damage + enemy_hit
        player_damage = player_damage + player_hit
        if player_health <= 0:
            death()
        if enemy_health <= 0:
            win()
    else:
        print('fightlengthdebug')
        fightstart()	
#defines how the player health is going during the fight.
def playerHealth():
    global player_health
    player_health = player_health
    global player_damage 
    player_damage = player_damage
    global enemy_hit
    enemy_hit = enemy_hit
    
    player_damage = player_damage + player_hit    
    
    
    if currentFightLength <= 5: 
        if enemy_health <= 0:
            win()
        if enemy_hit == 0:
            print('-->{} missed you!'.format(enemy_name))
            enemyHealth()
        else:
            player_health = player_health - enemy_hit
            print('Me:You took {} damage, you have {} health left.'.format(enemy_hit,player_health))
            enemyHealth() 
    else:
        fightlength()       
#defines the enemy health during the fight.
def enemyHealth():
    global enemy_health
    enemy_health = enemy_health
    global enemy_damage
    enemy_damage = enemy_damage
    global currentFightLength
    currentFightLength = currentFightLength
    global enemy_hit
    enemy_hit = enemy_hit
    global player_hit
    player_hit = player_hit
    
    enemy_damage = enemy_damage + enemy_hit       
    currentFightLength = currentFightLength + 1
    if player_hit == 0:
        print('-->You missed the {}!'.format(enemy_name))
        fightstart()
    if player_hit >= enemy_health: 
        win()
    else:
        enemy_health = enemy_health - player_hit
        print('Me:You dealt {} damage, {} has {} health left.'.format(player_hit,enemy_name,enemy_health))
        fightstart()
#defines what happens when you win a fight.
def win():
    global enemy_health
    enemy_health = random.randint(1, int(player_health))
    global killCount
    killCount = killCount + 1
    global currentGold
    currentGold = currentGold + goldEarned
    global player_state
    player_state = 'normal'
    global addXp
    addXp = random.randint(1,int(enemy_starting_health))
    global exp
    exp = exp + addXp
    global gainedXP
    gainedXP = addXp
    global fleestatus
    fleestatus = 'yes'
    global currentFightLength
    currentFightLength = currentFightLength = 0
    global enemy_damage
    enemy_damage = enemy_damage
    global player_damage
    player_damage = player_damage
    
    print('\n->You have killed a {}, he did {} damage to you. You dealt {}.\n-->You have {} health, you gained {} gold and {} exp.'.format(enemy_name,enemy_damage,enemy_starting_health,player_health,goldEarned,gainedXP))
    levelup()
#defines what happens on death - reset stats
def death():
    print('\n#######################')
    print('#Oh dear..you are dead#')
    print('#######################')
    global killCount
    killCount = 0
    global player_health
    player_health = 10
    global max_health
    max_health = 15
    global currentGold
    currentGold = 0
    global player_state
    player_state = 'normal'
    global enemy_health
    enemy_health = 1
    global exp
    exp = 1
    global currentLevel
    currentLevel = 1
    global needExp
    needExp = 5
    global woodenSword
    woodensword = 0
    global ironSword
    ironSword = 0
    global leatherChest
    leatherChest = 0
    global ironPlate
    ironPlate = 0
    global haveweapon
    haveweapon = 0
    global havearmor
    havearmor = 0
    global ininventory
    ininventory = 0
    global amuletLife
    amuletLife = 0
    global apple
    apple = 0
    global currentFightLength
    currentFightLength = currentFightLength = 0
    global player_damage 
    player_damage = 0
    global enemy_damage
    enemy_damage = 0
    main_menu()
#flee menu
def flee():
  global fleestatus
  fleestatus = fleestatus
  fleemenu = ""
  while fleemenu != "quit":
    if player_health <= enemy_health:
        flee = input('\nWARNING::Your health is less then the enemy.\n->Would you like to attempt to flee?\n-->Yes or no:')
        if flee == "yes":
            print('->Attempting to flee...')
            if fleecheck >= 25:
                print('->You made it out alive!')
                fleestatus = 'yes'
                main_menu()
            else:
                print('->You couldn\'t manage to find a way out!')
                return
        if flee == "no":
            fleestatus = 'no'
            print('->good luck!')
            return
    else:
        return
##########################################################################
#end of fight related things
##########################################################################
##########################################################################
#leveling things
##########################################################################
def levelup():
    global enemy_damage
    enemy_damage = 0
    global player_damage
    player_damage = 0
    global needExp
    needExp = needExp
    if exp >= needExp:
        global currentLevel
        currentLevel = currentLevel
        global max_health
        max_health = max_health
        global nextLevel
        nextLevel = nextLevel
        
        currentLevel = currentLevel + 1
        max_health = max_health + 5
        needExp = needExp * 2
        nextLevel = currentLevel + 1
        print('\n###########################################')
        print('#You have leveled up, you are now level {}!#\n#Your max health has increased to {}!     #'.format(currentLevel,max_health))
        print('###########################################\n')
        main_menu()
    else:
        main_menu()
##########################################################################
#end leveling things
##########################################################################
#debug message, changes as needed.
def debug():
    print('This is used during testing..\n')
    return	
#starts the game after everything is verfied
char_name()
