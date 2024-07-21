from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("CALCULATOR")
        master.geometry("357x420+0+0")
        master.config(bg="grey")
        master.resizable(False, False)
        
        self.equation = StringVar()
        self.entry_value = ''
        
        Entry(width=17, bg="#ccddff", font=("arial", 20, "bold"), textvariable=self.equation).place(x=0, y=0)
        
        Button(width=11, relief="flat", bg="grey", height=4, text="(", command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, relief="flat", bg="grey", height=4, text=")", command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=11, relief="flat", bg="grey", height=4, text="%", command=lambda: self.show('%')).place(x=180, y=50)
        
        Button(width=11, relief="flat", bg="grey", height=4, text="1", command=lambda: self.show(1)).place(x=0, y=125)
        Button(width=11, relief="flat", bg="grey", height=4, text="2", command=lambda: self.show(2)).place(x=90, y=125)
        Button(width=11, relief="flat", bg="grey", height=4, text="3", command=lambda: self.show(3)).place(x=180, y=125)
        
        Button(width=11, relief="flat", bg="grey", height=4, text="4", command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, relief="flat", bg="grey", height=4, text="5", command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, relief="flat", bg="grey", height=4, text="6", command=lambda: self.show(6)).place(x=180, y=200)
        
        Button(width=11, relief="flat", bg="grey", height=4, text="7", command=lambda: self.show(7)).place(x=0, y=275)
        Button(width=11, relief="flat", bg="grey", height=4, text="8", command=lambda: self.show(8)).place(x=90, y=275)
        Button(width=11, relief="flat", bg="grey", height=4, text="9", command=lambda: self.show(9)).place(x=180, y=275)
        
        Button(width=11, relief="flat", bg="grey", height=4, text="0", command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, relief="flat", bg="pink", height=4, text=".", command=lambda: self.show('.')).place(x=180, y=350)
        
        Button(width=11, relief="flat", bg="purple", height=4, text="+", command=lambda: self.show('+')).place(x=270, y=275)
        Button(width=11, relief="flat", bg="yellow", height=4, text="-", command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=11, relief="flat", bg="green", height=4, text="/", command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=11, relief="flat", bg="blue", height=4, text="*", command=lambda: self.show('*')).place(x=270, y=125)
        
        Button(width=11, relief="flat", bg="cyan", height=4, text="=", command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text="C",bg ="grey" ,  command=self.clear).place(x=0, y=350)
    
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
    
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)
    
    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except:
            self.equation.set("")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()
