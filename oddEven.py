print("I can tell you if a number is even or odd...")
number = int(input("Enter Number:"))
result  = number%2

if result == 1:
    print("Its odd")

elif result == 0:
    print("Its even")

else:
    print("Invalid")