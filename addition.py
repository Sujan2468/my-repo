def NOT(a):
    if a=='1':
        return '0'
    else: 
        return '1'
    
def AND (a, b):
    if a=='1' and b=='1':
        return '1'
    else: 
        return '0'

def OR(a, b):
    if a=='0' and b=='0':
        return '0'
    else:
        return '1'

def XOR(a, b): 
    if a==b:
        return '0'
    else:
        return '1'

first ='1111'
second = '1111'

def fullAdder(one, two , three):
    sum = XOR(XOR(one, two), three)
    carry = OR( AND(one, two ), AND(three, XOR(one, two)))
    return [carry, sum]


def fullSum(one, two):
    result = ''

    i =  len(one)
    j = len(two)
    str = ""
    for n in range(abs(i-j)):
        str = str +"0"
    times = max(i, j)

    if(i<j):
        one = str+one
    if(j<i):   
        two = str+two

    # print(one, two)     
    carry = '0'

    n=0
    while(times):
        result += (fullAdder(one[times-1], two[times-1], carry)[1])
        carry = fullAdder(one[times-1], two[times-1], carry)[0]
        times -=1
        # print(n, result)
        n+=1
        # print(one[i-n-1], two[j-n-1])
        # j-=1
        # i-=1
        # if(i<0): 
        #     i=0
        # if(j<0): 
        #     j=0
    # print("result", reversed(result))
    # print("carry", carry)
    result = carry + "".join(reversed(result))
    return result
    # print(result)

# print(carry, "".join(reversed(result)))

# print (fullSum('1000', '010'))
#operand1 = input("Enter first Operand : ")
#operand2 = input("Enter second operand : ")
#print("Sum of ",operand1," and ",operand2," is ",fullSum(operand1,operand2))