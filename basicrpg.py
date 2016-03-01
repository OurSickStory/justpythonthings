import random

commands = ["status", "debug", "fight", "rest"]
charname = input('What\'s your name?')
charname = str(charname)
player_state = 'normal'
enemy_list = ["chicken", "goblin", "werewolf"]
enemy_name = random.choice(enemy_list)
player_health = 10
max_health = 15
enemy_health = random.randint(1, int(player_health))
player_hit = random.randint(1,int(enemy_health))
enemy_hit = random.randint(1,int(player_health))
player_rest = random.randint(1,int(max_health))


def char_name():
    print('Welcome to the woods ' + charname + '.')
    main_menu()
	
def status(): 
    print('Current State: {} | Current health: {}.'.format(player_state, player_health)) 
    main_menu()

def rest():
    global player_health 
    player_health = player_health
    if player_health <= max_health:
        player_health = player_health + player_rest
        print('Your health has been restore, your current health is {}.'.format(player_health))
        main_menu()
    if player_health >= max_health:
        print('You seem to be fully healed')
        main_menu()

def debug():
    print('Just a debug message.')
    main_menu()
	
def main_menu():
    mainmenu = input("What would you like to do?:")	
    if mainmenu in commands:
        if mainmenu == "fight":
            print('You have started a fight with a {}.'.format(enemy_name))
            state = 'fight'
            fightstart()
        if mainmenu == "status":
            status()
        if mainmenu == "rest":
            rest()
    else:
        print('That\'s not a valid command, ' + charname + '.')
        main_menu()

def fightstart():
    global enemy_health
    enemy_health = enemy(enemy_health)
    global player_health
    player_health = player(player_health)
    global player_hit
    player_hit = random.randint(1,int(enemy_health))
    global enemy_hit
    enemy_hit = random.randint(1,int(player_health))
    
        #fight takes place.
    while (enemy_health >= 0):
        enemy_health = enemy(enemy_health)
    while (player_health >= 0):
        player_health = player(player_health)
    print('Current enemy health {} current player health {} enemy dealt {} you dealt {}.'.format(enemy_health,player_health,enemy_hit,player_hit))
    fightstart()
	
def win():
    global enemy_name
    enemy_name = random.choice(enemy_list)
    global enemy_health
    enemy_health = random.randint(1, int(player_health))
    print('You have killed a {}.'.format(enemy_name))
    main_menu()

  
def player(player_health):
    player_health = player_health - enemy_hit    
    if player_health <= 0:
        death()
    else:
	    return player_health
		
def enemy(enemy_health):	
    enemy_health = enemy_health - player_hit
    if enemy_health <= 0:
        win()
    else:
        return enemy_health

char_name()

def death():
    print('Oh dear..you are dead')
