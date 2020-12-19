#Program to print number of lines
a=input()
f=open(a,'r')
x=f.readlines()
b=x.count('\n')
for i in range(b):
    x.remove('\n')
print(len(x))
f.close()
