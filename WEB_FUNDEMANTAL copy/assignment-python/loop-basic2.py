def biggie_size(list):

    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list


# Example
print(biggie_size([-1, 3, 5, -5]))
# Output: [-1, 'big', 'big', -5]

print(biggie_size([10, 2, -3, 4, 0]))
# Output: ['big', 'big', -3, 'big', 0]


def sum_total(list):

    total = 0
    for i in list:
        total += i
    return total


print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))


def calculate_average(data_list):

    if not data_list:
        return 0  # Handle empty list case

    total_sum = sum(data_list)
    average = total_sum / len(data_list)
    return average


# Example usage:
my_numbers = [10, 20, 30, 40, 50]
avg = calculate_average(my_numbers)
print("The average of the list  " , avg)

empty_list = []
avg_empty = calculate_average(empty_list)
print("The average of the empty list  " ,avg_empty)


def get_list_length(list):

    return len(list)


# Example 
my_list = [37, 2, 1, -9]
length = get_list_length(my_list)
print("The length of the list  " ,length)


empty_list = []
length_2 = get_list_length(empty_list)
print(f"The length of the empty list is: {length_2}")


def find_minimum(numbers):

    if not numbers:
        return False
    else:
        minimum_value = numbers[0]
        for num in numbers:
            if num < minimum_value:
                minimum_value = num
        return minimum_value


print(find_minimum([37, 2, 1, -9]))
print(find_minimum([]))


def find_maximum(numbers):

    if not numbers:
        return False
    else:
        max_value = numbers[0]
        for num in numbers:
            if num > max_value:
                max_value = num
        return max_value


print(find_maximum([37, 2, 1, -9]))
print(find_minimum([]))


def reverse_list_in_place(input_list):

    left = 0
    right = len(input_list) - 1

    while left < right:
        # Swap elements at left and right pointers
        input_list[left], input_list[right] = input_list[right], input_list[left]

        # Move pointers towards the center
        left += 1
        right -= 1

    return input_list


# Example usage:
my_list = [37, 2, 1, -9]
reversed_my_list = reverse_list_in_place(my_list)
print(f"Original list after reversal: {reversed_my_list}")


def ultimate_analysis(lst):
    analysis = {}  # Create an empty dictionary

    analysis["sumTotal"] = sum(lst)
    analysis["length"] = len(lst)
    analysis["average"] = analysis["sumTotal"] / analysis["length"]
    analysis["minimum"] = min(lst)
    analysis["maximum"] = max(lst)

    return analysis


# Example usage
print(ultimate_analysis([37, 2, 1, -9]))


def count_positives(list4):
    count = 0
    for num in list4:
        if num > 0:
            count += 1

    if list4:  # Make sure the list is not empty to avoid IndexError
        list4[-1] = count #it refer to last element in array

    return list4
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

