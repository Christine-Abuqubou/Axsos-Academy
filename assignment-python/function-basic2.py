# count down function
def Count_Down(num):
    result = []
    for i in range(num, 0, -1):
        print(i)
        result.append(i)
    return result


print(Count_Down(5))

# print and return values by function


def print_and_return(list):
    print(list[0])
    return (list[1])

result=print_and_return([1,2])
print(result)

#return the first value plus list of length

def first_plus_length(list):
    return list[0]+len(list)

print(first_plus_length([1,2,3,4,5]))

#values greater than secon
def values_greater_than_second(lst):
   if len(lst) < 2:
       return False
   second_value = lst[1]
   new_list = [x for x in lst if x > second_value] #check each element of x
   print(len(new_list))  # Print how many values
   return new_list
# Example 
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))

# Returns: [5, 3, 4]
print(values_greater_than_second([3])) #it will return false

#length and

def length_and_value(size, value):
   return [value] * size    #it will repeat the value
# Example 
print(length_and_value(4, 7))  # Output: [7, 7, 7, 7]
print(length_and_value(6, 2))  # Output: [2, 2, 2, 2, 2, 2]


