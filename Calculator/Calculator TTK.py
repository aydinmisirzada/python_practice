from tkinter import *
from tkinter import ttk
from functools import partial

class Calculator():
    num1, num2 = 0, 0
    res = ""
    op_triggered = False
    
    def __init__(self):
        self.operations = {'+': False,'-': False,'*': False,'/': False,'=': False,'AC': False}
        
    def math_op(self,op):
        for key, val in self.operations.items():
            if val:
                self.operations[key] = False
        if op == 'AC':
            print('ac trig')
            self.num1 = 0
            self.num2 = 0
            self.res = ""
            field_value.set(self.res)
            self.op_triggered = False
            return
        self.op_triggered = True
        self.operations[op] = True
        print(self.operations)
    
    def num_entered(self,num,*args):
        if self.op_triggered:
            self.num2 = num
            field_value.set(num)
        else:
            self.num1 = num
            field_value.set(num)
            self.op_triggered = False
        print(self.num1,self.num2)
            
    def calculate(self):
        for key, val in self.operations.items():
            if val:
                self.num1 = eval(f"{self.num1} {key} {self.num2}")
                self.num2 = 0
                self.res = str(self.num1)
        field_value.set(self.res)
            
window = Tk()
window.title("My Calculator - Press Q to exit")
window.resizable(width=False,height=False)

calc = Calculator()

screen_width = int(window.winfo_screenwidth() / 2)
screen_height = int(window.winfo_screenheight() / 2)

window.geometry(f"480x220+{screen_width-250}+{screen_height-200}")

frame = ttk.Frame(window,padding="0")
frame.grid(column=0,row=0,sticky=(N,W,E,S))

window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)

style = ttk.Style()
style.configure('Op.TButton',foreground='orange')
style.configure('TEntry',font="Serif 18",padding=10)
style.configure('TButton',font="Serif 15",padding=10)

field_value = StringVar()
field = ttk.Entry(frame,width=50,textvariable=field_value)
field.grid(column=0,columnspan=4,row=0)

button7 = ttk.Button(frame,text='7',command=lambda: calc.num_entered(7))
button7.grid(column=0,row=1)

button8 = ttk.Button(frame,text='8',command=lambda: calc.num_entered(8))
button8.grid(column=1,row=1)

button9 = ttk.Button(frame,text='9',command=lambda: calc.num_entered(9))
button9.grid(column=2,row=1)

button_div = ttk.Button(frame,text='/',style='Op.TButton',command=lambda: calc.math_op('/'))
button_div.grid(column=3,row=1)
###############
button4 = ttk.Button(frame,text='4',command=lambda: calc.num_entered(4))
button4.grid(column=0,row=2)

button5 = ttk.Button(frame,text='5',command=lambda: calc.num_entered(5))
button5.grid(column=1,row=2)

button6 = ttk.Button(frame,text='6',command=lambda: calc.num_entered(6))
button6.grid(column=2,row=2)

button_mul = ttk.Button(frame,text='*',style='Op.TButton',command=lambda: calc.math_op('*'))
button_mul.grid(column=3,row=2)
###############
button1 = ttk.Button(frame,text='1',command=lambda: calc.num_entered(1))
button1.grid(column=0,row=3)

button2 = ttk.Button(frame,text='2',command=lambda: calc.num_entered(2))
button2.grid(column=1,row=3)

button3 = ttk.Button(frame,text='3',command=lambda: calc.num_entered(3))
button3.grid(column=2,row=3)

button_plus = ttk.Button(frame,text='+',style='Op.TButton',command=lambda: calc.math_op('+'))
button_plus.grid(column=3,row=3)
###############
buttonAC = ttk.Button(frame,text='AC',command=lambda: calc.math_op('AC'))
buttonAC.grid(column=0,row=4)

button0 = ttk.Button(frame,text='0',command=lambda: calc.num_entered(0))
button0.grid(column=1,row=4)

button_eq = ttk.Button(frame,text='=',style='Op.TButton',command=lambda: calc.calculate())
button_eq.grid(column=2,row=4)

button_min = ttk.Button(frame,text='-',style='Op.TButton',command=lambda: calc.math_op('-'))
button_min.grid(column=3,row=4)

for i in range(10):
    window.bind(str(i),partial(calc.num_entered,i))
    
window.bind('=',lambda x: calc.calculate())
window.bind('<Return>',lambda x: calc.calculate())
window.bind('+',lambda x: calc.math_op('+'))
window.bind('-',lambda x: calc.math_op('-'))
window.bind('*',lambda x: calc.math_op('*'))
window.bind('/',lambda x: calc.math_op('/'))
window.bind('c',lambda x: calc.math_op('AC'))

window.bind('q',quit)
window.mainloop()
