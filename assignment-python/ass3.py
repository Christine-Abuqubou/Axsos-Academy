#1   it print 5
def a():
    print (5)
print(a())


#2  it print 5+5
def a():
     return 5
    
    
print(a()+a())




#3  no return just it print  the element inside  the funtion
def a():
    return 5    #it will return 5 and stop
    return 10
print(a())



#4  same as #3
def a():
 return 5
print(10)   #it will print 10 and return 5
print(a())

#5 x=5
def a():
    print(5)
x = a()
print(x)

#6 it will return non by default since the function has no return statment
def a(b,c):
    print(b+c) #the right way is return b+c
print(a(1,2) + a(2,3)) #each of them print 3 and 5 but it returns none so none+none =error

#7  return "25" as a string
def a(b,c):
    return str(b)+str(c)
print(a(2,5))



#8   print 100  ,return  10 and stop
def a():
    b = 100   #set variable b=10
    print(b)
    if b < 10: 
        return 5
    else:
        return 10
    return 7 #cant reach
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




#10   return 8 and stop
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


#14 so it print 132
def a():
    print(1) # print 1
    b() # call the fun b which print 3
    print(2) #print 2
def b(): 
    print(3)  #print 3
a()


#15  so the output will be 1,3,5,10
def a():
    print(1) # print 1
    x = b() # x  = 5   call b and return the value  in x  which equal 5
    print(x) #print 5  
    return 10 # return 10
def b():
    print(3) # print 3
    return 5  #return 5
y = a() #    inside function a print 1 and  runs b which print 3 and reurn 5 =x
print(y) #print 10 by return function of a it returns 10