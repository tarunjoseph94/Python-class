class Emp:
    empcount=0
    def __init__(self,name,sal):
         Emp.empcount+=1
         self.name=name
         self.sal=sal
    def printcount(self):
        print('Total number of employess',Emp.empcount)
    def printdets(self):
        print("Name is ",self.name,",The salary is ",self.sal)
e1=Emp("abcd",100)
e1.printcount()
e1.printdets()
e2=Emp("dgef",200)
e2.printcount()
e2.printdets()
e3=Emp("hijk",300)
e3.printcount()
e3.printdets()
e2.printcount()

if (hasattr(e1,'sal')):
    setattr(e1,'sal',500)
    print(getattr(e1,'sal'))
    setattr(e1,'sala',400)
    print(getattr(e1,'sala'))
    delattr(e1,'sala')
    
else:
    print("attribute does  not exist")

