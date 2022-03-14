win = 90
user  = int(input("Enter The Number between 1 to 100: "))

if user == win:
     print("You Are Win")

else:                             # nested if else
     if user<win:
           print("Too Low")
     else:
           print("Too High")