import random
def randInt( min=0, max=500  ):
    num = random.random()*(max-min)+min
    return num
print(randInt(0,101))
print(randInt(max=51))
print(randInt(min=50))
print(randInt(min=50,max=501))



