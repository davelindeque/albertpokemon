#David Lindeque
#Made a module called artwork which allows us to print character ASCII art, while keeping the raw text values in a separate file. 

from random import randrange
from PyInquirer import prompt
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

print(charmander.attacks)

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


print(username)



#print(name)

questions = [
    {
        'type': 'list',
        'name': 'intro_pokemon',
        'message': 'What do you want to do?',
        'choices': [
            'Order a pizza',
            'Make a reservation',
            'Talk to the receptionist']
    }
]

answers = prompt(questions)

pprint(answers)

pokemon_content.pokeart("bulbasaur")