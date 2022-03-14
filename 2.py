num = 18

#num = int(input("Enter the number: "))
for i in range(2, int(num**0.5)+1):
    if(num%i==0):
        print("not prime")
        break
else:
    print("prime")