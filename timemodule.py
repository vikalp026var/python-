import time
initial =time.time()
print(initial )
k=0
while(k<45):
     print("This is vikalp bahi ")
     k=k+1
print("While loop time",time.time()-initial )
initial2=time.time()
for i  in range (45):
     print("This is vikalp bhai ")
print("for  loop time",time.time()-initial2 )
localtime=time.asctime(time.localtime(time.time()))
print(localtime)