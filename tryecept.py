print("Enter num1")
num1=int(input())
print("Enter num2")
num2=int(input())
try:
    print("The sum of these two number is",
    int(num1)+int(num2))
except Exception as e:
    print(e)
