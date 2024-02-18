
from model import Model
from view import View


class Controller:
    
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        
    
    def main(self):
        self.view.run()
    
    def onBottonClick(self, caption):
        
        result = self.model.onBottonClick(caption)
        self.view.var.set(result)
    



if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
