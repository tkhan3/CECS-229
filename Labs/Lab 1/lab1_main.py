# Lauro Cabral
# CECS 229
# March 12,2018
# Lab 1


# 1. Define a one-line procedure cubes(L) 
def cubes(L): return [ x**3 for x in L]
x = [1,2,3]
print "1. " , cubes(x)

# 2. Define a one-line procedure dict2list(dct,keylist)
def dict2list(dct, keylist): return [ dct[i] for i in keylist]
dct={'a':'A', 'b':'B', 'c':'C'}
keylist=['b','c','a']
print "2. " , dict2list(dct,keylist)

# 3. Define a one-line procedure list2dict(L, keylist)
def list2dict(L, keylist): return { keylist[i]:L[i] for i in range(len(L)) }
L=['A','B','C']
keylist=['a','b','c']
print "3. " , list2dict(L,keylist)