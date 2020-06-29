print("Enter two numbers")
a = int(input())
b = int(input())
print("1: add \n2: subtract\n3: Multiply \n4: divide")
choice = int(input())
if(choice == 1):
    print(a + b)
elif(choice == 2):
    print(a - b)
elif(choice == 3):
    print(a * b)
elif(choice == 4):
    print(a // b)
else:
    print("Wrong choice")
