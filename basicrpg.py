import random

commands = ["status", "debug", "fight"]
charname = input('What\'s your name?')
charname = str(charname)
player_state = 'normal'
enemy_list = ["chicken", "goblin", "werewolf"]
enemy_name = random.choice(enemy_list)
player_health = 10
enemy_health = random.randint(1, int(player_health))
player_hit = random.randint(1,int(enemy_health))
enemy_hit = random.randint(1,int(player_health))


def char_name():
    print('Welcome to the woods ' + charname + '.')
    main_menu()
	
def status(): 
    print('Current State: {} | Current health: {}.'.format(player_state, player_health)) 
    main_menu()

def debug():
    print('Just a debug message.')
    main_menu()
	
def main_menu():
    mainmenu = input("What would you like to do?:")	
    if mainmenu in commands:
        if mainmenu == "fight":
            print('You have started a fight with an {}.'.format(enemy_name))
            state = 'fight'
            fightstart()
        if mainmenu == "status":
            status()
    else:
        print('That\'s not a valid command, ' + charname + '.')
        main_menu()

def fightstart():
    global player_health
    player_health = current(player_health)
    global enemy_health
    enemy_health = current(enemy_health)
    
        #fight takes place.
    while (enemy_health < 0):
        enemy_health = current(enemy_health)
    while (player_health <=0):
        player_health = current(player_health)
    print('Current enemy health {} current player health {} enemy dealt {} you dealt {}.'.format(enemy_health,player_health,enemy_hit,player_hit))
    fightstart()
  
def death():
    print('Oh dear..you are dead')

def win():
    print('You have killed a {}.'.format(enemy_name))
    main_menu()
    
def current(player_health):
    player_health = player_health - enemy_hit
    if player_health <= 0:
        death()
    else:
        return player_health
  
def current(enemy_health):
    enemy_health = enemy_health - player_hit
    if enemy_health <= 0:
        win()
    else:
        return enemy_health

  



char_name()
