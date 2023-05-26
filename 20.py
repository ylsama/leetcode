
def a():
    s = '()[]()'
    head = 0
    q = ['0']*len(s)
    for i in s:
        print(i)
        if i in '([{':
            q[head] = i
            head += 1
        else:
            if head ==0: return False
            if q[head-1]!='([{'[')]}'.index(i)]:
                return False
            else:
                head -= 1
    return head == 0 

print(a())
