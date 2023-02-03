''' "r"----open file for reading---DEFAULT MODE 
"w"----- open file for writing
"x" ------ creates file if not exits
"a"------- Add more content to a file 
"t"------- text mode --DEFAULT MODE 
"b"------- binary mode 
"+"-------- read and write 
'''
f = open("vikal.txt","rt")
cont=   f.read()
print(cont)
f.close()
######writing in the file ##########
f=open("vikalp.txt","w")
a=f.write("vikap is a bad boy")
print(a)
f.close()
###########append mode#########
f=open("vikalp.txt","a")
a=f.write("vikap is a bad boy")
print(a)
f.close()

######## Handle read and write #########
f=open("vikalp.txt","r+")
print(f.read())
f.write("thank you")