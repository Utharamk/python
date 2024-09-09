a=('a','b','c','d')
a=list(a)
a[1]='z'
print("changed list:",a)
a=tuple(a)
print(a)