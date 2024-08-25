#used to determine all winning triples in intcoord format for first version of this game

import player_class as p
import winningtriples
cords = p.Coordinaten()
wt = winningtriples.winning_triples
winning_triples_ints = []
#winning_triples_ints.append

for tuples in range(8):
    for items in range(3):
        win = cords.str2intcoords(wt[tuples].__getitem__(items))
        print(win)
    

