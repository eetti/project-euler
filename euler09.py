#Works!

a = 1
b = 1
c = 998

def verify(a, b, c):
        if a ** 2 + b ** 2 == c ** 2:
            print a,b,c
            if a + b + c == 1000:
                return True

def py_trip():
    for i in xrange (1, 1000):
        a = i
        for j in xrange (1, 1000):
            b = j
        #        for k in xrange (1, 1000):
            c = 1000 - a - b
            if c < 0: break 
            if verify(a,b,c):
                print a,b,c,a*b*c

print py_trip()

#print [sorted((x, y , z) for x in range (1, 30) for y in range (1, 30) for z in range (1, 30) if x**2 + y**2 == z**2)]


#py_triplet = lambda a, b, c: a**2 + b**2 == c ** 2
#py_triplet(3, 4, 5)
