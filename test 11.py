def SimpleFunction(self):
    print ("This is a simple function.")

class Employee:
    salary = 0
    age = 0
    name = ''

    #constructor :init(double '_' on left and double '_' on right)
    def __init__(self, salary, age, name):
        self.salary = salary
        self.name = name
        self.age = age

    def raiseSalary (self):
        self.salary = self.salary * 0.1 + self.salary

    def printSalary (self):
        print (self.salary)

    myExternalFunction = SimpleFunction

E1 = Employee(10000 ,45, 'Bob')
E2 = Employee(7000 ,35, 'Jane')
E3 = Employee(5000 ,25, 'Jack')

print (E1.name)
print ("Age of E2: ", E2.age)
print ("Salary of E3: "), E3.printSalary()

#one freaky thing
E1.role = 'Supervisor'
print ("E1's role: ", E1.role)

E = [E1, E2, E3]

for person in E:
    print (person.name)

for dude in E:
    dude.raiseSalary()

E1.myExternalFunction()
