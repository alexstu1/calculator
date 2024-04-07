class ExpTree:
    '''
    builds a binary tree, then post order solves it
    '''
    def __init__(self):

        self.order=['^','**','*','/','-','+']
        self.legal=['^','**','*','/','-','+']
    def cleanup(self,string):
        idx=0
        string=string.strip(' ')
        while idx<len(string):
            if string[idx]==' ':
                string=string[0:idx]+string[idx+1:]
            idx+=1
        if string[0]=='-':
            string='0'+string
        idx=1
        while idx<len(string):
            if string[idx]=='-' and string[idx-1]=='-':
                string=string[0:idx-1]+'+'+string[idx+1:]
                idx-=1
            idx+=1
        idx=1
        while idx<len(string):
            if string[idx]=='+' and string[idx-1]=='+':
                string=string[0:idx]+string[idx+1:]
                idx-=1
            idx+=1
        return string
    def enlist(self,string):
        lst=[]
        hold=''
        index=-1
        for chr in string:
            index+=1
            #duplicate space protection here, refactor this
            if chr==' ':
                continue
            if chr.isnumeric() or chr=='.':
                hold=hold+chr
                continue
            elif hold!='':
                lst.append(float(hold))
                hold=''
            if chr in self.legal:
                lst.append(chr)
                continue
            raise ValueError(f'unimplemented symbol found: {chr}')
        lst.append(float(hold))
        return lst
    def fix_neg_div(self,lst):
        idx=0
        while idx<len(lst):
            if lst[idx]=='-':
                if type(lst[idx-1])==float:
                    lst[idx]='+'
                else:
                    lst.pop(idx)
                    idx-=1
                lst[idx+1]=0-lst[idx+1]
            idx+=1
        idx=0
        while idx<len(lst):
            if lst[idx]=='/':
                lst[idx]='*'
                lst[idx+1]=1/lst[idx+1]
            idx+=1
        return lst
    def parse(self,lst):
        for sym in self.order:
            #print(sym,lst)
            idx=0
            while idx<len(lst):
                #print(lst)
                if len(lst)==1: 
                    if type(lst[0])==Node:
                        held=lst[0]
                        return held.solve()
                    return lst[0]
                if sym==lst[idx]:
                    print(sym,lst)
                    node1=Node(lst.pop(idx))
                    if type(lst[idx-1])==Node:
                        node1.left=lst.pop(idx-1)
                    else:
                        node1.left=Node(lst.pop(idx-1))
                    if type(lst[idx-1])==Node:
                        node1.right=lst.pop(idx-1)
                    else:
                        node1.right=Node(lst.pop(idx-1))
                    lst.insert(idx-1,node1)
                    idx=-1
                idx+=1
        #[1,'+',2,'*',3,'+',4]
    def solve(self,string):
        string=self.cleanup(string)
        lst=self.enlist(string)
        lst=self.fix_neg_div(lst)
        return self.parse(lst)
#[parenthesis,exponent,mult,div,add,subt]


class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        #contains legacy subrtraction and division
        self.operators={'+':self.add,'-':self.minus,'*':self.mult,'/':self.div,'**':self.exp,'^':self.exp}

    def add(self,a,b):
        return a+b
    def minus(self,a,b):
        return a-b
    def mult(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def exp(a,b):
        return a**b
    def solve(self):
        if self.left==None and self.right==None:
            return self.value
        left=self.left.solve()
        right=self.right.solve()
        answer=self.operators[self.value](left,right)
        return answer


def test():
    a=ExpTree()
    b=a.solve('1/-2*3+4')
    #lst=a.fix_neg_div(lst)
    #b=a.parse(lst)
    print(b)

    
    '''
    a=Node('*')
    b=Node(3)
    c=Node(4)
    a.left=b
    a.right=c
    print(a.solve())
    '''
test()