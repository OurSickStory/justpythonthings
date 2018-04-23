# -*- coding: utf-8 -*-
import json
import random
import math

#Define initial data
data = {
       'player': {'name': 'name',
                'hp': int(10),
                'fl': int(1),
                'maxhp': int(10),
                'gold': int(30),
                'xp': int(1),
                'xpgain': int(0),
                'nxtlvl': int(1),
                'level': int(1),
                'strength': int(1)},

       'ai': {'name': 'chicken',
               'hp': int(5),
               'startinghp': int(5),
               'level': int(10),
               'strength': int(1)},

}

with open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(str_)
    outfile.close()

def updatedata(xpgain, gold):
    with open('data.json', 'w', encoding='utf8') as outfile:
        goldgained = data['player']['gold']
        update_gold = goldgained + int(gold)
        increasexp = data['player']['xp']
        currentxp = int(xpgain) + increasexp
        xpgained = int(xpgain)
        data['player']['xpgain'] = xpgained
        data['player']['xp'] = currentxp
        data['player']['gold'] = update_gold
        data['player']['fl'] = int(0)
        update_ai_health = random.randint(data['ai']['startinghp'], data['player']['maxhp'])
        data['ai']['hp'] = update_ai_health

        str_ = json.dumps(data,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(str_)
        xp = data['player']['xp']
        nxtlvl = data['player']['nxtlvl']
        outfile.close()
        levelup(xp, nxtlvl)


def levelup(xp, nxtlvl):
    if xp >= nxtlvl:
        with open('data.json', 'w', encoding='utf8') as outfile:
            level = data['player']['level']
            update_level = int(level) + 1
            data['player']['level'] = update_level
            level = data['player']['level']
            neededxp = round((4 * (level ** 3)) / 5)
            data['player']['nxtlvl'] = neededxp
            print(neededxp)
            health_increase = random.randint(1, data['player']['xpgain'])
            current_max_health = data['player']['maxhp']
            update_max_health = current_max_health + health_increase
            data['player']['maxhp'] = update_max_health
            chance_to_increase_strength = 85
            random_number = random.randint(1, 100)
            increase_ai_starting_health = random.randint(1, data['ai']['strength'])
            update_ai_starting_health = increase_ai_starting_health + data['ai']['startinghp']
            data['ai']['startinghp'] = update_ai_starting_health
            print('Congrats, you gained a level! You are now lvl {} your max health is now {}'.format(update_level, update_max_health))
            if random_number >= chance_to_increase_strength:
                strength = data['player']['strength']
                update_strength = int(random.randint(1, data['player']['strength']))
                updated_strength = strength + update_strength
                data['player']['strength'] = updated_strength
                ai_strength = data['ai']['strength']
                update_ai_strength = int(random.randint(1, data['ai']['strength']))
                updated_ai_strength = ai_strength + update_ai_strength
                data['ai']['strength'] = updated_ai_strength
                print('you managed to gain {} strength levels! Your foes have also become noticeably stronger.'.format(update_strength))
                pass
            str_ = json.dumps(data,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)
            outfile.close()
            heal()
    else:
        heal()


def heal():
    with open('data.json', 'w', encoding='utf8') as outfile:
        data['player']['hp'] = data['player']['maxhp']
        data['ai']['hp'] = data['ai']['startinghp']
        print('as you head back to town you feel refreshed.')
        str_ = json.dumps(data,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(str_)
        outfile.close()


def combat():
    combatOn = True
    with open('data.json') as data_file:
        data_loaded = json.load(data_file)
        player_health = data_loaded['player']['hp']
        ai_health = data_loaded['ai']['hp']
        ai_name = data_loaded['ai']['name']
        print('you encountered a {} he has {} health'.format(ai_name, ai_health))

    while combatOn is True:
        with open('data.json', 'w', encoding='utf8') as outfile:
            player_health = data['player']['hp']
            ai_health = data['ai']['hp']
            fightLength = data['player']['fl']
            data['player']['fl'] = fightLength
            data['ai']['hp'] = ai_health
            data['player']['hp'] = player_health
            str_ = json.dumps(data,
                        indent=4, sort_keys=True,
                        separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)
        
        if ai_health <= 0 or player_health <= 0:
            break

        if ai_health and player_health > 0:
            player_hit = random.randint(0, data['player']['strength'])
            ai_health = ai_health - player_hit
            data['ai']['hp'] = ai_health
            if fightLength <= 5:
                print('you hit the {} for {} he has {} hp left'.format(ai_name, player_hit, ai_health))
            else:
                pass
            pass

            if ai_health and player_health > 0:
                ai_hit = random.randint(0, data['ai']['strength'])
                player_health = player_health - ai_hit
                data['player']['hp'] = player_health
                if fightLength <= 5:
                    data['player']['fl'] = data['player']['fl'] + 1
                    print('the {} hit you for {} you have {} hp left'.format(ai_name, ai_hit, player_health))
                else:
                    pass
                pass

    if ai_health <= 0 or player_health <= 0:

        if ai_health <= 0:
            xpgained = random.randint(1, data['player']['maxhp'])
            gold = random.randint(1, data['ai']['startinghp'])
            youwin(xpgained, gold)

        if player_health <= 0:
            yousuck()

        else:
            pass
    else:
        print('shit')


def youwin(xpgain, gold):
    youwin.xpgain = xpgain
    youwin.gold = gold
    print('you win, you earned {} xp and {} gold.'.format(xpgain, gold))
    updatedata(xpgain, gold)


def yousuck():
    print('you lost')
    heal()


def debug():
    print('testing grounds')


def status():
    with open('data.json') as data_file:
        status = json.load(data_file)
        print(status)


def unknown_command():
    print('that\'s not a valid command')


user_input = ""
menu_commands = {
"f": combat,
"h": heal,
"s": status,
"d": debug,
}

while user_input != "quit":
    user_input = input("\nWhat would you like to do?:")
    menu_commands.get(user_input, unknown_command)()
