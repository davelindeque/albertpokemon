#David Lindeque
#Made a module called artwork which allows us to print character ASCII art, while keeping the raw text values in a separate file. 

from random import randrange
from PyInquirer import prompt
from pprint import pprint
import pokemon_content 
from pokemon_content import Pokemon, pokeart
from playsound import playsound

playsound('pokemonsong.mp3')
#use this to randomly deal damage

#print(randrange(1,3)/2)

#Initiate Pokemon

charmander = Pokemon('Charmander', 'Fire', 'Water', 10, [{'Ember' : 'Fire'},{'Tackle' : 'Normal'}])
squirtle = Pokemon('Squirtle', 'Water', 'Grass', 10, [{'Water Gun' : 'Water'}, {'Tackle' : 'Normal'}])
bulbasaur = Pokemon('Bulbasaur', 'Grass', 'Fire', 10, [{'Vine Whip' : 'Grass'}, {'Tackle' : 'Normal'}])
#flareon


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