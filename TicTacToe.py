debug = False

import random
import winningtriples as w
import sreplace
sr = sreplace.SReplace()
import player_class as p
Coords = p.Coordinaten()
Player = p.Player
import AI
ai = AI.AI()

players = [Player("x"), Player("o")]

ttt_field = "3 - - -|\n2 - - -|\n1 - - -|\n0 1 2 3|\n"
       #x1 = index add 1; x2 index add 3; x3 index add 5 
       #y1 = index 21, y2 = index 11, y3 = index 1
       #1 2 = index 12, 2 3 = index 4, 3 1 = index 26
       
beginner: Player 
not_beginner: Player
rnd_beginner: bool = False
        
unoccupied_fields: list = w.full_field
player_unoccupied_fields: list = w.full_field
        
beginner_input = input("Wer fängt an? (x/o/r(random))\n")	
if beginner_input.lower() == "x":
    beginner = players[0]
elif beginner_input.lower() == "o":
    beginner = players[1]
elif beginner_input == "r":
    rnd_beginner = True
    beginner = random.choice(players)
else:
    print("Invalid Input")
    KeyboardInterrupt
    
def TicTacToe(field: str, Beginner: Player, game_is_running = False): 
    Players: list = [Beginner, (players.__getitem__(1 - players.index(Beginner)))]
    current_player: Player
    if rnd_beginner == False:
        current_player = Beginner
    else:
        current_player = random.choice(Players)
        
    player_combined_fields: list = w.full_field
    
    while game_is_running:
        
        if current_player == Beginner:
            raw_input = input(f"\nSpieler({current_player.get_symbol()}) ist an der reihe, wo möchtest du dein {current_player.get_symbol()} setzen?\n"+
                                f"gebe die coordinaten in diesem Format ein: x y\n{field}")
            print(" ")
            coords_input = Coords.str2intcoords(raw_input)
        else:
            coords_input = ai.simulate_inputV2(current_player, players.__getitem__(1 - players.index(current_player)), player_unoccupied_fields)
            print(f"KI({current_player.get_symbol()}) ist dran")
        
            
         
        #check if player_class threw an exception
        if Coords.get_exception() == True:    
            continue
        elif Coords.get_exception() == False:                 
            field_cordsitem = field.__getitem__(coords_input)    
            #check if place in field is already occupied
            if field_cordsitem == "x" or field_cordsitem == "o":
                print("Das Feld ist bereits beglegt!")
                continue  
            else:
                field = sr.sreplace(field, current_player.get_symbol(), coords_input)
                current_player.add_field(coords_input)
                player_combined_fields.append(current_player.get_fields(True))
                #print(f"{unoccupied_fields} {current_player.get_fields(True)}\n{current_player.get_fields(True)}")
                player_unoccupied_fields.remove(current_player.get_fields(True))
                current_player.remove_fields(current_player.get_fields(only_newest=True), True)
                
            #check if someone won
            for tuples in range(w.winning_triples_ints.__len__()):
                if debug:
                    print(f"pfields:{current_player.get_fields()} wints:{w.winning_triples_ints[tuples]} tuples:{tuples}\n unoccupied fields: {unoccupied_fields}")
                    print(f"{current_player.get_fields(False, True)} {current_player.get_fields(False, False)}")
                if all(elem in current_player.get_fields() for elem in w.winning_triples_ints[tuples]):
                    print(f"{current_player.get_symbol()} gewinnt!!!!")
                    #edits the field to mark the winning "lane"
                    for ints in w.winning_triples_ints[tuples]:                      
                        field = sr.sreplace(field, "*", ints)
                    #field = sr.sreplace(field, "  ", )
                    print(field)
                    game_is_running = False	
                    break
                
            #check if the field is fully occupied
            if player_combined_fields.__len__() == 9:
                if game_is_running == True:    
                    print("Unentschieden, durch volles Feld!")
                    print(field)
                    game_is_running = False
                    break
                
            #check if game is still winnable(by checking if win fields are not occupied, and if they are by other player)
            for tuples in range(w.winning_triples_ints.__len__()):
                if debug:
                    print(f"pfields:{current_player.get_fields()} wints:{w.winning_triples_ints[tuples]} tuples:{tuples}\ncombinedfields: {player_combined_fields}")
                    print(f"{current_player.get_fields(False, True)} {current_player.get_winnable_status()}")
                #check for current player
                if all(elem in current_player.get_fields(False, True)+current_player.get_fields() for elem in w.winning_triples_ints[tuples]):
                    current_player.set_winnable_status()
                    #print(current_player.get_fields(False, True)+current_player.get_fields())
                    break
                else:
                    current_player.set_winnable_status(False)
                    #print(current_player.get_fields(False, True)+current_player.get_fields())
                    
                #check for not current player
                if all(elem in players.__getitem__(1 - players.index(current_player)).get_fields(False, True)+players.__getitem__(1 - players.index(current_player)).get_fields() for elem in w.winning_triples_ints[tuples]):
                    players.__getitem__(1 - players.index(current_player)).set_winnable_status()
                    break
                else:
                    players.__getitem__(1 - players.index(current_player)).set_winnable_status(False)
                    
            if current_player.get_winnable_status() == False and players.__getitem__(1 - players.index(current_player)).get_winnable_status() == False:
                if game_is_running == True:
                    print("Unentschieden!!!")
                    print(field)
                    game_is_running = False
                    break                    
            
        else:
            print("debug: exception bool in player class not rightfully set")
        
        current_player = players.__getitem__(1 - players.index(current_player))
    
TicTacToe(ttt_field, beginner, True)