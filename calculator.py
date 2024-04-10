from tkinter import *
from calculations import solve
def startup():
    root=Tk()
    root.title('Calculator')
    ent=Entry(root,width=50,borderwidth=5,justify=RIGHT)
    ent.grid(row=0,column=1,columnspan=4)
    ent.focus_set()
    ent.clipboard_append('h')
    memlst=[]
    histlist=[]
    frames=labelFrames(root)
    numberButtons(frames[0],ent)
    history(frames[3],histlist,memlst,ent)
    basicMath(frames[0],frames[1],ent,histlist,memlst)
    memory(frames[2],memlst,ent)
    return root


def labelFrames(root):
    basic_frame=LabelFrame(root,padx=5,pady=5)
    basic_frame.grid(row=3,column=1)
    special_frame=LabelFrame(root,padx=5,pady=5)
    special_frame.grid(row=3,column=2,sticky=S)
    memory_frame=LabelFrame(root,padx=5,pady=5)
    memory_frame.grid(row=2,column=1,sticky=E)
    history_frame=LabelFrame(root,padx=5,pady=5)
    history_frame.grid(row=0,column=0,rowspan=10,padx=5,pady=5,sticky=NS)
    return [basic_frame,special_frame,memory_frame,history_frame]

def numberButtons(frame,ent):
    button1=Button(frame,text='1',padx=40,pady=20,command=lambda: button_click('1',ent))
    button2=Button(frame,text='2',padx=40,pady=20,command=lambda: button_click('2',ent))
    button3=Button(frame,text='3',padx=40,pady=20,command=lambda: button_click('3',ent))
    button4=Button(frame,text='4',padx=40,pady=20,command=lambda: button_click('4',ent))
    button5=Button(frame,text='5',padx=40,pady=20,command=lambda: button_click('5',ent))
    button6=Button(frame,text='6',padx=40,pady=20,command=lambda: button_click('6',ent))
    button7=Button(frame,text='7',padx=40,pady=20,command=lambda: button_click('7',ent))
    button8=Button(frame,text='8',padx=40,pady=20,command=lambda: button_click('8',ent))
    button9=Button(frame,text='9',padx=40,pady=20,command=lambda: button_click('9',ent))
    button0=Button(frame,text='0',padx=40,pady=20, command=lambda: button_click('0',ent))

    button1.grid(row=4,column=0)
    button2.grid(row=4,column=1)
    button3.grid(row=4,column=2)
    button4.grid(row=3,column=0)
    button5.grid(row=3,column=1)
    button6.grid(row=3,column=2)
    button7.grid(row=2,column=0)
    button8.grid(row=2,column=1)
    button9.grid(row=2,column=2)
    button0.grid(row=5,column=1)
def button_click(button,ent):
    current=ent.get()
    ent.delete(0,END)
    ent.insert(0,current+button)
def basicMath(frame,sframe,ent,histlist,memlst):
    button_add=Button(frame,text='+',padx=39,pady=20,command=lambda: button_click('+',ent))
    button_subt=Button(frame,text='-',padx=40,pady=20,command=lambda: button_click('-',ent))
    button_mult=Button(frame,text='*',padx=40,pady=20,command=lambda: button_click('*',ent))
    button_div=Button(frame,text='/',padx=40,pady=20,command=lambda: button_click('/',ent))
    button_neg=Button(frame,text='+/-',padx=35,pady=20,command=lambda: negative_swap(ent))
    button_dec=Button(frame,text='.',padx=42,pady=20,command=lambda: button_click('.',ent))
    button_bksp=Button(sframe,text='Bksp',padx=52,pady=20,command= lambda: ent.delete(len(ent.get())-1))
    button_equals=Button(sframe,text='=',padx=60,pady=20,command=lambda: equals(ent,histlist))
    button_clear_all=Button(sframe,text='C',padx=60,pady=20,command=lambda: clear_all(ent,histlist,memlst))
    button_clear_entry=Button(sframe,text='CE',padx=57,pady=20,command=lambda: clear_entry(ent,histlist,memlst))

    button_add.grid(row=2,column=3)
    button_subt.grid(row=3,column=3)
    button_mult.grid(row=4,column=3)
    button_div.grid(row=5,column=3) 
    button_neg.grid(row=5,column=0)
    button_dec.grid(row=5,column=2)
    button_bksp.grid(row=0,column=0)
    button_equals.grid(row=3,column=0)
    button_clear_all.grid(row=2,column=0) 
    button_clear_entry.grid(row=1,column=0) 

