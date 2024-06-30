from addition import fullSum
from addition import NOT

def twosComplement(str):
    bits = list(str)
    another = ''
    for bit in bits:
        another+=NOT(bit)
        
    # print(fullSum(another, '1'))
    return fullSum(another, '1')[1:]

# print("here", twosComplement('100'))
        
        
def sub(first, second):
    # print('twos', twosComplement(second))
   
    for n in range(len(first), 8):
        first = "0"+first
    for n in range(len(second), 8):
        second = "0"+second
   
    # print(first, second)
    return fullSum(first, twosComplement(second))        
    
#operand1 = input("Enter a first operand : ")
#operand2 = input("Enter a second operand : ")
#print("Difference of ",operand1," and ",operand2," is ",sub(operand1,operand2))
