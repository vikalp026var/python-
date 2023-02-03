print("\t \t \t Temperature Converter \t \t \t  ")
while(1):                                           # c/5 = f-32/9
    print("Enter Your choice :")
    print("1.Farheinheit to celsius converter. ")
    print("2.Celsius to Farheinheit Converter .")
    print("3.Exit")
    x=int(input())
    if x==1:
        print("Welcome to Farheinheit to celsius converter. ")
        print("----------------------------------------------")
        print("Enter the Temperature in farheinheit ")
        f=int(input())
        c=(f-32)/9*5
        print("Result: Temperature int celsius is ",c)
        print("Thank you ")
    elif x==2:
        print("Welcome to celsius  to Farenheit  converter. ")
        print("----------------------------------------------")
        print("Enter the Temperature in Celsius  ")
        c=int(input())
        f=32+1.8*c
        print("Result: Temperature in farenheit is ",f)
        print("Thank you ")
    else :
        print("You are terminated your program successfully ")
        print("Thank You ")
        
    
