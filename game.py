# David Lindeque
# May 2020
# Albert Python Assignment

from random import randrange
from PyInquirer import prompt
import sys 
import time
from pprint import pprint
import pokemon_content 
from pokemon_content import Pokemon, pokeart, battle
import simpleaudio as sa


#Play Pokemon theme song
wave_obj = sa.WaveObject.from_wave_file("pokemonsong.wav")
play_obj = wave_obj.play()


#Initiate Pokemon

charmander = Pokemon('Charmander', 'Fire', 'Water', 10, [{'attack_name' : 'Ember', 'attack_type' : 'Fire'},{'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])
squirtle = Pokemon('Squirtle', 'Water', 'Grass', 10, [{'attack_name' : 'Water Gun', 'attack_type' : 'Water'}, {'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])
bulbasaur = Pokemon('Bulbasaur', 'Grass', 'Fire', 10, [{'attack_name' : 'Vine Whip', 'attack_type' : 'Grass'}, {'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])
flareon = Pokemon('Flareon', 'Grass', 'Fire', 10, [{'attack_name' : 'Vine Whip', 'attack_type' : 'Grass'}, {'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])
vaporeon = Pokemon('Vaporeon', 'Water', 'Grass', 10, [{'attack_name' : 'Water Gun', 'attack_type' : 'Water'}, {'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])
leafeon = Pokemon('Leafeon', 'Grass', 'Fire', 10, [{'attack_name' : 'Vine Whip', 'attack_type' : 'Grass'}, {'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])
ivysaur = Pokemon('Ivysaur', 'Grass', 'Fire', 10, [{'attack_name' : 'Vine Whip', 'attack_type' : 'Grass'}, {'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])
charizard = Pokemon('Charizard', 'Fire', 'Water', 10, [{'attack_name' : 'Ember', 'attack_type' : 'Fire'}, {'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])
wartotle = Pokemon('Wartotle', 'Water', 'Grass', 10, [{'attack_name' : 'Water Gun', 'attack_type' : 'Water'}, {'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])
blastoise = Pokemon('Blastoise', 'Water', 'Grass', 10, [{'attack_name' : 'Water Gun', 'attack_type' : 'Water'}, {'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])
charmeleon = Pokemon('Charmeleon', 'Fire', 'Water', 10, [{'attack_name' : 'Ember', 'attack_type' : 'Fire'}, {'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])
venusaur = Pokemon('Venusaur', 'Grass', 'Fire', 10, [{'attack_name' : 'Vine Whip', 'attack_type' : 'Grass'}, {'attack_name' : 'Tackle', 'attack_type' : 'Normal'}])


#Create wild Pokemons and also player pokedex.


wild_pokemon = [charmander, squirtle, bulbasaur, flareon, vaporeon, leafeon, ivysaur, charizard, wartotle, blastoise, charmeleon, venusaur]
pokedex = []



#Start-up flow begins:


print(r"""

Welcome to a new adventure...


    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|


Welcome to Pokemon! Gotta catch em all!

Lets' begin...

""")


#Asking user to enter name. Checking that inout is comprised of alpha characters (letters) only.


while True:
    username = input("Trainer, what is your name? ")
    username = str(username)
    if username.isalpha():
    	break
    else:
    	print("Please enter your name, comprised of letters only.")

print('Welcome {}, your destiny awaits.'.format(username))


#Using PyInquirer throughout game for input selection.  


questions = [
    {
        'type': 'list',
        'name': 'intro_pokemon',
        'message': '{}, please select a Pokemon to begin:'.format(username),
        'choices': [pokemon.name for pokemon in wild_pokemon]
    }
]

answers = prompt(questions)


#Player to choose first pokemon.


choice = answers['intro_pokemon']

for i,pokemon in enumerate(wild_pokemon):
    if choice == pokemon.name:
        pokedex.append(wild_pokemon.pop(i))
        break

print('Well done, you selected {}. Great choice {}!'.format(pokedex[0],username))
pokemon_content.pokeart(pokedex[0].name.lower())

health_inverse = 10 - pokedex[0].health
print('Health: |' + '[]' * pokedex[0].health + ' ' * health_inverse + '|')
print('Element: {}'.format(pokedex[0].element))
print('Weakness: {}'.format(pokedex[0].weakness))
print(' ')



#################################

def pokedex_portal():
    print(f'{username}, welcome to your Pokedex. Select a Pokemon to learn more or release into the wild.')
    print(r"""
  /\___________/\
  \  ___\_/___  /
  / /   ___   \ \
 / /  .'   '.  \ \
( (__/   _   \__) )
( ( |===(_)===| ) )
 \ \ \       / / /
  \ \ '.___.' / /
  /\ \___|___/ /\
 / / /_______\ \ \
/_/_/_________\_\_\
        """)
    choices_list = [pokemon.name for pokemon in pokedex]
    choices_list.append('Go Home')
    questions = [
        {
            'type': 'list',
            'name': 'pokedex_choice',
            'message': '{}, please select a Pokemon to explore:'.format(username),
            'choices': choices_list
        }
    ]
    answers = prompt(questions)
    choice = answers['pokedex_choice']

    if choice == 'Go Home':
        homemenu()




    else:
        for i, poke in enumerate(pokedex):
            if choice == poke.name:

                print("Selected Pokemon:")
                print(" ")
                pokedexart = (poke.name).lower()
                pokemon_content.pokeart(pokedexart)
                print('')
                print((choice).upper())
                print('')
                healthinverse = 10 - poke.health
                print('Health: |' + '[]' * poke.health + ' ' * healthinverse + '|')
                print('Element: {}'.format(poke.element))
                print('Weakness: {}'.format(poke.weakness))
                print(' ')

                
                questions2 = [
                    {
                        'type': 'list',
                        'name': 'pokedex_choice2',
                        'message': 'Pokedex Options',
                        'choices': ['Release Pokemon to the wild', 'Return']
                    }
                ]
                answers2 = prompt(questions2)
                choice2 = answers2['pokedex_choice2']

                if choice2 == 'Release Pokemon to the wild':
                    print('')
                    print('You released {} to the wild!'.format(poke.name))
                    wild_pokemon.append(pokedex.pop(i))
                    print('')
                    if len(pokedex) == 0:
                        break
                    pokedex_portal()


                elif choice2 == 'Return':
                    pokedex_portal()



            

##############################


def attack_choice(poke_range):
    if len(poke_range) == 1:
        print('You only have one Pokemon.')
        selected = poke_range[0]
        print('{} selected.'.format(selected.name))

    else:

        poke_attack_list = [pokemon.name for pokemon in poke_range]
        poke_attack_list.append('Back')
        questions3 = [
            {
            'type': 'list',
            'name': 'fightchoice1',
            'message': 'Which pokemon do you want to use?',
            'choices': poke_attack_list
            }
            ]
        answers = prompt(questions3)
        choice2 = answers['fightchoice1']

        if choice2 == 'Back':
            pass

        for i, poke in enumerate(poke_range):
            if choice2 == poke.name:
                selected = pokedex[i]
                print('')
                print('You have selected: {}'.format(choice2))
                return selected
                break

##############################

def battle_attack(att, opp):
    global pokedex
    global wild_pokemon
    battle_mode = True
    while battle_mode == True:
        if len(pokedex) == 1:

            questions1 = [
                        {
                        'type': 'list',
                        'name': 'fightchoice',
                        'message': 'Battle Menu',
                        'choices': ['Fight', 'Run'],
                        }
                        ]
            answers = prompt(questions1)
            choice2 = answers['fightchoice']

        else:

            questions2 = [
                        {
                        'type': 'list',
                        'name': 'fightchoice',
                        'message': 'Battle Menu',
                        'choices': ['Fight', 'Switch Pokemon','Run'],
                        }
                        ]
            answers2 = prompt(questions2)
            choice2 = answers2['fightchoice']

        

        if choice2 == 'Run':
            print('')
            print('You got away safely!')

            for poke in pokedex:
                if att.name == poke.name:
                    poke.health = 10
                    break
            battle_mode = False
            return

        elif choice2 == 'Switch Pokemon':
            att = attack_choice(pokedex)

        elif choice2 == 'Fight':
            opponent_element = opp.element
            opponent_weakness = opp.weakness
            opponent_attack_index = randrange(0,1)
            opponent_attack = opp.attacks[opponent_attack_index]['attack_name']


            if opponent_attack == "Ember":
                oppattackelement = 'fire'

            elif opponent_attack == "Vine Whip":
                oppattackelement = "grass"

            else:
                oppattackelement = 'water'



            attackchoice = [(att.attacks[0]['attack_name']), (att.attacks[1]['attack_name'])]
            questions3 = [
                        {
                        'type': 'list',
                        'name': 'attackchoice',
                        'message': '{}, choose an attack:'.format(username),
                        'choices': attackchoice,
                        }
                        ]
            answers3 = prompt(questions3)
            choice3 = answers3['attackchoice']

            if choice3 == "Ember":
                attackelement = 'fire'

            elif choice3 == "Vine Whip":
                attackelement = "grass"

            else:
                attackelement = 'water'

            outcome = pokemon_content.battledamage(attackelement, oppattackelement, att, opp)

            attdamage = outcome[0]
            oppattdamage = outcome[1]
            old_health = att.health
            
            print('')
            print('{} used {}, dealing {} damage.'.format(att.name, choice3, attdamage))
            print('')
            print('Opposing {} used {}, dealing {}.'.format(opp.name, opponent_attack, oppattdamage))
            print('')

            att.health -= oppattdamage
            if att.health <= 0:
                att.health = 0

            opp.health -= attdamage
            if opp.health <= 0:
                opp.health = 0

            if att.health == 0 and opp.health == 0:
                print('')
                print('Winner! You beat {} before they could attack you back.'.format(opp.name))
                print('')
                print('{} health: {}'.format(att.name, old_health))
                print('')
                print('{} health: {}'.format(opp.name, opp.health))
                print('')

                for poke in pokedex:
                    if att.name == poke.name:
                        poke.health = 10
                for j, wild in enumerate(wild_pokemon):
                    if opp.name == wild.name:
                        wild.health = 10
                        pokedex.append(wild_pokemon.pop(j))
                
                battle_mode = False

            else:
                print('')
                print('Score:')
                print('')
                print('{} health: {}'.format(att.name, att.health))
                print('')
                print('{} health: {}'.format(opp.name, opp.health))
                print('')

            
            if att.health == 0 and opp.health > 0:
                print('Winner: {}'.format(opp.name))
                if len(pokedex) == 1:
                    pokedex = []
                    battle_mode = False

                else:
                    for i, poke in enumerate(pokedex):
                        if att.name == poke.name:
                            poke.health = 10
                            wild_pokemon.append(pokedex.pop(i))
                        break
                    for j, wild in enumerate(wild_pokemon):
                        if opp.name == wild.name:
                            wild.health = 10
                        break
                    
                    battle_mode = False
                            



            elif att.health > 0 and opp.health == 0:
                for poke in pokedex:
                    if att.name == poke.name:
                        poke.health = 10
                for j, wild in enumerate(wild_pokemon):
                    if opp.name == wild.name:
                        wild.health = 10
                        pokedex.append(wild_pokemon.pop(j))
                
                

                print('Winner: {}'.format(att.name))
                print('')
                print('Well done {}, you caught {}.'.format(username, opp.name))
                print('')
            

                battle_mode = False

     







#pokedex global variable assigned before this at top of file.


##############################


def homemenu():
    global pokedex
    global wild_pokemon



    step1 = [
        {
            'type': 'list',
            'name': 'step1_choice',
            'message': 'What would you like to do?',
            'choices': ['Catch Pokemon', 'View Pokedex', 'Quit']
            }
        ]   

    answers = prompt(step1)
    choice = answers['step1_choice']

    pokedex_count = len(pokedex)

    if choice == 'Catch Pokemon':
        print("Let's begin...")
        time.sleep(1)
        print('In order to catch Pokemon, we need to battle!')
        time.sleep(1)
        opponent = pokemon_content.battle(wild_pokemon)


        if pokedex_count == 1:
            chosen = pokedex[0]
            print("{}, you currently only have 1 Pokemon, {}.".format(username, chosen.name))
            print("Go get 'em {}!".format(chosen.name))
            print('')
            battle_attack(chosen, opponent)
          




        else:
            chosen = attack_choice(pokedex)
            battle_attack(chosen, opponent)
            
            
                
    elif choice == 'Quit':
        print('Thanks for playing {}!'.format(username))
        sys.exit()

    elif choice == 'View Pokedex':
        pokedex_portal()


##############################
# Game logic


playing = True
while playing:
    if len(pokedex) == 0:
        print("GAME OVER")
        print('')
        print('You have no Pokemon left.')
        print('Thanks for playing {}!'.format(username))
        print('')
        playing = False
        break

    elif len(pokedex) == 12:
        print(r"""
____   ___.______________________________ _______________.___._._.
\   \ /   |   \_   ___ \__    ___\_____  \\______   \__  |   | | |
 \   Y   /|   /    \  \/ |    |   /   |   \|       _//   |   | | |
  \     / |   \     \____|    |  /    |    |    |   \\____   |\|\|
   \___/  |___|\______  /|____|  \_______  |____|_  // ______|____
                      \/                 \/       \/ \/       \/\/
        """)
        print(f"""Congratulations {username}, you have completed the game! You have caught 'em all!""")
        print('')
        print('Look forward to seeing you soon!')
        print('')
        playing = False
        break


    homemenu()



    