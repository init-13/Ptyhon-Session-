'''
Approach :

1-User choose the desired operation. Options 1, 2, 3 and 4 are valid.
2-Two numbers are taken and an if…elif…else branching is used to execute a particular section.
3-Using functions add(), subtract(), multiply() and divide() evaluate
'''

# Function to add two numbers
def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
	return num1 / num2

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")


# Take input from the user
Enter_Your_Choice = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if Enter_Your_Choice == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

elif Enter_Your_Choice == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif Enter_Your_Choice == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif Enter_Your_Choice == 4:
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
else:
	print("Invalid input")
