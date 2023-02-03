#def function_name_print(a,b,c,d):
     #print(a,b,c,d)
###function_name_print("Harry","Vikalp","sankalop","Star")
def funargs(normal,*args,**kwargs):
     print(normal)
     for item in args :
          print(item)
     for key,value in kwargs.items():
          print(f"{key} is a {value}")
har=["Harry","father","Sister","Daughter in law"]
normal="855"
kw={"Rohan":"Monitor","Vishu":"Cook"}
funargs(normal,*har,**kw)