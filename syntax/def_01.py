def sum(a=1, b=2, c=3):
    return "%d %d %d" % (a,b,c)

print "=" * 50
print sum(3, 4, 5)

print "=" * 50
print sum(3, 4)

print "=" * 50
print sum(3, c=6666)