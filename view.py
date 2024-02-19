from tkinter import ttk
import tkinter as tk

class View(tk.Tk):
    
    PAD = 10
    BOTTOM_CAPTIONS = [
        "","", "", "DEL",
        "(", ")", "^", "+",
        "7", "8", "9", "-",
        "4", "5", "6", "*",
        "1", "2", "3", "/",
        "C", "0", ".", "="
    ]
    FUNCTIONS = {
        "exp": "exp()",
        "ln": "ln()",
        "log10": "log10()",
        "log2": "log2()",
        "sqrt": "sqrt()"
    }
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Calculator")
        
        self.var = tk.StringVar()
        self.function_var = tk.StringVar()
        self.history_var = tk.StringVar()
        
        self.create_widgets()
        

    def create_widgets(self):
        
        self._create_frame()
        
        self._create_entry()
        
        self._create_buttons()
        
        self._create_combobox()
        
        self._create_history_button()
    
    def _create_frame(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=self.PAD, pady=self.PAD)
    
    def _create_entry(self):
        entry = ttk.Entry(self.frame, justify='right' 
                          ,textvariable=self.var)
        
        entry.pack(fill="x", expand=True)
        
    def _create_buttons(self):
        keypad = ttk.Frame(self.frame)
        keypad.pack(fill="both", expand=True)
        
        for i, caption in enumerate(self.BOTTOM_CAPTIONS):
            button = ttk.Button(keypad, text=caption, command=lambda 
                                c=caption: self.controller.onBottonClick(c))
            row = i // 4
            column = i % 4
            button.grid(row=row, column=column, sticky="nsew")
            keypad.rowconfigure(row, weight=1)
            keypad.columnconfigure(column, weight=1)
            
            # check if the button is an operator button
            if caption in "+-*/":  
                button.bind("<Button-1>", lambda e, b=button: b.config(style="Operator.TButton"))  
                # change the color of the button when clicked
                button.bind("<ButtonRelease-1>", lambda e, b=button: b.config(style="TButton"))
    
    def _create_combobox(self):
        functions = list(self.FUNCTIONS.keys())
        combobox = ttk.Combobox(self.frame, values=functions, 
                                textvariable=self.function_var)
        
        combobox.pack(fill="x", expand=True)
        combobox.bind("<<ComboboxSelected>>", lambda e: 
                    self.controller.onFunctionSelect(combobox.get()))
        # Add a binding to update the entry when a combobox selection is made
        combobox.bind("<<ComboboxSelected>>", lambda e: 
                    self.update_entry_from_combobox(combobox.get()))

    def update_entry_from_combobox(self, value):
        self.var.set(value)
        self.update_display(value)
        
    def _create_history_button(self):
        history_button = ttk.Button(self.frame, text="History", command=self.controller.show_history)
        history_button.pack(fill="x", expand=True)
    
    def update_display(self, value):
        self.var.set(value)
            
    def run(self):
        self.mainloop()
