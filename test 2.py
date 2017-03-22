#comment: Single line comment

#====
# Part-1
#====

a = 5
print (a)
a = "Allowed?"
print (a)

a, b, c = 1, 15, 9
print (b)
print (c)

a, b = 5, "Other than number"
a, b = b, a
print (a)
print (b)

x = input ("Enter a number: ")
x = int (x)
x = x + 1
print (x)

#====
# if-else
#====

if x > 0 and x < 100:
    print ("x is positive")
    print ("I have so much to say")
elif x == 0 or x < -100:
    print ("It's zero!!")
else:
    print ("Definitely negative")
    print ("More things for negative")

#====
#DData Structure in 5 lines of code
#====

x = [1, 2, 3.1487, "Wow this is allowed", 9876]
print (x[0])
print (x[2])
print (x[3])
print (x.count(1))

#====
#Loops in Python
#====
#for(int i = 0; i < 10; i++)
for i in range(10):
    print ("Print this a bunch of times")
for item in x:
    print (item)

S= "Python is awesome"
for item in S:
    print (item)
    if item == 'a':
        print("=======")
