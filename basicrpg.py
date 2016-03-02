##########################################################################
#import the things needed for the game.
##########################################################################
import random

##########################################################################
#variables and in game define's
##########################################################################
commands = ["status", "debug", "fight", "rest", "buy"]
charname = input('What\'s your name?')
charname = str(charname)
player_state = 'normal'
enemy_list = ["chicken", "goblin", "werewolf"]
enemy_name = random.choice(enemy_list)
player_health = 10
max_health = 15
enemy_health = random.randint(1,int(player_health))
enemy_starting_health = 1
player_hit = random.randint(1,int(enemy_health))
enemy_hit = random.randint(1,int(player_health))
max_heal = max_health - player_health
player_rest = random.randint(1,int(max_heal))
RestorFight = random.randint(1,100)
killCount = 0
currentGold = 0
goldEarned = random.randint(1,int(enemy_starting_health))
buyMenu = ["buy","list","mainmenu","armor","weapons", "buy wooden sword", "buy iron sword", "buy leather chest", "buy iron plate"]
weapons = ["wooden sword", "iron sword"]
armor = ["leather chest", "iron plate"]

##########################################################################
#start of the game
##########################################################################
def char_name():
    print('Welcome to the woods ' + charname + '.')
    main_menu()

##########################################################################
#main menu and things related to the main menu.
##########################################################################
def main_menu():
    mainmenu = ""
    while mainmenu != "quit":
        mainmenu = input("What would you like to do?:")
        if mainmenu in commands:
            if mainmenu == "fight":
                print('You have started a fight with a {}. He has {} health.'.format(enemy_name,enemy_health))
                global enemy_starting_health
                enemy_starting_health = enemy_health
                global goldEarned
                goldEarned = random.randint(1,int(enemy_starting_health))
                global player_hit
                player_hit = random.randint(1,int(enemy_health))
                global enemy_hit
                enemy_hit = random.randint(1,int(player_health))
                state = 'fight'
                fightstart()
            if mainmenu == "rest":
                rest()
            if mainmenu == "status":
                status()
            if mainmenu == "debug":
                debug()
            if mainmenu == "buy":
                buy_menu()
        else:
            print('That\'s not a valid command, ' + charname + '.')

#defines the status function in main menu
def status():
    print('->Current State: {}\n->Current health: {}\n->Kill Count: {}\n->Gold on hand: {}'.format(player_state, player_health,killCount,currentGold))
    return

#defines the rest/heal function in main menu
def rest():
    global player_health
    player_health = player_health
    global RestorFight
    RestorFight = random.randint(1,100)

    if RestorFight >= 75:
        print('->Looks like I\'m not sleeping now!')
        fightstart()

    if player_health < max_health:
        global max_heal
        max_heal = max_health - player_health
        
        global player_rest
        player_rest = random.randint(1,int(max_heal))
        
        player_health = player_health + player_rest
        print('Your health has been restore, your current health is {}.'.format(player_health))
        return

    if player_health >= max_health:
        print('You seem to be fully healed')
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
        buymenu = input('What would you like to buy?:')
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
    
            if buymenu == "list":
                print('You can check what weapons and armour are available by typing "weapons" or "armor" in the buy menu.\nYou can only have one of each.\nUse "mainmenu" to return to the main menu.')

            if buymenu == "armor":
                print('Current armor is:\n->Leather chest\n-->Price: 200 gold\n-->Blocks: up to 3 damage.\n->Iron Plate\n-->Price: 500 gold\n-->Blocks up to 5 damage.')
            
            if buymenu == "weapons":
                print('Current weapon\'s are:\n->Wooden Sword\n-->Price: 100 gold\n--Adds: up to 3 damage.\nIron Sword\n-->Price: 300 gold\n-->Adds up to 5 damage.')

            if buymenu == "mainmenu":
                return
        else:
            print('That\'s not a valid command, ' + charname + '. Use list to see what\'s available.')
##########################################################################
#end of buy menu things
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
    player_hit = random.randint(1,int(enemy_health))
    global enemy_hit
    enemy_hit = random.randint(1,int(player_health))

#the while loop for the fight, determines death/win    
    while enemy_health >= 0:
        enemy_health = enemy(enemy_health)
    while player_health >= 0:
        player_health = player(player_health)
    fightstart()

#defines what happens when you win a fight.
def win():
    print('->You have killed a {}, dealing {} damage.\n-->You have {} health and gained {} gold.'.format(enemy_name,player_hit,player_health,goldEarned))
    global enemy_health
    enemy_health = random.randint(1, int(player_health))
    global killCount
    killCount = killCount + 1
    global currentGold
    currentGold = currentGold + goldEarned
    main_menu()

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

#defines what happens on death - reset stats
def death():
    print('Oh dear..you are dead')
    global killCount
    killCount = 0
    global player_health
    player_health = 10
    global currentGold
    currentGold = 0
    main_menu()
##########################################################################
#end of fight related things
##########################################################################

#debug message, changes as needed.
def debug():
    print('Just a debug message.')
    return	

#starts the game after everything is verfied
char_name()

