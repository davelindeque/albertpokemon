#David Lindeque
#module made where the pokemon class will be created and stored. In addition, all ASCII art for Pokemon will be stored here. 
from random import randrange
from PyInquirer import prompt

#############################
# battle selects the opponent.

def battle(wild_pokemon):
    opponent_index = randrange(0, len(wild_pokemon) -1)
    opponent = wild_pokemon[opponent_index]
    opponent_name = wild_pokemon[opponent_index].name
    print("You've encountered a wild {}.".format(opponent_name))
    pokeart(opponent_name.lower())
    print(opponent_name.upper())
    print(' ')
    opponent_health_inverse = 10 - wild_pokemon[opponent_index].health
    print('Health: |' + '[]' * wild_pokemon[opponent_index].health + ' ' * opponent_health_inverse + '|')
    print('Element: {}'.format(wild_pokemon[opponent_index].element))
    print('Weakness: {}'.format(wild_pokemon[opponent_index].weakness))
    print(' ')
    return opponent


#############################
# battledamage is attack point calculator.

def battledamage(elementattack, oppelementattack, chosen, opponent):

    if elementattack == opponent.element:
        attdamage = randrange(1,3)//2

    elif elementattack == opponent.weakness:
        attdamage = randrange(1,3)*2

    else:
        attdamage = randrange(1,3)

    if oppelementattack == chosen.element:
        oppdamage = randrange(1,3)//2

    elif oppelementattack == chosen.weakness:
        oppattdamage = randrange(1,3)*2

    else:
        oppattdamage = randrange(1,3)

    return [attdamage, oppattdamage]

    
#############################
# hint was an idea where users get 1 hint throughout the game.


'''

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
'''


############################
#Trainer class

class Trainer:
    name = ''
    pokedex = []

    def __init__(self, name, pokedex):
        self.name = name
        self.pokedex = pokedex

class Pokemon:
    name = ''
    element = ''
    weakness = ''
    health = 0
    attacks = []

    def __init__(self, name, element, weakness, health, attacks):
        self.name =  name
        self.element = element
        self.weakness = weakness
        self.health = health
        self.attacks = attacks

    def __repr__(self):
        return self.name



############################
#Pokemon character art printer.


