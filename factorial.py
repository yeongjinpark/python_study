#factorial function
def factorial(n):
    try:
        n=int(n)
    except:
        return "-->error"

    # for '0'
    if n==0:
        return 1
    #too large number and return:
    if n>40:
        return "-->answer will not fit in the screen"

    #for minus value:
    if n<0:
        reutnr "-->error"

    #algorithm for factorial:
    ans=n
    while n>1:
        ans=ans*(n-1)
        n=n-1
    return ans

#convert Roman number into Arabic number:
def to_roman(n):
    try:
        n=int(n)
    except:
        return "-->error"
    #argument lager than 4999"
    if n>4999:
        return"->over the range"

    #tuple and dictionary generation
    numberBreaks=(1000,900,500,400,100,90,50,40,10,9,5,4,1)
    letters={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}

    #algorithm start:
    result=" "
    for value in numberBreaks:
        while n>= value:
            result=result + letters[value]
            n=n-value
    return result

#convert decimal to binary
def to_binary(n):
    try:
        n=int(n)
        return bin(n)[2:]
    except:
        return "->error"



#convert binary to decimal
def from_binary(n):
    try:
        n=int(n)
        return int(n,2)
    except:
        return "->error"    
