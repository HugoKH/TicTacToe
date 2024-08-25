import random
import winningtriples as w

class Player():
    
    def __init__(self, symbol: str = random.choice(["X", "o"])):
        """
        Initializes a Player with a given symbol.
        
        symbol: The symbol to be assigned to the player. Must be 'x' or 'o'.
        Raises ValueError if symbol is not 'x' or 'o'.
        """
        self._empty_fields: list = w.full_field
        self._symbol = None
        self._set_symbol(symbol)
        self._fields: list = []
        self._is_winnable: bool = True

    def get_symbol(self) -> str:
        """
        Returns the current symbol of the player.
        """
        return self._symbol
    
    def _set_symbol(self, value: str) -> None:
        """
        Sets the symbol for the player.
        
        value: The symbol to be set. Must be 'x' or 'o'.
        Raises ValueError if value is not 'x' or 'o'.
        """
        if value.lower() in ['x', 'o']:
            self._symbol = value.lower()
        else:
            raise ValueError("Symbol must be 'x' or 'o'.")

    def get_not_symbol(self):
        """
        Returns the not used symbol.
        Used for 1. Version of TicTacToe
        """
        if self._symbol == "x":
            return "o"
        else:
            return "x"

    def __repr__(self):
        """
        Returns Player symbol
        """
        return f"Player(symbol='{self._symbol}')"
    
    def add_field(self, intfield: int, empty_fields: bool = False):
        if empty_fields==True:
            self._empty_fields.append(intfield)
        else:
            self._fields.append(intfield)
        
    def get_fields(self, only_newest:bool = False, empty_fields: bool = False):
        if only_newest == True:  
            if empty_fields == False:
                return self._fields[-1]
            elif empty_fields == True:
                return self._empty_fields[-1]
        elif only_newest == False:
            if empty_fields == False:
                return self._fields
            elif empty_fields == True:
                return self._empty_fields
            
    def remove_fields(self, intfield: int, empty_fields: bool = False):
        if empty_fields==True:
            self._empty_fields.remove(intfield)
        else:
            self._fields.remove(intfield)
    
    def set_winnable_status(self, winnable: bool = True):
        """
        Sets the winnable bool
        """
        self._is_winnable = winnable

    def get_winnable_status(self):
        """
        Returns the winnable bool
        """
        return self._is_winnable
    
debug: bool = False
class Coordinaten():     
    
    def __init__(self):
        self._int_cords: int = None
        self._cords: tuple = None
        self._exception: bool = False
        
    def switch(self, cords: tuple):
        """
        Returns a integer which contains the right index for the ttt field given the coordinates
        """
        x_cords = cords.__getitem__(0)
        x_int: int
        y_cords = cords.__getitem__(1)
        y_int: str
                            
        if y_cords == 1:
            y_int = 19
        elif y_cords == 2:
            y_int = 10
        elif y_cords == 3:
            y_int = 1
        else:
            print("heftig was kaputt gegangen")
            self._exception = True
        
        if x_cords == 1:
            x_int = 1
        elif x_cords == 2:
            x_int = 3
        elif x_cords == 3:
            x_int = 5
        else:
            print("heftig was kaputt gegangen")
            self._exception = True
            
        self._int_cords = y_int + x_int
        return self._int_cords
    
    def str2intcoords(self, str_cords: str):
        """
        Returns the given string to int with the right cords for the field #type coordinates
        Also sets _exception to False, so get_exception returns False
        """
        self._exception = False
        
        if (len(str_cords) == 3 and 
            str_cords[1] == ' '):

                # Try to split and convert to integers
                try:
                    # Remove the parentheses and split by the space
                    x_str, y_str = str_cords.split(' ')
                    
                    # Convert to integers
                    x = int(x_str)
                    y = int(y_str)
                    
                    if x >= 4 or x <= 0 or y >= 4 or y <= 0:
                        print("Die Eingabe entspricht nicht dem Koordinaten Format!")
                        self._exception = True
                    else:
                        self._cords = (x, y)
                        
                        self.switch(self._cords)
                                                      
                        if debug:
                            print(self._cords)
                    
                
                except:
                    print("Die Eingabe entspricht nicht dem Koordinaten Format!(except)")
                    self._exception = True
                    
                    
        else:
            print("Die Eingabe entspricht nicht dem Koordinaten Format!")
            self._exception = True
                    
        return self._int_cords
    
    def get_exception(self):
        return self._exception