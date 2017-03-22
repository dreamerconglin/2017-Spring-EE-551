#defining a function
def simpleFunction():
    print ("Simple funcion")
    print ("Does nothing")

def addThis(x, y):
    print (x+y)
    return x+y

#calling funcions
simpleFunction()
x = 6
print (x)
x = simpleFunction
x()
a = addThis(2,3)
addThis(2.7,3.14)
addThis("Add"," This?")
