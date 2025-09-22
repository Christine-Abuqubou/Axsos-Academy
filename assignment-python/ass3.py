#1   it print 5
def a():
    return 5
print(a())


#2  it print 5+5
def a():
    return 5
print(a()+a())




#3  no return just it print  the element inside  the funtion
def a():
    return 5
    return 10
print(a())



#4  same as #3
def a():
 return 5
print(10)
print(a())

#5 x=5
def a():
    print(5)
x = a()
print(x)

#6 nontype erorr 
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#7  return "25"
def a(b,c):
    return str(b)+str(c)
print(a(2,5))



#8   print 100  ,return 5
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())





#9 return7 ,return14, print 21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))




#10   return 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))





#11 print 500 , 
b = 500
print(b) # 500
def a():
    b = 300
    print(b) # 300
print(b) # 500
a()
print(b) # 500


#12
b = 500
print(b) # 500
def a():
    b = 300
    print(b) # 300
    return b # retrun 300
print(b) # 500
a()
print(b) # 500





#13
b = 500
print(b) # 500
def a():
    b = 300
    print(b) # 3 00
    return b # return 300
print(b) # 500
b=a() # b=300
print(b) # 300


#14
def a():
    print(1) # print 1
    b() # print 3
    print(2) #print 2
def b():
    print(3) 
a()


#15
def a():
    print(1) # print 1
    x = b() # x  = 5
    print(x) #print 5
    return 10 # return 10
def b():
    print(3) # print 3
    return 5  #return 5
y = a() # a = 10
print(y) #print 10