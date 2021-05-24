import random

warrior = {
    'name' : 'warrior',
    'atk' : 7,
    'def' : 7,
    'hp' : 20,
    'id' : 0
}

zombie = {
    'name' : 'zombie',
    'atk' : 10,
    'def' : 2,
    'hp' : 8,
    'id' : 1
}

bat = {
    'name' : 'bat',
    'atk' : 3,
    'def' : 2,
    'hp' : 4,
    'id' : 2
}

# Chosen Enemy Information
selected_enemy = 0
enemy_attack = 0
enemy_defense = 0
enemy_hp = 0
enemy_name = ''
enemy_choice = 0

# Player Information
player_attack = 8
player_defense = 6
player_hp = 15
player_choice = ''

# Rolling Information
player_attack_roll = 0
player_defense_roll = 0
enemy_attack_roll = 0
enemy_defense_roll = 0

def enemy_creation():
    global selected_enemy
    global enemy_attack
    global enemy_defense
    global enemy_hp
    global enemy_name
    selected_enemy = random.randrange(0,3)

    if selected_enemy == 2:
        enemy_attack = bat.get('atk')
        enemy_defense = bat.get('def')
        enemy_hp = bat.get('hp')
        enemy_name = bat.get('name')
    elif selected_enemy == 1:
        enemy_attack = zombie.get('atk')
        enemy_defense = zombie.get('def')
        enemy_hp = zombie.get('hp')
        enemy_name = zombie.get('name')
    elif selected_enemy == 0:
        enemy_attack = warrior.get('atk')
        enemy_defense = warrior.get('def')
        enemy_hp = warrior.get('hp')
        enemy_name = warrior.get('name')

def player_decision():
    global player_choice

    print('Please choose an action')

    decision = input('Attack, Defend, or Heal? ')

    if decision == 'Attack':
        player_choice = 'Attack'
    elif decision == 'Defend':
        player_choice = 'Defend'
    elif decision == 'Heal':
        pass
    else:
        pass

def enemy_decision():
    global enemy_choice
    enemy_choice = random.randrange(0,2)

def enemy_roll():
    global enemy_attack_roll
    global enemy_defense_roll

    enemy_attack_roll = random.randrange(0,(enemy_attack + 1))
    enemy_defense_roll = random.randrange(0,(enemy_defense + 1))

def player_roll():
    global player_attack_role
    global player_defense_role

    player_attack_roll = random.randrange(0,(player_attack + 1))
    player_defense_roll = random.randrange(0,(player_defense + 1))

def battle_calc():
    global player_choice
    global enemy_choice
    global player_hp
    global enemy_hp

    if player_choice == 'Attack':
        if enemy_choice:
            player_hp = player_hp - enemy_attack
            enemy_hp = enemy_hp - player_attack
        else:
            if enemy_attack >= player_defense:
                player_hp = player_hp - (enemy_attack - player_defense)
            else: print('Enemy could not get through your defenses!')
        

def battle_sim():
    global enemy_attack
    global enemy_defense
    global enemy_hp
    global enemy_choice

    global player_attack
    global player_defense
    global player_hp
    global player_choice

    global player_attack_roll
    global player_defense_roll
    global enemy_attack_roll
    global enemy_defense_roll

    player_decision()
    enemy_decision()

    player_roll()
    enemy_roll()





    



enemy_creation()

print(f'Hello, player 1. Your enemy will be a {enemy_name}. His stats are as follows: HP: {enemy_hp}, Attack: {enemy_attack}, Defense: {enemy_defense}.')



