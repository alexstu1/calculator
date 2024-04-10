def _enlist(string):
    lst=[]
    hold=''
    index=-1
    legal=['*','/','-','+']
    for chr in string:
        index+=1
        if chr==' ':
            continue
        if chr.isnumeric() or chr=='.':
            hold=hold+chr
            continue
        elif hold!='':
            lst.append(float(hold))
            hold=''
        if chr in legal:
            lst.append(chr)
            continue
        raise ValueError(f'unimplemented symbol found: {chr}')
    lst.append(float(hold))
    return lst
def _doubles(lst):
    idx=1
    while idx<len(lst):
        if lst[idx]=='-'and lst[idx-1]=='-':
            lst.pop(idx)
            lst[idx-1]='+'
        idx+=1
    idx=1
    while idx<len(lst):
        if lst[idx]=='+'and lst[idx-1]=='+':
            lst.pop(idx)
            idx-=1
        idx+=1
    return lst
def _fix_mdas(lst):
    lst=lst.copy()
    idx=0
    while idx<len(lst):
        if lst[idx]=='-':
            if idx!=0 and type(lst[idx-1])==float:
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
    
def _parse(lst):
    lst=lst.copy()
    order=['*','+']
    for sym in order:
        idx=0
        while idx<len(lst):
            if len(lst)==1: 
                return lst[0]
            if sym==lst[idx]:
                left=lst.pop(idx-1)
                right=lst.pop(idx)
                lst[idx-1]=_math(left,sym,right)
                idx=-1
            idx+=1
    raise RuntimeError('Unexpected error during math operaitons')
def _math(left,sym,right):
    pointers={'*':_mult,'+':_add}
    for key in pointers:
        if sym==key:
            return pointers[key](left,right)
def _add(a,b):
    return a+b
def _mult(a,b):
    return a*b
def solve(string):
    lst=_enlist(string)
    lst=_doubles(lst)
    lst=_fix_mdas(lst)
    return _parse(lst)


def _test():
    print(solve('1+2-3*4/3'))
if __name__=='__main__':
    _test()
