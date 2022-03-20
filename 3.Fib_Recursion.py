'''
Fibbonacci Problem:

num       fib num
1              0 -> s1
2              1 -> s2    c=s1+s2
3              1 -> c
4              2
5              3 
6              5
7              8
8              13
9              21

fib(n) = fib(n-1) + fib(n-2)
fib(1) = 0
fib(2) = 1

'''

def fib(num):

    #Base Case
    if(num==1):
        return 0
    if(num==2):
        return 1

    return fib(num-1)+fib(num-2)

def fibi(num):
    c=0
    s1=0
    s2=1
    i=1
    while(i<=num):
        c=s1+s2
        s1 = s2
        s2 = c
        i+=1

    return s1

    
    
print(fib(10))
