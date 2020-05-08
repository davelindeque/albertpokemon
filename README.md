# albertpokemon
Pokemon Python Game 

Terminal-based Pokemon game as part of PM Onboarding training.

Interesting Notes:

- **ASCII art** added to improve user experience and create immediate mental association with the Pokemon universe (visual cues despite being terminal-based).
- **Pokemon Soundtrack:** Included simpleaudio to play WAV file of Pokemon soundtrack.  
- **PyInquirer** used for selection. 
- **Wild pokemon attack (disadvantage):** At present, the script results in the opposing player checking if they have advantage with a particular move, choosing that by default if they do. However, if the opposing player does not have an advantageous attack at their disposal, they will randomly select a move. This allows the possibility that they chose a move that embraces an element that the player's (user) Pokemon is comprised of. If this is the case, the wild Pokemon's attack will be disadvantaged by our strength, resulting in half damage (hitpoints = (int)/2 where int has range 1-3) dealt by attack. This "clumsy" choice of attack is an opponent weakness. We can either leave this inherent potential weakness, upgrade opponent attack logic or allow randomize when this logic is implemented by the opposition. The decision, in this regard, is influenced by the strength of opponent you are seeking to construct within the rules of the game.
- **Order of attack:** By default, whenever a battle commences, the player attacks first. An improvement can be implemented where the order in which players attack (user & wild opponent) is randomized.