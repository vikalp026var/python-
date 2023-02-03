import random
a=0  #for computer Won 
b=0  # for  user won 
l=["Stone","paper  ","Scissor"]
print("\t \t \t WELCOME TO GAME \t \t \t ")
print("\t \t \t-----------------------------------")
print("\t \t \t-----------------------------------")
print("\t \t \t-----------------------------------")
print("You have only 8 moves ")
n=8
while(1):
     for i in range(n,0,-1):
          print("Choose among: \n 1.Stone\n 2.paper \n 3.Scissor ")
          x=int (input())
          y=random.choice(l)
          if x==1 and y=="paper ":
               print("You Loss")
               print("Computer choose :",y)
               a=a+1
          elif x==1 and y=="Scissor ":
               print("You Won")
               print("Computer choose :",y)
               b=b+1
               
          elif x==1 and y=="Stone ":
               print("Game Draw")
               print("Computer choose :",y)
          
          elif x==2 and y=="paper":
               print("Game Draw")
               print("Computer choose :",y)
               
          elif x==2 and y=="Scissor":
               print("You Loss")
               a=a+1
               
          elif x==2 and y=="Stone":
               print("You Won")
               b=b+1
               
          elif x==3 and y=="Stone":
               print("You Loss")
               a=a+1

          elif x==3 and y=="paper":
               print("You Won")
               b=b+1

          elif x==3 and y=="Scissor":
               print("Game Draw")
          
print("\t \t \t Game Over\t \t \t ")
print("\t \t \t-----------------------------------")
print("\t \t \t-----------------------------------")
print("\t \t \t-----------------------------------")
print("\n You won number of times is ",b)
print("\n Computer win Number of chances ",a)

    
