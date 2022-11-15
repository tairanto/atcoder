#!/usr/bin/python3


import itertools
#nPr
tmp = ['a', 'b', 'c',]
print(list(itertools.permutations(tmp,2)))

#nCr
tmp = ['a', 'b', 'c',]
print(list(itertools.combinations(tmp,2)))