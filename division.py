dividend = '1111'
divisor = '0111'

from subtraction import sub
from addition import fullSum

def restoringDivision (dnd, dor):
    a = "".join(map(str, [0]* (len(dnd)+1)))
    b = a[-len(dor):]+dor
    q = dnd
    count = len(dnd)
    for i in range(count):
        # print("a", a, "q", q)
        a = a[1:]+q[0]
        # print("sub", a, b)
        diff = sub(a, b)[-count-1:]
        # print(diff, "diff")
        if(diff[0]=='1'):
            q=q[1:]+ "0"   
            # print("sum", b, diff)
            a = fullSum(b, diff)[-count-1:]
            # print(a, "a")
        else:
             q=q[1:]+ "1"
             a= diff
    return {"q":q, "a":a}
# print(restoringDivision(dividend, divisor))


def nonRestoringDivision(dnd, dor):
    a = "".join(map(str, [0]* (len(dnd)+1)))
    b = a[-len(dor):]+dor
    q = dnd
    count = len(dnd)
    for i in range(count):
        # print("a" ,a, "q" ,q)
        a = a[1:]+q[0] 
        if(a[0]=='0'):
            diff = sub(a, b)[-count-1:]
            q=q[1:]+ "0" if diff[0]=='1' else q[1:]+ '1' 
            a= diff 
        else:
            a= fullSum(a, b)[-len(dnd)-1:]
            q= q[1:]+'0' if a[0]=='1' else q[1:]+'1'
    if a[0]=='1':
        a = fullSum(a, b)[-len(dnd)-1:]
    return {"q":q, "a":a}

print(nonRestoringDivision(dividend, divisor))
print(restoringDivision(dividend, divisor))