import player_class as p
import winningtriples as w
import random
Player = p.Player
player = p.Player()

debug = False

class AI():
    def __init__(self) -> None:
        self._enemy_winning_fields: list = []
    
    def simulate_inputV1(self, combined_empty_fields: list):
        """
        Returns the AIs turn by getting the other players empty fields and choosing a random one of those
        """
        return random.choice(combined_empty_fields)
    
    def simulate_inputV2(self, sim_player: Player, main_player: Player, combined_empty_fields: list):
        """
        Returns the AIs turn, which:
        1. tries to block the enemys possible wins
        2. tries to win itself
        """
        matching_count: dict = {}
        matching_count_myself: dict = {}
        #matching_count_highest: dict = {}
        
        if debug:
            main_player.add_field(2)
            main_player.add_field(11)
            main_player.add_field(24)
            #main_player.add_field(22)
            sim_player.add_field(20)
        #checks every winning triple and assigns the fields which the player set a symbol to, to this triple
        for triples in w.winning_triples_ints:
            matching_count.setdefault(triples, [])
            matching_count_myself.setdefault(triples, [])
            #wie viele felder aus main_player.get_fields() pro winning_triple_ints enthalten sind 
            #und welche enthalten sind und welche nicht im triple enthalten sind
            for fields in main_player.get_fields():
                if fields in triples:   
                    matching_count[triples].append(fields)
            
            #same thing for own player, to win myself if possible       
            for fields in sim_player.get_fields():
                if fields in triples:   
                    matching_count_myself[triples].append(fields)
                    
        #for triples in w.winning_triples_ints:
        #   print(len(matching_count[triples]))
        
        #checks amount of fields there are to a possible win and block the path
        #print(matching_count)
        matching_count = dict(sorted(matching_count.items(), key=lambda item: len(item[1]), reverse = True))
        matching_count_myself = dict(sorted(matching_count_myself.items(), key=lambda item: len(item[1]), reverse = True))
        #print(matching_count)
        skip_count: int = 0
        skip_count_myself: int = 0
        
        for values in matching_count_myself.values():
            #print(values)
            skip_values_myself = False
            if skip_count_myself == 4:
                #print("Ich kann nichts mehr tun um zu gewinnen...")
                return ai.simulate_inputV1(combined_empty_fields)
            elif len(values) == 2:
                #welche felder fehlen zum gewinn
                for triples in w.winning_triples_ints:
                    if skip_values_myself:
                        break
                    if all(elem in triples for elem in values):
                        #print(f"triples: {triples}\nvalues: {values}")

                        for ints in triples:
                            if ints not in values:
                                if ints not in main_player.get_fields():    
                                    missing_int_to_win = ints
                                    #print(f"nicht in values: {ints}")
                                    #print(missing_int_to_win)
                                    skip_count_myself = 0                                      
                                    return missing_int_to_win  
                                else:
                                    #print(f"{ints} already blocked")
                                    skip_values_myself = True  # Setze das Flag, um die äußere Schleife neu zu starten
                                    skip_count_myself += 1
                                    #print(skip_count)
                                    break  # Breche die innere Schleife ab

                        if skip_values_myself:
                            break #zum äußersten loop zurückkehren  
        
        for values in matching_count.values():
            #print(values)
            skip_values = False
            if skip_count == 4:
                #print("Ich kann nichts mehr tun um zu gewinnen...")
                return ai.simulate_inputV1(combined_empty_fields)
            
            if len(values) == 3:
                print("Ich kann nichts mehr tun um zu gewinnen...")
                return ai.simulate_inputV1(combined_empty_fields)
            elif len(values) == 2:
                #welche felder fehlen zum gewinn
                for triples in w.winning_triples_ints:
                    if skip_values:
                        break
                    if all(elem in triples for elem in values):
                        #print(f"triples: {triples}\nvalues: {values}")

                        for ints in triples:
                            if ints not in values:
                                if ints not in sim_player.get_fields():    
                                    missing_int_to_win = ints
                                    #print(f"nicht in values: {ints}")
                                    #print(missing_int_to_win)
                                    skip_count = 0                                      
                                    return missing_int_to_win  
                                else:
                                    #print(f"{ints} already blocked")
                                    skip_values = True  # Setze das Flag, um die äußere Schleife neu zu starten
                                    skip_count += 1
                                    #print(skip_count)
                                    break  # Breche die innere Schleife ab

                        if skip_values:
                            break #zum äußersten loop zurückkehren        
                                           
                        if debug:
                            print(f"ints: {ints}\nvalue: {values}\n zahl ist drinne")
                            
            elif len(values) == 1:
                if 6 not in main_player.get_fields() and 6 not in sim_player.get_fields():
                    return 6
                else:
                    ecken: list = [2, 6, 20, 24]
                    for fields in main_player.get_fields()+sim_player.get_fields():
                        if fields in ecken:
                            ecken.remove(fields)
                    if ecken == []:
                        #print("alarmmm")
                        return ai.simulate_inputV1(combined_empty_fields)                        
                    else:
                        return random.choice(ecken)
                #temp, while winning is not programmed yet
            else:
                #temp, while aiming for a win isnt programmed yet
                return 6
                    
        

                
ai = AI()
#ai.simulate_inputV2(Player("x"), Player("o"))