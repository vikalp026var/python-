print("Welcome to factorial program")
print("Enter the number ")
x=int(input())
def fibnocci(n):
     if n==0:
          return 0
     elif n==1:
          return 1
     else :
          fib=fibnocci(n-1)+fibnocci(n-2)
          return fib
if x<=0:
     print("Please ente the positive number ")
else:
     print("Fibnocci series:")
     for i in range (x):
          print(fibnocci(i))
######################### factorial ########
def fact(n):
     if n==1:
          return 1
     else :
          return n*fact(n-1)
print ("Welcome the factorial program ")
print("-----------------------------------")
print("Enter the number ")
n=int(input())
print(fact(n))
