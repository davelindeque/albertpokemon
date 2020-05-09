# David Lindeque
# May 2020
# Albert Python Assignment

from random import randrange
from PyInquirer import promp
t
import sys 
import time
from pprint import pprint
import pokemon_content 
from pokemon_content import Pokemon, pokeart, battle
import simpleaudio as sa


"""Play Pokemon theme song throughout. simpleaudio is an easy-to-use, dependency-free audio package to play WAV files.""" 


#wave_obj = sa.WaveObject.from_wave_file("pokemonsong.wav")
#play_obj = wave_obj.play()


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
hint = int(1) 


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
            'message': '{}, please select a Pokemon to begin:'.format(username),
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




def homemenu():


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

    if choice == 'Catch Pokemon':
        print("Let's begin...")
        time.sleep(1)
        print('In order to catch Pokemon, we need to battle!')
        time.sleep(1)
        pokemon_content.battle(wild_pokemon)
        
    elif choice == 'Quit':
        print('Thanks for playing {}!'.format(username))
        sys.exit()

    elif choice == 'View Pokedex':
        pokedex_portal()










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










'''def battle():
    upper_wild_indexlimit = int(len(wild_pokemon) - 1)
    print(upper_wild_indexlimit)
    opponent_index = randrange(0,upper_wild_indexlimit)
    opponent = wild_pokemon[opponent_index]
    opponent_name = wild_pokemon[opponent_index].name
    print("You've encountered a wild {}.".format(opponent_name))
    pokemon_content.pokeart(opponent_name.lower())
    print(opponent_name.upper())
    print(' ')
    opponent_health_inverse = 10 - wild_pokemon[opponent_index].health
    print('Health: |' + '[]' * wild_pokemon[opponent_index].health + ' ' * opponent_health_inverse + '|')
    print('Element: {}'.format(wild_pokemon[opponent_index].element))
    print('Weakness: {}'.format(wild_pokemon[opponent_index].weakness))
    print(' ')'''

def battle_menu():

    questions1 = [
                {
                'type': 'list',
                'name': 'fightchoice',
                'message': '{}, choose an attack:'.format(username),
                'choices': ['Fight', 'Run', 'Hint']
                }
                ]
    answers = prompt(questions1)
    choice2 = answers['fightchoice']

    if choice2 == 'Fight':
        pass

    elif choice2 == 'Hint':
        pass

#battlemenu()

def hint():

    if hint < 1:
        print('No hints left! Returning to battle menu.')
        time.sleep(2)
        battlemenu()

    elif hint == 1:
        print("{}, in this game, you get one hint - this is it!".format(username))
        print(" ")
        attack1 = only_pokemon.attacks[0]['attack_name']
        pokeelement = only_pokemon.element
        opponent_element = opponent.element
        opponent_weakness = opponent.weakness

        if pokeelement == opponent_weakness:
            if pokeelement == opponent_element:
                print(f"""Your Pokemon, {only_pokemon}, has special attributes.
Every Pokemon has a special element. 
This element determines attack profile and advantage.
With that, every Pokemon has a weakness...

{only_pokemon} has the following attacks:

{attack1} - uses {only_pokemon}'s {pokeelement} element as it's attack type.
{attack1} - normal move type.

If you choose an attack that has an advantage over your opponent, you deal double damage.
An advantage is when your attack's element matches your opponent's weakness. 

If your attack uses an element that your opponent is made from, your attacks is 50% less powerful. 

Your opponent, {opponent_name}, is made from {opponent_element}. Their weakness is {opponent_weakness}.

Your {attack1} is comprised of the same element as your opponent's element, {opponent_element}.

Using this attack will deal up to 50% less damage! We recommend using Tackle.

                        """)
                hint -= 1
                print(' ')
                battlemenu()

            else: 
                print(f"""Your Pokemon, {only_pokemon}, has special attributes.
Every Pokemon has a special element. 
This element determines attack profile and advantage.
With that, every Pokemon has a weakness...

{only_pokemon} has the following attacks:

{attack1} - uses {only_pokemon}'s {pokeelement} element as it's attack type.
{attack1} - normal move type.

If you choose an attack that has an advantage over your opponent, you deal double damage.
An advantage is when your attack's element matches your opponent's weakness. 

If your attack uses an element that your opponent is made from, your attacks is 50% less powerful. 

Your opponent, {opponent_name}, is made from {opponent_element}. Their weakness is {opponent_weakness}.

Use your {attack1} to deal double damage!
                            """)
       


    if len(pokedex) == 1:
        only_pokemon = pokedex[0]
        print("{}, you currently only have 1 Pokemon, {}.".format(username, only_pokemon.name))
        print("Go get 'em {}!".format(only_pokemon.name))
        attack_name
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
            battle_menu()

        else:
            wild_pokemon[opponent_index].health = 10
            print(' ')
            print('You got away safely.')
            homemenu()



 #       else:
 #           print(' ')

#            homemenu()









"""Battle function with required logic for game to execute.
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

            homemenu()"""

#battle()



        
