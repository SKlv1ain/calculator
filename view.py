from tkinter import ttk
import tkinter as tk

class View(tk.Tk):
    
    PAD = 10
    BOTTOM_CAPTIONS = [
        "mod","expo", "sqrt", "DEL",
        "(", ")", "^", "+",
        "7", "8", "9", "-",
        "4", "5", "6", "*",
        "1", "2", "3", "/",
        "C", "0", ".", "="
    ]
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Calculator")
        
        self.var = tk.StringVar()
        
        self.create_widgets()
        

    def create_widgets(self):
        self._create_frame()
        self._create_entry()
        self._create_buttons()

    def _create_frame(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=self.PAD, pady=self.PAD)
        
    def create_label(self):
        label = ttk.Entry(self.frame, justify='right' ,textvariable=self.var, state='disabled')
        label.pack(fill="x", expand=True)
        
    
    def _create_entry(self):
        entry = ttk.Entry(self.frame, justify='right' ,textvariable=self.var)
        entry.pack(fill="x", expand=True)
        
    def _create_buttons(self):
        keypad = ttk.Frame(self.frame)
        keypad.pack(fill="both", expand=True)
        
        for i, caption in enumerate(self.BOTTOM_CAPTIONS):
            button = ttk.Button(keypad, text=caption, command=lambda c=caption: self.controller.onBottonClick(c))
            row = i // 4
            column = i % 4
            button.grid(row=row, column=column, sticky="nsew")
            keypad.rowconfigure(row, weight=1)
            keypad.columnconfigure(column, weight=1)

    
    def update_display(self, value):
        self.var.set(value)
        
            
    def run(self):
        self.mainloop()
