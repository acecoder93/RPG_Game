#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. Fight
# 2. Do nothing - in which case the goblin will attack him anyway
# 3. Flee

import random

class Character:
    def __init__ (self, power, health, name, coins, coinbag, armor, evade): # add money/inventory
        self.power = power
        self.health = health
        self.name = name
        self.coins = coins
        self.coinbag = coinbag
        self.armor = armor
        self.evade = evade

    def attack(self, opponent):
        opponent.health -= self.power
        self.health -= opponent.power
        if self.name == 'Medic':
            Medic.special(self)
        elif opponent.name == 'Zombie':
            zombie.special(opponent)
        elif opponent.name == 'Shadow':
            shadow.special(opponent)
        elif opponent.name == 'Mafia':
            mafia.special(opponent)
        elif opponent.name == 'GamerGod':
            gamergod.special(opponent)

        x = random.randint(1,10)
        if x <= 2:
            opponent.health -= (self.power * 2)
            print ('Critical hit!')
            print ('Opponent\'s health: {}'.format(opponent.health))
        if opponent.health <= 0:
            print ('{} is dead!'.format(opponent.name))
            print ('{} has dropped {} coins.'.format(opponent.name, opponent.coins))
            self.coinbag = opponent.coins
        if self.health <= 0:
            print("The {} does {} damage to {}.".format(opponent.name, opponent.power, self.name))
            print ('{} is dead.'.format(self.name))


    def alive(self, opponent):
        print ('{} has {} health.'.format(self.name, self.health))
        print ('{} has {} health.'.format(opponent.name, opponent.health))
        if self.health > 0:
            self.health -= opponent.power
            if opponent.name == 'Shadow':
                shadow.special(opponent)
            if self.health <= 0:
                print("The {} does {} damage to {}.".format(opponent.name, opponent.power, self.name))
                print ('{} is dead.'.format(self.name))

class Hero(Character):
    def __init__(self, power, health, name, coins, coinbag, armor, evade):
        super().__init__(power, health, name, coins, coinbag, armor, evade)
            
class Goblin(Character):
    def __init__(self, power, health, name, coins, coinbag, armor, evade):
        super().__init__(power, health, name, coins, coinbag, armor, evade)

class Medic(Character):
    def __init__(self, power, health, name, coins, coinbag, armor, evade):
        super().__init__(power, health, name, coins, coinbag, armor, evade)

    def special(self, health):
        x = random.randint(1,10)
        if x <= 2:
            self.health += 2
            print ('Medic\'s health has regenerated by two points')

class Shadow(Character):
    def __init__(self, power, health, name, coins, coinbag, armor, evade):
        super().__init__(power, health, name, coins, coinbag, armor, evade)

    def special(self,opponent): 
        x = random.randint(1,10)
        if x <= 1:
            self.health -= opponent.power
            print ('Landed a hit!')

class Zombie(Character):
    def __init__(self, power, health, name, coins, coinbag, armor, evade):
        super().__init__(power, health, name, coins, coinbag, armor, evade)
    
    def special(self, opponent):
        if self.health <= 0:
            self.health += 10

class Mafia(Character):
    def __init__(self, power, health, name, coins, coinbag, armor, evade):
        super().__init__(power, health, name, coins, coinbag, armor, evade)
    
    def special(self, opponent):
        if self.health <= 5:
            self.power += 2

class God(Character):
    def __init__(self, power, health, name, coins, coinbag, armor, evade):
        super().__init__(power, health, name, coins, coinbag, armor, evade)

    def special(self, opponent):
        if self.health == opponent.health:  
            self.health = 0
            opponent.health = 0
            print ('Everyone loses!')

# Heroes:
anuj = Hero(2, 10, 'Hero', 5, 5, 0, 0)
Medic = Medic(4, 5, 'Medic', 2, 0, 0, 0)
# Enemies:
goblin = Goblin(1, 8, 'Goblin', 3, 0, 0, 0)
shadow = Shadow(2, 9, 'Shadow', 6, 0, 0, 0)
zombie = Zombie(3, 4,'Zombie', 10, 0, 0, 0) # fix zombie regeneration
mafia = Mafia(4, 8, 'Mafia', 7, 0, 0, 0)
gamergod= God(5, 10, 'GamerGod', 15, 0, 0, 0)
# class Store:
#     def __init__(self, hero):

# class Attribute:
#     def __init__(self, power, health, name, armor, evade):
#         self.power = power
#         self.health = health
#         self.name = name
#         self.armor = armor
#         self.evade = evade
# class Tonic:
#     cost = 5
#     name = 'tonic'
#     def apply(self, character):
#         self.health +=2
#         print ('{}\'s health increased to {}.'.format(self.name, self.health))
# class Sword:
#     cost = 10
#     name = 'sword'
#     def apply(self, character):
#         self.power += 2
#         print ('{}\'s power increased to {}.'.format(self.name, self.power))

# class Armor:
#     cost = 7
#     name = 'armor'
#     def apply(self, character):
#         self.armor += 2
#         print ('{}\'s armor increased to {}.'.format(self.name, self.armor))

# class Evade:
#     cost = 5
#     name = 'evade'
#     def apply(self, character)
#         self.evade += 2
#         print ('{}\'s evade increased to {}.'format(self.name, self.evade))


# store_list = [Tonic, Sword]
# items = [Tonic, Sword]
#     def do_shopping(self,hero):
#         while True:
#             print("=====================")
#             print("Welcome to the store!")
#             print("=====================")

#             print ('You have {} coins.'.format(hero.coinbag))
#                 for x in range(len(store_list)):
#                     item = store_list[x]:
#                     print ("{}. buy {} ({})".format(i+1, item.name, item.cost))
#                 print ('10. None - Exit Store')
#                 option_select = int(input('Enter a number: '))

#                 if option_select == 10:
#                     break
#                 else:
#                     item_to_purchase = store_list[option_select-1]
#                     item = item_to_purchase()
#                     hero.buy(item)


def main():
    hero_select = [anuj, Medic] 
    hero_question = int(input('Select a number between 0 - 1 to choose a character: '))
    # Need to debug for rule exclusions
    if hero_question == 0:
        hero = hero_select[0]
    elif hero_question == 1:
        hero = hero_select[1]
    else:
        hero_question = int(input('Select a number between 0 - 1 to choose your hero: '))
    print ('You have selected to be {}.'.format(hero.name))
    print (' ')


    enemy_select = [goblin, shadow, zombie, mafia, gamergod]
    enemy_question = int(input('Select a number between 0 and 4 to choose your enemy '))
    if enemy_question == 0:
        enemy = enemy_select[0]
    elif enemy_question == 1:
        enemy = enemy_select[1]
    elif enemy_question == 2:
        enemy = enemy_select[2]
    elif enemy_question == 3:
        enemy = enemy_select[3]
    elif enemy_question == 4:
        enemy = enemy_select[4]
    print ('You have selected {} to be your enemy. '.format(enemy.name))
    print (' ')

    
    while enemy.health > 0 and hero.health > 0:
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The {} has {} health and {} power.".format(enemy.name, enemy.health, enemy.power))
        print()
        print("What do you want to do?")
        print("1. Fight")
        print("2. Do nothing")
        print("3. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
        elif raw_input == "2":
            hero.alive(enemy)
        elif raw_input == "3":
            x = str.upper(input('Are you sure you would like to quit? (Y or N) '))
            if x == "Y":
                print ("Goodbye.")
            elif x == "N":
                print ("Too late!")
            break
        else:
            print("Invalid input {}".format(raw_input))

main ()