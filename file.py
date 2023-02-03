f=open("vikalp.txt")
print(f.tell()) #tell the file pointer 
print(f.readline())
print(f.tell())#tell the file pointer 
print(f.readline())
f.seek(0)
print(f.readline())
f.close()
#####shortcut##########
with open ("vikalp.txt") as f:
    a=f.read(4)
    print(a)                         ############ without close##########
 
      