while(1):
    print("Enter a number ")
    n=int(input())
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print("\n")
    for i in range(1,n,1):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\n")
    
