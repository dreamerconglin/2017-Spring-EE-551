f = open("newFile.txt",'a')
f.write("\n This will create new lines \n Each time you say \n")
f.write(" More text \n And a little more \n But notice they are formatted")
f.close()

f = open("newFile.txt", 'r')
mystr = f.read()
print (mystr)
f.close()

f = open("newFile.txt", 'r')
for line in f.readlines():
    print (line)
f.close()
