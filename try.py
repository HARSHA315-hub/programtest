a = int(input("Enter the number to be divided:"))
b = int(input("Enter the number used to divide:"))
try:
    result = a/b
    print(result)
except:
    print("The number cannot divide by zero.")
try:
    user_age = int(input("Enter a age:"))
except ValueError:
    print("That is not a number.")
try:
    n = input("Enter  number:")
    result = "Total" + int(n)
except TypeError:
        print("String and integer error")
        print("Total:" + str(n))