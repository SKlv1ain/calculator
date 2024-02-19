
# from model import Model
from view import View

from model import Model


class Controller:
    
    
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        
    def run(self):
        self.view.run()
    
    def onFunctionSelect(self, function):
        self.model.onFunctionSelect(function)
        self.view.function_var.set(function)
        self.view.var.set(self.model.current + self.view.function_var.get())
        
        
    def onBottonClick(self, caption):
        result = self.model.onBottonClick(caption)
        new_input = self.view.function_var.get() + result
        self.view.update_entry_from_combobox(new_input)
    
    def show_history(self):
        self.view.show_history(self.model.history)
 
