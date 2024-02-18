



class Model:
    
    def __init__(self) -> None:
        self._result = ""
        self._operator = ""
        self._previous = ""

    def onBottonClick(self, caption):
        
        if caption == "C":
            self._result = ""
            
        elif caption == "=":
            self._result = str(self._evaluate())
            
        elif caption == "DEL":
            self._result = self.delete()
            
        elif caption == ".":
            if "." not in self._result:
                self._result += caption
        
        elif isinstance(caption, int):
            self._result += str(caption)
        
        else:
            if self._result:
                self._previous = self._result
                self._operator = caption
                self._result = ""
            
        return self._result
    
    def delete(self):
        self._result = self._result[:-1]
        return self._result
    

    def _evaluate(self):
        return eval(self._previous + self._operator + self._result)