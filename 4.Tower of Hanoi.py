'''
number of minimnum steps to solve tower of hanoi:

for 'n' disk ===>  2^n - 1

n       steps
1          1
2          3
3          7
4         15

'''
n=4
src = "source"
dest = "destination"
aux = "auxiliary"







def toh(n,src,dest,aux): #gives us steps to solve toh for n disk from src to dest using aux
    #Base Case
    if(n==1): # As we know for only 1 disk we move it from src to dest (no calculation needed)
        print("shift disk 1 from",src,"to",dest)  # we give the step here 
        return  # we stop the function

    toh(n-1,src,aux,dest) # Give me the steps to move n-1 disks from src to aux using dest
    print("shift","disk",n, "from",src,"to",dest) # we now shift nth disk from src to dest
    toh(n-1,aux,dest,src) # Give me the steps to move n-1 disks from aux to dest using src










toh(n,src,dest,aux)
    

'''
1. shift all the upper n-1 disk from src to aux using dest
2. shift nth disk from src to dest
3. shift all the n-1 disk from aux to dest using src.
'''


    

    
    
