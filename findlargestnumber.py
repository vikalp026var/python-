print("\t \t Enter three numbers")
print("First Number is ")
x=int(input())
print("\n Seconf n Number is ")
y=int(input())
print("\n Third  Number is ")
z=int(input())
if x>y and x>z:
    print("The largest number is ",x)
elif y>x and y>z:
    print("The largest number is ",y)
else :
    print("The largest number is ",z)
