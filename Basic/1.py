#Operators in python 
#Assignment Op
a = 10
b = "Ten"
c = 10.02
d = True
print(a,b,c,d)

#Arithmatic Op
a = 10
b = 10
print(a+b)
print(a-b)
print(a//b)
print(a%b)
print(a*b)

#comparision operator
print(1>2)
print(1<2)
print(1==2)
print(1!=2)


#checking operator type using type function and isinstanse function
print(type(a)==int)
print(isinstance(b,str))

#logical operator
print(True and True)
print(False or True)
print(not False)

#logical bitwise operator 
print(10&10)
print(10|1)
print(~10)
print(10<<1)
print(10>>1)

#Ternary operator
r = True if 20 > 18 else False
print(r)

#Membership  operator 
print(9 in range(1,10))

#Identity operator 
print(a is b)