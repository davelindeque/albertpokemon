#David Lindeque
#Made a module called artwork which allows us to print character ASCII art, while keeping the raw text values in a separate file. 

from random import randrange
from PyInquirer import prompt
import sys 
import time
from pprint import pprint
import pokemon_content 
from pokemon_content import Pokemon, pokeart
import simpleaudio as sa



"""Play Pokemon theme song throughout. simpleaudio is an easy-to-use audio package to play WAV files. 
Originally, I tried playsound, however, that requires AppKit dependencies, while simpleaudio is dependency-free."""

wave_obj = sa.WaveObject.from_wave_file("pokemonsong.wav")
play_obj = wave_obj.play()



#use this to randomly deal damage
#print(randrange(1,3)/2)

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

#print(charmander.attacks)

#Create wild Pokemons and also player pokedex.

wild_pokemon = [charmander, squirtle, bulbasaur, flareon, vaporeon, leafeon, ivysaur, charizard, wartotle, blastoise, charmeleon, venusaur]
pokedex = []


print("""

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

#Using PyInquirer to allow selection of Pokemon.  

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

print('Great, you selected {}. Great choice {}!'.format(pokedex[0],username))
pokemon_content.pokeart(pokedex[0].name.lower())

health_inverse = 10 - pokedex[0].health
print('Health: |' + '[]' * pokedex[0].health + ' ' * health_inverse + '|')
print('Element: {}'.format(pokedex[0].element))
print('Weakness: {}'.format(pokedex[0].weakness))
print(' ')

#homemenu()
def homemenu():


    step1 = [
        {
            'type': 'list',
            'name': 'step1_choice',
            'message': 'What would you like to do?',
            'choices': ['Catch Pokemon', 'Quit']
            }
        ]   

    answers = prompt(step1)
    choice = answers['step1_choice']

    if choice == 'Catch Pokemon':
        print("Let's begin...")
        time.sleep(1)
        print('In order to catch Pokemon, we need to battle!')
        time.sleep(1)

        pass
    elif choice == 'Quit':
        print('Thanks for playing {}!'.format(username))
        sys.exit(0)

homemenu()

#Battle function with required logic for game to execute.

def battle():
    upper_wild_indexlimit = int(len(wild_pokemon) - 1)
    print(upper_wild_indexlimit)
    opponent_index = randrange(0,upper_wild_indexlimit)
    opponent = wild_pokemon[opponent_index].name
    print("You've encountered a wild {}.".format(opponent))
    pokemon_content.pokeart(opponent.lower())
    print(opponent.upper())
    print(' ')
    opponent_health_inverse = 10 - wild_pokemon[opponent_index].health
    print('Health: |' + '[]' * wild_pokemon[opponent_index].health + ' ' * opponent_health_inverse + '|')
    print('Element: {}'.format(wild_pokemon[opponent_index].element))
    print('Weakness: {}'.format(wild_pokemon[opponent_index].weakness))
    print(' ')

    if len(pokedex) == 1:
        only_pokemon = pokedex[0]
        print("{}, you currently only have 1 Pokemon, {}.".format(username, only_pokemon.name))
        print("Go get 'em {}!".format(only_pokemon.name))
        questions = [
                    {
                        'type': 'list',
                        'name': 'battle1choice',
                        'message': '{}, what would you like to do?'.format(username),
                        'choices': ['Fight', 'Run']
                    }
                ]

        answers = prompt(questions)
        choice = answers['battle1choice']
        if choice == 'Fight':

            questions1 = [
                        {
                        'type': 'list',
                        'name': 'battle1choice',
                        'message': '{}, what would you like to do?'.format(username),

                        'choices': ['Fight', 'Run']
                        }
                    ]
            pass
        else:
            print(' ')

            homemenu()

battle()



        




















#pprint(answers)

#pokemon_content.pokeart("bulbasaur")