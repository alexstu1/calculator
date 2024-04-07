from tkinter import *
from calculations import ExpTree
class Window:
    def __init__(self,width):
        self.root=Tk()
        self.root.title('Calculator')
        self.ent=Entry(self.root,width=width,borderwidth=5,justify=RIGHT)
        self.ent.grid(row=0,column=1,columnspan=4)
        self.ent.focus_set()
        self.running=False
        self._init_labelFrames()
        self._init_number_buttons()
        self._init_basic_math_buttons()
        self._init_show_eq(width)
        self._init_memory()
        self._init_history()
        self.clear_all()
    def _init_history(self):
        self.hist_button=Button(self.history_frame,text='History',padx=30,pady=10,command=self.swap_history)
        self.mem_button=Button(self.history_frame,text='Memory',padx=30,pady=10,command=self.swap_memory)
        self.hist_button.grid(row=0,column=0)
        self.mem_button.grid(row=0,column=1)
        self.no_mem=Label(self.history_frame,text='No numbers in memory!')
        self.no_hist=Label(self.history_frame,text='No history yet!')
        self.sub_frame_hist=LabelFrame(self.history_frame,borderwidth=5)
        self.sub_frame_hist.grid(row=1,column=0,columnspan=2,sticky=NS)
        self._is_hist=False
        self.hist_list=[]
        self.swap_history()
    def swap_history(self):
        self._is_hist=True
        self.update_mem_or_hist()
    def swap_memory(self):
        self._is_hist=False
        self.update_mem_or_hist()
    def update_mem_or_hist(self):
        self.sub_frame_hist.destroy()
        self.sub_frame_hist=LabelFrame(self.history_frame,borderwidth=0)
        self.sub_frame_hist.grid(row=1,column=0,columnspan=2,sticky=NS)
        self.no_hist.grid_forget()
        self.no_mem.grid_forget()
        if self._is_hist and len(self.hist_list)!=0:
            idx=0
            while idx<len(self.hist_list):
                lab=Label(self.sub_frame_hist,text=self.hist_list[idx])
                lab.grid(row=1+idx,column=0,columnspan=2)
                idx+=1
        elif self._is_hist:
            self.no_hist.grid(row=1,column=0,columnspan=2)
        elif not self._is_hist and self.mem_hist==[0]:
            self.no_mem.grid(row=1,column=0,columnspan=2)
        else:
            idx=0
            while idx<len(self.mem_hist):
                lab=Button(self.sub_frame_hist,text=self.mem_hist[idx],padx=10,pady=5,command=lambda index=idx: self.set_screen(self.mem_hist[index]))
                lab.grid(row=1+idx,column=0,columnspan=2)
                idx+=1
    def _init_labelFrames(self):
        self.basic_frame=LabelFrame(self.root,padx=5,pady=5)
        self.basic_frame.grid(row=3,column=1)
        self.special_frame=LabelFrame(self.root,padx=5,pady=5)
        self.special_frame.grid(row=3,column=2,sticky=S)
        self.memory_frame=LabelFrame(self.root,padx=5,pady=5)
        self.memory_frame.grid(row=2,column=1,sticky=E)
        self.history_frame=LabelFrame(self.root,padx=5,pady=5)
        self.history_frame.grid(row=0,column=0,rowspan=10,sticky=NS)
    def _init_number_buttons(self):
        self.button1=Button(self.basic_frame,text='1',padx=40,pady=20,command=lambda: self.button_click(1))
        self.button2=Button(self.basic_frame,text='2',padx=40,pady=20,command=lambda: self.button_click(2))
        self.button3=Button(self.basic_frame,text='3',padx=40,pady=20,command=lambda: self.button_click(3))
        self.button4=Button(self.basic_frame,text='4',padx=40,pady=20,command=lambda: self.button_click(4))
        self.button5=Button(self.basic_frame,text='5',padx=40,pady=20,command=lambda: self.button_click(5))
        self.button6=Button(self.basic_frame,text='6',padx=40,pady=20,command=lambda: self.button_click(6))
        self.button7=Button(self.basic_frame,text='7',padx=40,pady=20,command=lambda: self.button_click(7))
        self.button8=Button(self.basic_frame,text='8',padx=40,pady=20,command=lambda: self.button_click(8))
        self.button9=Button(self.basic_frame,text='9',padx=40,pady=20,command=lambda: self.button_click(9))
        self.button0=Button(self.basic_frame,text='0',padx=40,pady=20, command=lambda: self.button_click(0))
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
        self.button_add=Button(self.basic_frame,text='+',padx=39,pady=20,command=lambda: self.hold('+'))
        self.button_subt=Button(self.basic_frame,text='-',padx=40,pady=20,command=lambda: self.hold('-'))
        self.button_mult=Button(self.basic_frame,text='*',padx=40,pady=20,command=lambda: self.hold('*'))
        self.button_div=Button(self.basic_frame,text='/',padx=40,pady=20,command=lambda: self.hold('/'))
        self.button_neg=Button(self.basic_frame,text='+/-',padx=35,pady=20,command=self.negative_swap)
        self.button_dec=Button(self.basic_frame,text='.',padx=42,pady=20,command=lambda: self.button_click('.'))
        self.button_bksp=Button(self.special_frame,text='Bksp',padx=52,pady=20,command= self.bksp)
        self.button_equals=Button(self.special_frame,text='=',padx=60,pady=20,command=self.equals)
        self.button_clear_all=Button(self.special_frame,text='C',padx=60,pady=20,command=self.clear_all)
        self.button_clear_entry=Button(self.special_frame,text='CE',padx=57,pady=20,command=self.clear_entry)
        self._display_basic_math_buttons()
    def _display_basic_math_buttons(self):
       self.button_add.grid(row=2,column=3)
       self.button_subt.grid(row=3,column=3)
       self.button_mult.grid(row=4,column=3)
       self.button_div.grid(row=5,column=3) 
       self.button_neg.grid(row=5,column=0)
       self.button_dec.grid(row=5,column=2)
       self.button_bksp.grid(row=0,column=0)
       self.button_equals.grid(row=3,column=0)
       self.button_clear_all.grid(row=2,column=0) 
       self.button_clear_entry.grid(row=1,column=0) 
    def _init_show_eq(self,width):
        self.show_eq_text= StringVar()
        self.show_eq=Label(self.root,width=width,textvariable=self.show_eq_text)
        self.show_eq.grid(row=1,column=1,columnspan=4)
    def _init_memory(self):
        self.mem_hist=[0]
        self.button_mc=Button(self.memory_frame,text='MC',padx=20,pady=10,command=self.mem_clear)
        self.button_mr=Button(self.memory_frame,text='MR',padx=20,pady=10,command=lambda: self.set_screen(self.mem_hist[0]))
        self.button_mem_add=Button(self.memory_frame,text='M+',padx=20,pady=10,command=lambda:self.mem_add(float(self.ent.get())))
        self.button_mem_subt=Button(self.memory_frame,text='M-',padx=20,pady=10,command=lambda:self.mem_subt(float(self.ent.get())))
        self.button_ms=Button(self.memory_frame,text='MS',padx=20,pady=10,command=lambda: self.mem_store(float(self.ent.get())))
        self._display_memory()
    def _display_memory(self):
        self.button_mc.grid(row=0,column=0)
        self.button_mr.grid(row=0,column=1)
        self.button_mem_add.grid(row=0,column=2)
        self.button_mem_subt.grid(row=0,column=3)
        self.button_ms.grid(row=0,column=4)
    def negative_swap(self):
        current=self.ent.get()
        if current.lstrip('-')!=current:
            self.ent.delete(0)
        else:
            self.ent.insert(0,'-')
    def bksp(self):
        if len(self.ent.get())>0:
            self.ent.delete(len(self.ent.get())-1)
    def set_screen(self,val):
        self.ent.delete(0,END)
        self.ent.insert(0,val)
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
        self.held=None
        self.held_sym=None
        self.hist_list=[]
        self.update_mem_or_hist()
    def hold(self,button):
        if self.held == None:
            self.held=str(self.ent.get())
        if self.held!='0':
            self.held=self.held.lstrip('0 ')
        self.held_sym=button
        self.ent.delete(0,END)
        self.show_eq_text.set(self.held+' '+self.held_sym)
    def equals(self):
        if self.held_sym==None or self.ent.get()=='' or self.held==None:
            return
        if self.ent.get()=='0' and self.held_sym=='/':
            self.clear_entry()
            self.ent.insert(0,'ERROR: Divide by 0')
            return
        hold=str(self.ent.get())
        hold=hold.lstrip(' 0')

        tree=ExpTree()
        result=tree.solve(self.held+self.held_sym+hold)
        #result=eval(self.held+self.held_sym+hold)
        
        
        self.hist_list.append(self.held+self.held_sym+hold+'='+str(result))
        if len(self.hist_list)>15:
            self.hist_list.pop(0)
        self.update_mem_or_hist()
        self.ent.delete(0,END)
        self.show_eq_text.set('')
        self.held=None
        self.held_sym=None
        self.ent.insert(0,result)
    def mem_clear(self):
        self.mem_hist=[0]
        self.update_mem_or_hist()
    def mem_add(self,val):
        self.mem_hist[0]=self.mem_hist[0]+float(val)
        self.update_mem_or_hist()
    def mem_subt(self,val):
        self.mem_hist[0]=self.mem_hist[0]-float(val)
        self.update_mem_or_hist()
    def mem_store(self,val):
        if self.mem_hist[0]==0:
            self.mem_hist[0]=val
        else:
            self.mem_hist.insert(0,val)
        if len(self.mem_hist)>9:
            self.mem_hist.pop(9)
        self.update_mem_or_hist()
    def math_cleanup(self):
        #when making more buttons that do a calc, make this funcion as a cleaner
        pass


        
def main():
    win=Window(50)
    win.root.mainloop()
main()