def pokeart(poke_name):
	if poke_name == "bulbasaur":
		print("""
			                     /
                        _,.------....___,.' ',.-.
                     ,-'          _,.--"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                       |
     .'    `---""       ``"-.--"'`   |             . |
    .,__|   .               |.        |             |.___
    `,'         ,-"'  .               |             |    L
   ,'          '    _.'                -._          /    |
  ,`-.    ,".   `--'                      >.      ,'     |
 . .'|   `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / |`        `.    .      .'/
 j|:D  |         `--'  ' ,'_  . .         `.__, |   , /
/ L:_  |                 .  "' :_;                `.'.'
.    ""'                  ""'                    |
 `.                                 .    `.   _,..  `
   `,_   .    .                _,-'/    .. `,'   __  `
    ) ||        ___....----"'  ,'   .'  | |   '  | .
   /   `. "`-.--"'         _,' ,'     `---' |    `./  |
  .   _  `""'--.._____..--"   ,             '         |
  | ." `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'| ____.___.'
 `"^--'..'   '-`-^-'"--    `-^-'`.''  `.,^.`.--'


				""")

	elif poke_name == "squirtle":
		print("""

              _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                     |. |
      ,'                      .    |
      ._|               ,"".       |
     ._.'|             / |  `      __
     |   |     `-.'   ||    `.       |
     |   |            '-._,'||       | |
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -"  .     `____
`.__"'-.`-...,---------','         `. `..  /.   |
.'        `"-..___      __,'|          |  |     |
 .          |   `""--'    `.           . |     |
  `        |              `.          |  .     |
    |-.        |- --_ _ _  _ _ _ _ _ '.        j   |                                                                          
    `._    .'      |          `.     .|   ,     |
         `--,|       .            `7""' |  ,      |
            ` `      `            /     |  |      |    _,-'"`-._
             | `.     .__________/      |  '      |  ,'          `.
               |    ``.       |   |  /.''         |                 |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      |         ."     `.  |/        j     `    |
               /    `.     |       /         | /         |_____/    |
              |       `-.   7-.._ .          |"          '  ___     /
              |          `./_    `|          |     _______./   | __/
              `.           / `----|          |`---'
                |          |      |          |
                |           |     `|         |
                |.-_       _|.     |_.      _| 
                                  `---.__,--.|

                                  """)


	elif poke_name == "charmander":
		print("""

	     _.--""`-..
            ,'          `.
          ,'          __  `.
         ||          " __   |
        , |           | |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' | `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. |        .   ,    |
-:..     `. `-..--_.,.<       `"      | `.        `-| |   .
  `,         "" '     `.              ,'         |   |  ',,
    `.      '            '            |          '    |'. ||
      `.   |              |      _,-'           |       ''
        `._'               |   '"|                .      |
           |                '     |                `._  ,'
           |                 '     |                 .'|
           |                 .      |                | |
           |                 |       L              ,' |
           |                 |       |             /   '
           |                 |       |           ,'   /
          ,'  |               |  _.._ ,-..___,..-'    ,'
         |     .             .      `!             ,j'
        |       `.          |        .           .'|
       .          `.       |         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,|
   -" _`.         _,'     | _  _  _.|
    ""--'--- - - -"'        `' '! |! |
                            `" " -'

                            """)

	elif poke_name == "charizard":
		print("""

		 ."-,.__
                 `.     `.  ,
              .--'  .._,'"-' `.
             .    .'         `'
             `.   |          ,'
               `  '--.   ,-"'
                `"`   |  |
                   -. |, |
                    `--Y.'      ___.
                         |     L._, |
               _.,        `.   <  <|                _
             ,' '           `, `.   | |            ( `
          ../, `.            `  |    .|`.           | |_
         ,' ,..  .           _.,'    |||l            )  '".
        , ,'   |           ,'.-.`-._,'  |           .  _._`.
      ,' /      | |        `' ' `--/   | |          / /   ..|
    .'  /        | .         ||__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` |
 / .           |"`_/. `-_ |_,.  ,'    +-' `-'  _,        ..,-.    |`.
.  '         .-f    ,'   `    '.       |__.---'     _   .'   '     | |
' /          `.'    l     .' /          |..      ,_|/   `.  ,'`     L`
|'      _.-""` `.    | _,'  `           | `.___`.'"`-.  , |   |     | |
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
. |          ,' .-   ,' ||               | .-.        `.      .'     ||
 `'        ,'    `".'    |               |    `.        '. -.'       `'
          /      ,'      |               |,'   | -.._,.'/'
          .     /        .               .       |    .''
        .`.    |         `.             /         :_,'.'
          | `...|   _     ,'-.        .'         /_.-'
           `-.__ `,  `'   .  _.>----''.  _  __  /
                .'        /"'          |  "'   '_
               /_|.-'| ,".             '.'`__'-( |
                 / ,"'"|,'               `/  `-.|"

                 """)

	elif poke_name == "charmeleon":
		print("""

	               ,-'`
                  _,"'    j
           __....+       /               .
       ,-'"             /               ; `-._.'.
      /                (              ,'       .'
     |            _.    |             |    ---._ `-.
     ,|    ,   _.'  Y    |              `- ,'   |    `.`.
     l'    | ,'._,|  `.    .              /       ,--. l
  .,-        `._  |  |    |              |        _   l .
 /              `"--'    /              .'       ``. |  )
|     ,                 |                .        |  `. '
`.                .     |                '._  __   ;. | '
  `-..--------...'       |                   `'  `-"'.  | 
      `......___          `._                        |  | 
               /`            `..                     |   .
              /|                `-.                  |    L
             / |               |   `._               .    |
           ,'  |,-"-.   .       .     `.            /     |
         ,'    |     '   |       |       `.         /      |
       ,'     /|       |   .     |         .       /       |
     ,'      / |        |   .    +          |     ,'       .'
    .       .  |         |  |     |           | _,'        / 
    |       |  L          `|      .          `        ,' '
    |    _. |   |           /      |           .     .' ,'
    |   /  `|    |         .       |  /        |   ,' .'
    |   ,-..|      -.     ,        | /         |,.' ,'
    `. |___,`    /  `.   /`.       '          |  .'
      '-`-'     j     ` /."7-..../|          ,`-'
                |        .'  / _/_|          .
                `,       `"'/"'    |           `.
                  `,       '.       `.         |
             __,.-'         `.        | '       |
            /_,-'|           ,'        |        _.
             |___.---.   ,-'        .-':,-"`| ,' .
                  L,.--"'           '-' |  ,' `-.|
                                        `.'

                                        """)

	elif poke_name == "wartotle":
		print("""

	__                              _.--'"7
    `. `--._                        ,-'_,-  ,'
     ,'  `-.`-.                   /' .'    ,|
     `.     `. `-     __...___   /  /     - j
       `.     `  `.-""        " .  /       /
         |     /                ` /       /
          |    /                         ,'
          '._'_               ,-'       |
             | |             ,|  |   ...-'
             || `         ,|_|  |   | `             _..__
            /|| |          | |  |   |  |   _,_    .-"     `-.
           | '.-'          |_|_,' __!  | /|  |  /           |
   ,-...___ .=                  ._..'  /`.| ,`,.      _,.._ |
  |   |,.. |      '  `'        ____,  ,' `--','  |    /     |
 ,`-..'  _)  .`-..___,---'_...._/  .'      '-...'   |      /
'.__' ""'      `.,------'"'      ,/            ,     `.._.' `.
  `.             | `--........,-'.            .         |      |
    `-.          .   '.,--""     |           ,'|         |      .
       `.       /     |          L          ,|   .       |  .,---.
         `._   '      |           |         /  .  L      | /   __ `.
            `-.       |            `._   ,    l   .    j |   '  `. .
              |       |               `"' |  .    |   /  '      .' |
              |       |                   j  |    |  /  , `.__,'   |
              `.      L                 _.   `    j ,'-'           |
               |`"---..| ._______,...,--' |   |   /|'      /       |
               '       |                 |   .  / |      '        /
                .      .              ____L   | '  j    -',       /
               / `.     .          _,"     |    | /  ,-','      ,'
              /    `.  ,'`-._     /         |   i'.,'_,'      .'
             .       `.      `-..'             |_,-'      _.'
             |         `._      |            ''/      _,-'
             |            '-..._|              `__,.--'
            ,'           ,' `-.._`.            .
           `.    __      |       "'`.          |
             `-"'  `"'            7         `.
                                    `---'--.,'"`'
                                    """)

	elif poke_name == "blastoise":
		print("""

			    _
            _,..-"--' `,.-".
          ,'      __.. --',  |
        _/   _.-"' |    .' | |       ____
  ,.-""'    `-"+.._|     `.' | `-..,',--.`.
 |   ,.                      '    j 7    l |__
 |.-'                            /| |    j||  .
 `.                   |         / L`.`""','||  |
   `.,----..._       ,'`"'-.  ,'   | `""'  | |  l
     Y        `-----'       v'    ,'`,.__..' |   .
      `.                   /     /   /     `.|   |
        `.                /     l   j       ,^.  |L
          `._            L       +. |._   .'||  | |
            .`--...__,..-'"'-._  l L  "    |  | |
          .'  ,`-......L_       |  | |     _.'  ,'.  l
       ,-"`. / ,-.---.'  `.      |  L..--"'  _.-^.|   l
 .-"".'"`.  Y  `._'   '    `.     | | _,.--'"     |   |
  `._'   |  |,-'|      l     `.   | |"..          |   l
  ,'.    |  |`._'      |      `.  | |_,...-------"`    L
 /   |   | _|-' `.     L       | j ,|              |   |
`--,"._,-+' /`---^..../._____,.L',' `.             ||  |
   |,'      L                   |     `-.          | |j
            .                    |       `,        |  |
             |                __`.Y._      -.     j   |
              |           _.,'       `._     |    |  j
              ,-"`-----"--'           |`.    |  7   |
             /  `.        '            |  |    | /   |
            |     `      /             |  |    Y    |
            |      |    .             ,'    |   L_.-')
             L      `.  |            /      ]     _.-^._
              |   ,'  `-7         ,-'      / |  ,'      `-._
             _,`._       `.   _,-'        ,',^.-            `.
          ,-'     v....  _.`"',          _:'--....._______,.-'
        ._______./     /',,-'"'`'--.  ,-'  `.
                 --"`.,'         _|`----...' 
                        --------""'


			""")

	elif poke_name == "ivysaur":
		print("""

			      ___   ,   Y',"..
                           ,'           |  | |
                          /              . |  `
                         /               | |   |
            __          .                | |    .
       _   |  `. ---.   |                | j    |
      / `-._|   `Y   |  |                |.     |
     _`.    ``    |   | |..              '      |,-'""7,....
     l     '-.     . , `|  | , |`. , ,  /,     ,'    '/   ,'_,.-.
     `-..     `-.  : :     |/ `   ' "|,' | _  /          '-'    /___
      |"' __.,.-`.: :        /   /._    l'.,'                       /
       `--,   _.-' `".           /__ `'-.' '         .             |
       ,---..._,.-------"--.__..----,-.'   .  /    .'   ,.--      /
       |                          ,':| /    | /     ;.,-'--      ,.-
       |     .---.              .'  :|'     |/ ,.-='"-.`"`' _   -.'
       /    |    /               `. :|--.  _L,"---.._        "----'
     ,' `.  |_ ,'           _,     `''   ``.-'       `-  -..___,'
    . ,.  .   `   __     .-'  _.-           `.     .__    |
    |. |`        "  ;   !   ,.  |             `.    `.`'---'
    ,| |C|       ` /    | ,' |(]|            -. |-..--`
   /  "'--'       '      /___|__]        `.  `- |`.
  .       ,'                   ,   /       .    `. |
    |                      .,-'  ,'         .     `-.
     x---..`.  -'  __..--'"/---"  ,-.      |   |   |
    / |--._'-.,.--'     _`-    _. ' /       |     -.|
   ,   .   `-..__ ...--'  _,.-' | `   ,.-.  ;   /  '|
  .  _,'         '"-----""      |    `   | /  ,'    ;
  |-'  .-.    `._               |     `._// ,'     /
 _|    `-'   _,' "`--.._________|        `,'    _ /.
//|   ,-._.'"/|__,.   _,"     /_|__/`. /'.-.'.-/_,`-' 
`-"`"' v'    `"  `-`-"              `-'`-`  `'

		""")

	elif poke_name == "venusaur":
		print("""

			    _._       _,._
                        _.'   `. ' .'   _`.
                ,"-/`""-.-.,/. ` V'/-,`.,--/---."-..
              ,'    `...,' . ,| -----._|     `.   /  |
             `.            .`  -'`"" .._   :> `-'   `.|
            ,'  ,-.  _,.-'| `..___ ,'   |'-..__   .._ L|
           .    | _ -'   `-'     ..      `.-' `.`-.'_ .|
           |   ,',-,--..  ,--../  `.  .-.    , `-.  ``.
           `.,' ,  |   |  `.  /'/,,.|/  |    ||   |
                `  `---'    `j   .   |  .     '   j
              ,__`"        ,'|`'|_/`.'|'        ||-'-, _,.
       .--...`-. `-`. /    '- ..      _,    // ,' .--"'  ,'".
     _'-""-    --  _`'-.../ __ '.'`-^,_`-"-------....__  ' _,-`
   _.----`  _..--.'        |  "`-..-" __|'"'         .""-. ""'--.._
  /        '    /     ,  _.+-.'  ||._'   ----. .          `     .__|
 `---    /        /  / j'       _/|..`  -. `-`| |   |  |   `.  | `-..
," _.-' /    /` ./  /`_|_,-"   ','|       `. | -'`._,   L  | .  `.   |
`"' /  /  / ,__...-----| _.,  ,'            `|----.._`-.|' |. .` ..  .
   /  '| /.,/    |--.._ `-,' ,          .  '`.'  __,., '  ''``._ | |`,'
  /_,'---  ,     |`._,-` | //  / . /    `._,  -`,  / / _   |   `-L -
   /       `.     ,  ..._ ' `_/ '| |/ `._'       '-.'   `.,'     |
  '         /    /  ..   `.  `./ | ; `.'    ,"" ,.  `.    |      |
   `.     ,'   ,'   | | |  |       "        |  ,' |   |    `    ,L
   /|`.  /    '     | `-| '                  /`-' |    L    `._/  |
  / | .`|    |  .   `._.'                   `.__,'   .  |     |  (`
 '-""-'_|    `. `.__,._____     .    _,        ____ ,-  j     ".-'"'
        |      `-.  |/.    `"--.._    _,.---'""|/  "_,.'     /-'
         )        `-._ '-.        `--"      _.-'.-""        `.
        ./            `,. `".._________...""_.-"`.          _j
       /_|.__,"".   ,.'  "`-...________.---"     .".   ,.  / |
              |_/""-'                           `-'--(_,`"`-`
              	""")


	elif poke_name == "flareon":
		print("""

		         /|     '
                        / `.  ,'|,-.____
                       /    `'  `       `""----...,
             .    ,__.'                        .-'._
            / |   ' .'                   ,_         `'`--.._
         _.'  . ,'                        `.`-._            `'.
        |      `                            .  .`-._,"'--._    `-.
     ,_.'     `                              `. .`._`.     `-._   '
      .                                     ..'  `. `.`.       `-. `.
      |                                       `.   `. `.`.        `. |
      |                                       ,',.'"-|  | `.         `
    ,-'                                       /     ."_  `  |
     .                              '`._ ,.  /      |  '  `. |
 ..._)                               |  "  `.        `-'.  |  .
   |       '.---.._'._  ."'-._     .'      |            `.|  '
    `.         `._ .._ `-'     `.`-.|       '              ` /
      `.          `-. `. `-.__   '-  `._     |              |.
       L_            `._ `.   `"--..__  `"-../|             ||-.,|
         `.'            `-.`.         `-._     `-._       .' |`. /
            .           _..`.`.._       ..`      __`"-..-'   |.'  '-'
            /___     ."'     `-._`"----"'   `  .( )`.          `.  .
                -.,./      `""   `""'""'`--.   `._   `.        /    |
                   /        ,               `._   `""'  _____.'      '
                             .                 `._      "...'       /
                  .         .'                    `""-----'        ' _
                  '         `-.                                    .'
                ,'            /                                   _,
               /         _..-"|"--..                             |
              /       ."'     |  .'.,----,                  ,.-'"|
             .      ,'        |     |   `--'.        __...-"`...-'
             '     /          '      |       `-----"'
            /     '            .      |        |
           .       .           '._,'_.'`.       |
           '._.  ).'                    `        `.
              `"'                        |         `
                                          `.   .   ,'
                                            `"-'--'
                                            """)

	elif poke_name == "vaporeon":
		print("""
			             ,,~",
                       )    "-"-,,,--~~",~-,,_   ,~",-" |
                      ,/||,"~,,_'|"-, _,|     ",-",,-"   '|
                  ,,~"    "-,_ "-|,'|"  "'~~-,-";;/,,-~",/
                /"-,,   ,,-"' "'~--,||  |"'~--"~,,~"   ,-"/,
               /     "-/ ,-"'~--,,;"~'  |   ,~"|,,,--~,/   "-,
              /       / /          "~-,,|  (o   |  |,,-"--~~"`"`,
           ,-" __,,-~' /     _,,---,        |_,/    |          |
  _,,-_~",-"---~~"`"~~|    (     o  "~,    ,-~,      /~--,,_   '|
~"~--,,_          _,,-~'|    "~-,,,--~"    "~"      /       "~-,,|
        "~,   ,,~"     ,-"/,                      ,/        ,-"     _______
           "~',~~--,,-"_,,-~"~--,,_          _,-""~,      ,/~~~~~"`"   , -,"-,
              "-,   ,-"          / "`"`"`"|'        "-,   /          ___,),,"-'
                 |,/            /          |      ____,|-"    ,,-~"`"
                    "'~~,-,,_  /     ___    | ,,~" _______,,-~"
                         | | "-'-,-~"-, "~--""    '|
                         | |   -"       |         '|
                        /  /   |   |   ),)          |
                        /  |    "~-"-,"              |
                       /    '|,    _/                 |
                      /     ___"`"`"                  |
                    ,/ ,,~"   "'~,                   /
                  ,/  /           "-,               /,
                 ,-" /               |            ,/  |
              ,-"   |                 |       ,,-"    '|
            ,-"    |                   |   ,,-"         |
          ,-"       |                  | ,~"            |
        ,-"          |                 /               /
      ,-"             "-,            ,/,              /
      /                  "~,,__     ,," /           ,"
     /                      |  "`"`"   ||       ,,~"
     /                      ,|         | |       |
     |                    ,/  | |     /  |      |              __,,--~,"
     |                   /     "~"~--"    |_      |    ,,--~"`"         /
     |                  /                   |      | /,,~"             /
      |                ,/                   |      | |                |
       |               |                    |   /  /'                /
        |              |                    ,"~"-'                  /
          |,           |                  ,/                    ,-"
           "-,          '|               /           ______,,-"          __,,--,
              "-,         "-,           /    _,,-~"`"       "`"`"`"`"`"`"      /
                 "~-,,_     "'~~-------~"                                   ,-"
                       "'~~--------------,,_                             ,-"
                                            "~,,                     ,,-"
                                                "~--,,,__      __,,~"
                                                         "`"`"`"
                                                         """)
	elif poke_name == "leafeon":
		print("""

			.' .
                   .| '|
           _...___/`'   .
         ,'             |
     ,|,"             )/|                             , .
    / |              / , .                            |` |
   /            ...-'  ',                              .  |
  .           ,>      .                                |   |
  |          .'   ___`,                  .'  ,--.._,.-'/  ,'
..|          |.-"', /                  ,' | /       ."'   '.
| '          |  ,'//                   .'  "    __,._'    |
 | `         /."_/'_,                 '.       /         _'
  `.|     _,'   |.`  ) ,^.              `     '       ,-"
    |.  .'  _   | `. '-  `,            , |     `.    ,-
    | `w  ," |  |   |   .'   _,_ :"'. / 7 . ,`..'   .'
    '|    `.'  /     |   `-'"   `   _:_,.}|  :  _. ,'
     |       .'       `-.      _,.-"       `-+-`  '
     |       |           ``--"'               `.
     |   .- .                                   |
      `.._,":                                    |
            '                                    `.  '-7
             |                                  .'`-"  :
              |                        .        `      `-'
             j |                       `.        `.     |
             |  `.  |      .^,'.       ,.+        :    _'
             |   |`.|      |    |,  ,-'  :`.       |  /_.,
            /    |  |     /     .,-'.     `.`.      V  /
           /    .' j     / _._,"     `      ':`.     . (
          /    /,-"|    j  `.         `-.    |  .    |/
          .   `'   |    |    7           |   |   |   |
           `.   .  |    |  v'            |  .'   |   |
             `.  `.|   j'.'              |  |    |  j
               |   |   |                j   |   j   |
                `.j   /|                |_,j    |  j
                  /  /`"              ,"   |    '  |
                 /  j                 '_,.-'   /.-'|
                |   |                         /__.-'
               .'`-.'
              /    |
              `----' 
              """)










