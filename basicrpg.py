import random

commands = ["status", "debug", "fight", "rest"]
charname = input('What\'s your name?')
charname = str(charname)
player_state = 'normal'
enemy_list = ["chicken", "goblin", "werewolf"]
enemy_name = random.choice(enemy_list)
player_health = 10
max_health = 15
enemy_health = random.randint(1,int(player_health))
player_hit = random.randint(1,int(enemy_health))
enemy_hit = random.randint(1,int(player_health))
max_heal = max_health - player_health
player_rest = random.randint(1,int(max_heal))
RestorFight = random.randint(1,100)
killCount = 0

def char_name():
    print('Welcome to the woods ' + charname + '.')
    main_menu()
	
def status(): 
    print('Current State: {} | Current health: {}. Kill Count {}.'.format(player_state, player_health,killCount)) 
    main_menu()

def rest():
    global player_health 
    player_health = player_health
    global RestorFight
    RestorFight = random.randint(1,100)
    
    if RestorFight >= 75:
        print('Looks like I\'m not sleeping now!')
        fightstart()
        
      
    if player_health < max_health:
        global max_heal
        max_heal = max_health - player_health
        global player_rest
        player_rest = random.randint(1,int(max_heal))
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
    print('You have started a fight with a {}.'.format(enemy_name))
    global enemy_health
    enemy_health = enemy(enemy_health)
    global player_health
    player_health = player(player_health)
    global player_hit
    player_hit = random.randint(1,int(enemy_health))
    global enemy_hit
    enemy_hit = random.randint(1,int(player_health))
    print('Current player health: {}.'.format(player_health))    
        #fight takes place.
        
    while (enemy_health >= 0):
        enemy_health = enemy(enemy_health)
    while (player_health >= 0):
        player_health = player(player_health)
    fightstart()
	
def win():
    print('You have killed a {}.'.format(enemy_name))
    global enemy_health
    enemy_health = random.randint(1, int(player_health))
    global killCount
    killCount = killCount + 1
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
        
def death():
    print('Oh dear..you are dead')
    global killCount
    killCount = 0
    global player_health
    player_health = 10
    main_menu()
    
char_name()
