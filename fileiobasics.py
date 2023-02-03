''' "r"----open file for reading---DEFAULT MODE 
"w"----- open file for writing
"x" ------ creates file if not exits
"a"------- Add more content to a file 
"t"------- text mode --DEFAULT MODE 
"b"------- binary mode 
"+"-------- read and write 
'''
f = open("vikalp.txt")
content=f.read()
print(content)
f.close()
