#Health Management system
# 3 clients - Harry ,Rohan and Hammad 
#Total 6 files 
#write a Function that when execute takes as input client name 
def getdata():
     import datetime
     return datetime.datetime.now()
def take(k):
     if k==1:
          c=int(input("Enter 1 for excercise and 2 for food "))
          if c==1:
               value=input("type here \n")
               with open ("harry-ex.txt","a")as op:
                    op.write(str([str(getdata())])+" "+ value +"\n")
               print("successfully written")
          elif c==2:
               value=input("type here\n")
               with open ("harry-food.txt","a") as op:
                    op.write(str([str(getdata())]) + " :"+ value +"\n")
               print("successfully written")
     elif k==2:
          c=int(input("Enter 1 for excercise and 2 for food "))
          if c==1:
               value=input("type here \n")
               with open ("rohan-ex.txt","a")as op:
                    op.write(str([str(getdata())])+" "+ value +"\n")
               print("successfully written")
          elif c==2:
               value=input("type here\n")
               with open ("rohan-food.txt","a") as op:
                    op.write(str([str(getdata())]) + " :"+ value +"\n")
               print("successfully written")
     elif k==3:
          c=int(input("Enter 1 for excercise and 2 for food "))
          if c==1:
               value=input("type here \n")
               with open ("hammad-ex.txt","a")as op:
                    op.write(str([str(getdata())])+" "+ value +"\n")
               print("successfully written")
          elif c==2:
               value=input("type here\n")
               with open ("hammad-food.txt","a") as op:
                    op.write(str([str(getdata())]) + " :"+ value +"\n")
               print("successfully written")
     else:
          print("plz enter valid input(1(harry),2(rohan),3(hammad)")

def retrieve(k):
     if k==1:
          c=int(input("enter 1 for exercise and 2 for food "))
          if c==1:
               with open ("harry-ex.txt") as op:
                    for i in op :
                         print(i,end=" ")
          elif c==2:
               with open("harry-food.txt") as op:
                    for i in op:
                         print(i,end="")
     elif k==2:
          c=int(input("enter 1 for exercise and 2 for food "))
          if c==1:
               with open ("rohan-ex.txt") as op:
                    for i in op :
                         print(i,end=" ")
          elif c==2:
               with open("rohan-food.txt") as op:
                    for i in op:
                         print(i,end="")
     elif  k==3:
          c=int(input("enter 1 for exercise and 2 for food "))
          if c==1:
               with open ("hammad-ex.txt") as op:
                    for i in op :
                         print(i,end=" ")
          elif c==2:
               with open("hammad-food.txt") as op:
                    for i in op:
                         print(i,end="")
     else :
          print("plz enter valid input (harry,rohan,hammad)")
print("Health Management system :")
print("----------------------------------")

while(1):
     a=int(input("Press 1 for look the value and 2 for retrieve"))
     if a==1:
          b=int(input("press 1 for harry 2 for rohan 3 for hammad"))
          take (b)
     else :
          b=int(input("press 1 for harry 2 for rohan 3 for hammad"))
          retrieve (b)
  


                  

