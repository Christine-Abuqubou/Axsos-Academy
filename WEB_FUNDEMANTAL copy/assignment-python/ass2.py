# print all integers from 0 to 150

for i in range(151):   
    print(i)

    # print multiplies by 5
    for i in range(5, 1001, 5):
        print(i)

    # counting the dogo way
    for i in range(1, 101):
        if i % 10 == 0:
            print("coding dojo")
        elif i % 5 == 0:
            print("coding")
        else:
            print(i)

# add odd integers
total = 0
for i in range(0, 50001, 1):
    if (i%2==0):
     total += i
print("final sum is ", total)

    # count by four
for i in range(2018, 0, -4):
    print(i)

        # low num ,highnumP
x = 2
y = 9

for i in range(x, y + 1):
    if i % 3 == 0:
        print(i)
