########### DECLARTION THE DICTIONARY ##########################
d1={}
print(type(d1))
d2={"vikalp":"burger","harish":"fish","golu":"egg","uu":{ "g":"iii"}}
print(d2["golu"])
print(d2["uu"])
d2["Ankit"]="Junk food "
print(d2)
d2[420]="ppp"
print(d2)
del d2[420]
print(d2)
d3=d2
print(d3)
print(d2.update({"Leena":"Toffee"}))
print(d2)
print(d2.keys())
print(d2.items())



############ CREATE THE DICTIONARY AND TAKE INPUTS FROM THE USER AND RETURN THE MEANING OF THE WORD FROM THE DICTIONARY ###########
d1={"swap":"reverse ","octagon ":"8 side "}
print("Enter the word from these among words :swap,octagon")
x=int(input())
print(d1.items())