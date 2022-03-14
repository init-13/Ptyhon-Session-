# # Python program to find factors of a number using function

# def find_factors(num):  #user-defined function
#    print('The factors of', num,'are:')
#    for i in range(1, num + 1):
#        if num % i == 0:
#            print(i, end=' ')

# # take inputs
# num = int(input('Enter number: '))

# # calling function
# find_factors(num)

n= 4
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")

    print()