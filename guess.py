n=18
c=9
while(1):
    n1=int(input("Enter a number "))
    if c<=9:
        if n==n1 :
            print("Matched ")
            c=c-1
        else :
            print("Not matched ")
            c=c-1
        print("Guess remain ",c-1)
    else:
        print("Game over !!!")
     
   


