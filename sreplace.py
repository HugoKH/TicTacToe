class SReplace():
    
    def __init__(self) -> None:
        pass
    
    #replaces a single item in wholestr with newstr at index and returns the edited string
    def sreplace(self, wholestr: str, newstr: str, index: int):
        wholestr_list = list(wholestr)
        wholestr_list.pop(index)
        wholestr_list.insert(index, newstr)
        wholestr_newstr = "".join(wholestr_list)
        
        return wholestr_newstr
