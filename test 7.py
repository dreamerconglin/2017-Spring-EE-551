def make_increments(n):
    return lambda x : x+n

inc5 = make_increments(5)
inc10 = make_increments(10)
inc100 = make_increments(100)

print (inc5(20))
print (inc10(20))
print (inc100(20))
