from urllib2 import urlopen

# 1
f = urlopen("http://www.example.com")
print f.read(500);

# 2
print urlopen('http://www.example.com').read(500);

# 3 : post
