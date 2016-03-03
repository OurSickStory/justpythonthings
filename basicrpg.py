##########################################################################
#import the things needed for the game.
#You can PLAY the game here: http://sobieski.codes/rpg/
#if you just want to have some giggles without downloading/looking at code
##########################################################################
import random
##########################################################################
#menu variables
###############################################`###########################
menucommands = ["status", "debug", "fight", "rest", "buy", "help"]
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
enemy_name = random.choice(enemy_list)
player_health = 10
max_health = 15
enemy_health = random.randint(1,int(player_health))
enemy_starting_health = 1
player_hit = random.randint(0,int(enemy_health))
enemy_hit = random.randint(0,int(player_health))
killCount = 0
currentGold = 0
goldEarned = random.randint(1,int(enemy_starting_health))
fleecheck = random.randint(1,100)
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
buyMenu = ["buy","help","main menu","armor","weapons", "buy wooden sword", "buy iron sword", "buy leather chest", "buy iron plate"]
weapons = ["wooden sword", "iron sword"]
armor = ["leather chest", "iron plate"]
woodenSword = 0
ironSword = 0
leatherChest = 0
ironPlate = 0

##########################################################################
#start of the game
##########################################################################
def char_name():
    print('Welcome to the woods ' + charname + '.\nUse "help" to get started.\n')
    main_menu()

##########################################################################
#main menu and things related to the main menu.
##########################################################################
def main_menu():
    mainmenu = ""
    while mainmenu != "quit":
        mainmenu = input("What would you like to do?:")
        if mainmenu in menucommands:
            if mainmenu == "fight":
                global enemy_starting_health
                enemy_starting_health = enemy_health
                global goldEarned
                goldEarned = random.randint(1,int(enemy_starting_health))
                global player_hit
                player_hit = random.randint(1,int(enemy_health))
                global enemy_hit
                enemy_hit = random.randint(1,int(player_health))
                global player_state
                player_state = 'fight'
                monstername()
            if mainmenu == "rest":
                rest()
            if mainmenu == "status":
                status()
            if mainmenu == "debug":
                debug()
            if mainmenu == "buy":
                print('Use "help" to get started.')
                buy_menu()
            if mainmenu == "help":
                help()
        else:
            print('That\'s not a valid command, ' + charname + '.\n')

#defines the help menu
def help():
    print('\nUsable commands are:\n->Help\n->Rest\n->Status\n->Buy (currently in progress)\n->Fight\n->Debug (only used for testing)\n')
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
        print('You seem to be fully healed\n')
        return

    if RestorFight >= 75:
        print('->Looks like I\'m not sleeping now! A {} has attacked!'.format(enemy_name))
        fightstart()

    if player_health < max_health:
        global max_heal
        max_heal = max_health - player_health
        
        global player_rest
        player_rest = random.randint(1,int(max_heal))
        
        player_health = player_health + player_rest
        print('Your health has been restore, your current health is {}.\n'.format(player_health))
        return

##########################################################################
#end of main menu things
##########################################################################	
##########################################################################
#buy menu and things related to the buy menu.
##########################################################################
def buy_menu():
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
    
            if buymenu == "help":
                print('\nYou can check what weapons and armour are available by typing "weapons" or "armor" in the buy menu.\nYou can only have one of each.\nUse "main menu" to return to the main menu.')

            if buymenu == "armor":
                print('Current armor is:\n->Leather chest\n-->Price: 200 gold\n-->Blocks: up to 3 damage.\n->Iron Plate\n-->Price: 500 gold\n-->Blocks up to 5 damage.')
                print('Type "buy item name" to buy.')            
            if buymenu == "weapons":
                print('Current weapon\'s are:\n->Wooden Sword\n-->Price: 100 gold\n--Adds: up to 3 damage.\nIron Sword\n-->Price: 300 gold\n-->Adds up to 5 damage.')
                print('Type "buy item name" to buy.')
                
            if buymenu == "main menu":
                return
        else:
            print('That\'s not a valid command, ' + charname + '. Use help to see what\'s available.')
##########################################################################
#end of buy menu things
##########################################################################	
##########################################################################
#monsternames
##########################################################################
def monstername():
    global enemy_name
    enemy_name = random.choice(enemy_list)
    
    if max_health < 25:
        enemy_name = random.choice(enemy_list)
        print('\nYou have started a fight with a {}. He has {} health.'.format(enemy_name,enemy_health))
        fightstart()

    if max_health >= 25:
        enemy_name = random.choice(enemy_list_2)
        print('\nYou have started a fight with a {}. He has {} health.'.format(enemy_name,enemy_health))
        fightstart()
##########################################################################
#end of monsters
##########################################################################
##########################################################################
#fight related things
##########################################################################
def fightstart():
#define globals to edit as the fight happens.
    global enemy_health
    enemy_health = enemy(enemy_health)
    global enemy_starting_health
    enemy_starting_health = enemy_health
    global player_health
    player_health = player(player_health)
    global player_hit
    player_hit = random.randint(0,int(enemy_health))
    global enemy_hit
    enemy_hit = random.randint(0,int(player_health))
    
    if player_hit == 0:
        print('-->You missed the {}!'.format(enemy_name))
        fightstart()
    
    if enemy_hit == 0:
        print('-->{} missed you!'.format(enemy_name))
        fightstart()

    if player_health <= enemy_health:
        flee()
    
#the while loop for the fight, determines death/win    
    while enemy_health >= 0:
        enemy_health = enemy(enemy_health)
    while player_health >= 0:
        player_health = player(player_health)
    fightstart()

#defines how the player health is going during the fight.
def player(player_health):
    player_health = player_health - enemy_hit
 
    if player_health <= 0:
        death()
    else:
      print('Me: You took {} damage. You have {} health left.'.format(enemy_hit,player_health))
      return player_health

#defines the enemy health during the fight.
def enemy(enemy_health):
    enemy_health = enemy_health - player_hit
        
    if enemy_health <= 0:
        win()
    else:
        print('Me: You dealt {} damage. {} has {} health left.'.format(player_hit,enemy_name,enemy_health))
        return enemy_health

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
    print('\n->You have killed a {}, dealing {} damage.\n-->You have {} health, you gained {} gold and gained {} exp.\n'.format(enemy_name,player_hit,player_health,goldEarned,gainedXP))
    levelup()

#defines what happens on death - reset stats
def death():
    print('\nOh dear..you are dead\n')
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
    main_menu()

#flee menu
def flee():
  fleemenu = ""
  while fleemenu != "quit":
    if player_health <= enemy_health:
        flee = input('\nWARNING::Your health is less then the enemy.\n->Would you like to attempt to flee?\n-->Yes or no:')
        if flee == "yes":
            print('->Attempting to flee...\n')
            if fleecheck >= 25:
                print('->You made it out alive!')
                main_menu()
            else:
                print('->You couldn\'t manage to fine a way out!')
                return
        if flee == "no":
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

