import random

commands = ["status", "debug", "fight"]
charname = input('What\'s your name?')
charname = str(charname)
player_state = 'normal'
enemy_list = ["chicken", "goblin", "werewolf"]
enemy_name = random.choice(enemy_list)
player_health = 10
current_player_health = player_health
enemy_health = random.randint(1, int(player_health))
current_enemy_health = enemy_health
player_hit = random.randint(1,int(current_enemy_health))
enemy_hit = random.randint(1,int(current_player_health))


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
            fightstart()
        if mainmenu == "status":
            status()
    else:
        print('That\'s not a valid command, ' + charname + '.')
        main_menu()

def fightstart():
    state = 'fight'
    if state == "fight":
        print('You have started a fight with an {}.'.format(enemy_name))
        
        #fight takes place.
        
        while state == "fight" and int(player_health) > 0:


            global current_enemy_health
            current_enemy_health = current_enemy_health - player_hit
            global current_player_health
            current_player_health = current_player_health - enemy_hit
			
            global player_hit 
            player_hit = random.randint(1,int(current_enemy_health))
            global enemy_hit 
            enemy_hit= random.randint(1,int(current_player_health))
            
            print('Current enemy health {} your current health {}.'.format(current_enemy_health,current_player_health))		
                
            if int(current_enemy_health) <= 0:
                print('you have killed the ' + enemy_name + '.')
                global enemy_name
                enemy_name =random.choice(enemy_list)
                global enemy_health 
                enemy_health = random.randint(1, int(player_health))
                main_menu()

            if int(current_player_health) <= 0:
                death() 

    else: 
        print('You are not currently in a fight!')
        main_menu()
  
def death():
    print('Oh dear..you are dead')

char_name()

