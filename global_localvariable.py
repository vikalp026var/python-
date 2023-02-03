l=10#global
def function1(n):
     l=5#local scope
     print(n,"vikalp")
     print(l)
print(l)
function1("This is me ")
print(l) 
 ##################################

x=89
def harry():
     x=20
     def rohan():
          global x
          x=88
          rohan()
          print("after calling rohan()",x)
harry()
print(x)