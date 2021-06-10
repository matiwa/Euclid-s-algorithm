a=int(input("Enter a: "))
b=int(input("Enter b: "))
a2=a
b2=b

#Algorithm version
while a!=b:
    if a>b:
        a-=b
    elif a<b:
        b-=a
print("GCD="+str(a))

'''Modulo version'''
while b2!=0:
    c=a2%b2
    a2=b2
    b2=c
print("GCD="+str(a2))