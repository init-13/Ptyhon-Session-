'''
[1,2,3,,5,,7,,,,11,]

[1,2,3,,5,,7,,,
 ,11,,13,,,,17,,19,]

 sqrt(20) => 4.5

 1,2,3,,5,,7,,,,11,,13,,,,17,,19,20
'''

def sieve(n):

    prime = []
  '''
prime = [true,true,true,true,true,true,true,true,true]
  index:     0      1      2      3   4      5      6   7      8

  '''
    for i in range(n+1):
        prime.append(True)

    # Create a list of 1 to n all True

    p=2 # start from 2 as it is the smallest prime

    while(p*p<=n): # all multiples will be covered till sqrt n
        #print(prime)
        if (prime[p]==True): # if a prime is encountered
            for i in  range(p*p,n+1,p): # Make all encountered prime multiples false
                prime[i] = False 
        p+=1

    for i in  range(2,n+1):
        if(prime[i]==True):# print all primes which is true
            print(i)

sieve(100)
        