def negative_swap(ent):
    current=ent.get()
    if current=='':
        ent.insert(0,'-')
        return
    idx=len(current)-1
    while idx>=0:
        if current[idx]=='-':
            if idx==0:
                ent.delete(0)
                break
            elif current[idx-1] not in '1234567890.':
                ent.delete(0,END)
                string=current[0:idx]+current[idx+1:]
                ent.insert(0,string)
                break
            else:
                ent.delete(0,END)
                string=current[0:idx]+'+'+current[idx+1:]
                ent.insert(0,string)
                break
        elif current[idx]=='+':
            ent.delete(0,END)
            string=current[0:idx]+'-'+current[idx+1:]
            ent.insert(0,string)
            break
        elif current[idx]==')':
            ent.delete(0,END)
            string=current[0:idx+1]+'*-'+current[idx+1:]
            ent.insert(0,string)
            break
        elif current[idx] in '*/^':
            ent.delete(0,END)
            string=current[0:idx+1]+'-'+current[idx+1:]
            ent.insert(0,string)
            break
        elif current[idx] in '1234567890.':
            idx-=1
            continue
        if idx==0:
            ent.delete(0,END)
            ent.insert(0,'-'+current)
            break
        raise SyntaxError(f'Unexpected symbol found: {current[idx]}')
def equals(ent,histlist):
    answer=solve(ent.get())
    histlist.insert(0,ent.get()+'='+str(answer))
    ent.delete(0,END)
    ent.insert(0,answer)
    update()
def clear_all(ent,histlist,memlst):
    while histlist!=[]:
        histlist.pop()
    while memlst!=[]:
        memlst.pop()
    ent.delete(0,END)
    update()
def clear_entry(ent,histlst,memlst):
    if len(ent.get())==0:
        clear_all(ent,histlst,memlst)
    ent.delete(0,END)
    update()
def memory(frame,lst,ent):
    button_mc=Button(frame,text='MC',padx=20,pady=10,command=lambda: memhelp(ent,memclear(lst)))
    button_mr=Button(frame,text='MR',padx=20,pady=10,command=lambda: memhelp(ent,memrecall(ent,lst)))
    button_mem_add=Button(frame,text='M+',padx=20,pady=10,command=lambda: memhelp(ent,memadd(solve(ent.get()),lst)))
    button_mem_subt=Button(frame,text='M-',padx=20,pady=10,command=lambda: memhelp(ent,memsub(solve(ent.get()),lst)))
    button_ms=Button(frame,text='MS',padx=20,pady=10,command=lambda: memhelp(ent,mem_store(solve(ent.get()),lst)))
    button_mc.grid(row=0,column=0)
    button_mr.grid(row=0,column=1)
    button_mem_add.grid(row=0,column=2)
    button_mem_subt.grid(row=0,column=3)
    button_ms.grid(row=0,column=4)
def memhelp(ent,func):
    #the func gets called in the functions calling this so both can be done in a lambda function
    if ent.clipboard_get()=='m':
        update()
def memrecall(ent,lst):
    ent.delete(0,END)
    if lst!=[]:
        ent.insert(0,lst[0])
def mem_store(num,lst):
        #!reminder
        lst.insert(0,num)
def memclear(lst):
    while lst!=[]:
        lst.pop()
def memadd(num,lst):
    if lst==[]:
        lst.append(num)
    else:
        lst[0]=lst[0]+num
def memsub(num,lst):
    if lst==[]:
        lst.append(0-num)
    else:
        lst[0]=lst[0]-num
def history(frame,histlist,memlist,ent):
    subframe=LabelFrame(frame,borderwidth=5)
    hist_button=Button(frame,text='History',padx=30,pady=10,command=lambda: swapper('hist',ent))
    mem_button=Button(frame,text='Memory',padx=30,pady=10,command=lambda: swapper('mem',ent))  
    hist_button.grid(row=0,column=0)
    mem_button.grid(row=0,column=1)
    subframe.grid(row=1,column=0,columnspan=2,sticky=NS)
    update(ent,subframe,histlist,memlist)
def swapper(target,ent):
    if target=='hist':
        ent.clipboard_clear()
        ent.clipboard_append('h')
    elif target=='mem':
        ent.clipboard_clear()
        ent.clipboard_append('m')
    update()        
def update(ent=None,subframe=None,histpoint=None,mempoint=None,pointers=[]):
    if histpoint!=None:
        pointers.append(histpoint)
        pointers.append(mempoint)
        pointers.append(subframe)
        pointers.append(ent)
    ent=pointers[3]
    subframe=pointers[2]
    memlst=pointers[1]
    histlist=pointers[0]
    target=ent.clipboard_get()
    hold=[]
    for item in subframe.children.values():
        hold.append(item)
    while hold!=[]:
        hold.pop().destroy()
    no_hist=Label(subframe,text='No history yet!')
    no_mem=Label(subframe,text='No numbers in memory!')
    if target=='h' and len(histlist)!=0:
        idx=0
        while idx<len(histlist):
            lab=Label(subframe,text=histlist[idx])
            lab.grid(row=1+idx,column=0,columnspan=2)
            idx+=1
    elif target=='h':
        no_hist.grid(row=1,column=0,columnspan=2)
    elif target=='m' and memlst!=[]:
        idx=0
        while idx<len(memlst):
            hold=memlst[idx]
            lab=Button(subframe,text=memlst[idx],padx=10,pady=5,command=lambda held=hold: ent.insert(len(ent.get()),held))
            lab.grid(row=1+idx,sticky=EW,column=0,columnspan=2)
            idx+=1
    elif target=='m':
        no_mem.grid(row=1,column=0,columnspan=2)
def main():
    root=startup()
    root.mainloop()
main()
