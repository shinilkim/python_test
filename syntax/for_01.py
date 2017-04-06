
language = ['python','perl','c','java']

# for 1
print '[A-01] for 1'
for lang in language:
    if lang in ['python','perl']:
        print "%6s need interpreter" % lang
    elif lang in ['c','java']:
        print "%6s need compiler" % lang
    elif lang in ['nodejs']:
        print 'not found nodejs'
    else:
        print "should not reach here"

print
# for2
print '[A-02] for 2'
for a in [1,2,3]:
    print a