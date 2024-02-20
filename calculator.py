from tkinter import *

class Window:
    def __init__(self,width):
        self.root=Tk()
        self.root.title('Calculator')
        self.ent=Entry(self.root,width=width,borderwidth=5)
        self.ent.grid(row=0,column=0,columnspan=4)
        self.running=False
        self._init_number_buttons()
        self._init_basic_math_buttons()
        self._init_show_eq(width)
    def _init_number_buttons(self):
        self.button1=Button(self.root,text='1',padx=40,pady=20,command=lambda: self.button_click(1))
        self.button2=Button(self.root,text='2',padx=40,pady=20,command=lambda: self.button_click(2))
        self.button3=Button(self.root,text='3',padx=40,pady=20,command=lambda: self.button_click(3))
        self.button4=Button(self.root,text='4',padx=40,pady=20,command=lambda: self.button_click(4))
        self.button5=Button(self.root,text='5',padx=40,pady=20,command=lambda: self.button_click(5))
        self.button6=Button(self.root,text='6',padx=40,pady=20,command=lambda: self.button_click(6))
        self.button7=Button(self.root,text='7',padx=40,pady=20,command=lambda: self.button_click(7))
        self.button8=Button(self.root,text='8',padx=40,pady=20,command=lambda: self.button_click(8))
        self.button9=Button(self.root,text='9',padx=40,pady=20,command=lambda: self.button_click(9))
        self.button0=Button(self.root,text='0',padx=40,pady=20, command=lambda: self.button_click(0))
        self._display_num_buttons()
    def _display_num_buttons(self):
        self.button1.grid(row=4,column=0)
        self.button2.grid(row=4,column=1)
        self.button3.grid(row=4,column=2)
        self.button4.grid(row=3,column=0)
        self.button5.grid(row=3,column=1)
        self.button6.grid(row=3,column=2)
        self.button7.grid(row=2,column=0)
        self.button8.grid(row=2,column=1)
        self.button9.grid(row=2,column=2)
        self.button0.grid(row=5,column=1)
    def _init_basic_math_buttons(self):
        self.button_add=Button(self.root,text='+',padx=40,pady=20,command=lambda: self.hold('+'))
        self.button_subt=Button(self.root,text='-',padx=40,pady=20,command=lambda: self.hold('-'))
        self.button_mult=Button(self.root,text='*',padx=40,pady=20,command=lambda: self.hold('*'))
        self.button_div=Button(self.root,text='/',padx=40,pady=20,command=lambda: self.hold('/'))
        self.button_equals=Button(self.root,text='=',padx=100,pady=20,command=self.equals)
        self.button_clear_all=Button(self.root,text='ca',padx=100,pady=20,command=self.clear_all)
        self.button_clear_entry=Button(self.root,text='ce',padx=100,pady=20,command=self.clear_entry)
        self._display_basic_math_buttons()
    def _display_basic_math_buttons(self):
       self.button_add.grid(row=2,column=3)
       self.button_subt.grid(row=3,column=3)
       self.button_mult.grid(row=4,column=3)
       self.button_div.grid(row=5,column=3) 
       self.button_equals.grid(row=6,column=4)
       self.button_clear_all.grid(row=2,column=4) 
       self.button_clear_entry.grid(row=3,column=4) 
    def _init_show_eq(self,width):
        self.show_eq_text= StringVar()
        self.show_eq=Label(self.root,width=width,textvariable=self.show_eq_text)
        self.show_eq.grid(row=1,column=0,columnspan=4)
    def button_click(self,button):
        current=self.ent.get()
        self.ent.delete(0,END)
        self.ent.insert(0,str(current)+str(button))
    def clear_entry(self):
        if len(self.ent.get())==0:
            self.clear_all()
        self.ent.delete(0,END)
    def clear_all(self):
        self.ent.delete(0,END)
        self.show_eq_text.set('')
    def hold(self,button):
        self.held=str(self.ent.get())
        self.held_sym=button
        self.clear_entry()
        self.show_eq_text.set(self.held+' '+self.held_sym)
    def equals(self):
        if self.ent.get()==0 and self.held_sym=='/':
            self.clear_entry()
            self.ent.insert(0,'ERROR: Divide by 0')
            return
        result=eval(self.held+self.held_sym+self.ent.get())
        self.clear_all()
        self.ent.insert(0,result)

    
def main():
    win=Window(50)
    win.root.mainloop()
main()