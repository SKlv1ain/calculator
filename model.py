from math import *
class Model:
    
    def __init__(self) -> None:
        self.current = ""
        self.last = "0"
        self.operator = ""
        self.reset = False
        self.history = {}
    
    def onFunctionSelect(self, function):
        if function != "=" and function != "C" and function != "DEL":
            self.add_string(function)
        elif function == "exp":
            self.current = "exp(" + self.current + ")"
        elif function == "ln":
            self.current = "ln(" + self.current + ")"
        elif function == "log10":
            self.current = "log10(" + self.current + ")"
        elif function == "log2":
            self.current = "log2(" + self.current + ")"
        elif function == "sqrt":
            self.current = "sqrt(" + self.current + ")"
        self.reset = True
    
    def onBottonClick(self, caption):
        if caption != "=" and caption != "C" and caption != "DEL":
            self.add_string(caption)
        elif caption == "C":
            self.current = ''
        elif caption == "DEL":
            self.current = self.current[:-1]
            if not self.current:
                self.current = ""
        elif caption == ".":
            self.onDot()
        elif caption == '^':
            self.onOperator("**")
        else:
            self.current = str(eval(self.current))
        return self.current
    
    def add_string(self, caption):
        self.current += str(caption)
        
    def calculate(self):
        self.current = str(eval(self.current))

            
    def onOperator(self, operator):
        if not self.operator:
            self.last = self.current
        else:
            self.onEqual()
        self.operator = operator
        self.reset = True
        
    def onClear(self):
        self.current = ""
    
    def onDel(self):
        self.current = self.current[:-1]
        if not self.current:
            self.current = ""
    
    def onEqual(self):
        if self.operator and self.last:
            self.current = str(eval(self.last + self.operator + self.current))
            self.last = "0"
            self.operator = ""
            self.reset = True
        
    def onDot(self):
        if self.reset:
            self.current = "0"
            self.reset = False
        if "." not in self.current:
            self.current += "."
    
    def __str__(self):
        return f"current: {self.current}, last: {self.last}, operator: {self.operator}, reset: {self.reset}"
    