'''

Example : def factorial(num-1):

    factorial(num-2)
    pass

0 1 2 3 4 5 6

# It creates the illusion of loop without using any looping function like 'for' or 'while'.

Defination: Recursion is the process by which a function calls itself directly or indirectly. The function which calls itself is
                    called recursive Function

There are 3 Components:
    1. Base Case -> Condition for which the function will stop 
    2. Work -> The instruction to achieve solution, depends  upon problem statement.
    3. Calling -> recursive calling of function.

When will function stop:
1. Base Case reached (return)
2. When Every Step is finished.

'''

# Iterative Function for n to 1
def printnto1(num):
    '''num =6
    6
    5
    4
    3
    2
    1

0       1       2       3       4
H       e       l        l        o
-5     -4       -3    -2       -1


    num=0

    '''

    for i in range(6,0,-1):
        print(i)

# Recursive Function for n to 1

def prec(num):# num se 1 print krna tha

    if (num==0): # Base Case
        return

    print(num) #Work (hmne kiya bs num ko print )
    
    prec(num-1) # Calling (Function se demand kiya ki tum num-1 se 1 print krke do)

#Dry Run
1. prec(6) # Still in the memory
2. prec(5) # Still in memory
3. prec(4) # Still in memory

#Output
6
5
4


prec(6)



        

    

    


        
        
        

    

    

    
















    
    
