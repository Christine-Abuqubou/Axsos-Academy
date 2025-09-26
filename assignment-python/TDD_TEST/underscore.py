class Underscore:
    def map(self, iterable, callback):
        # Apply the callback to each item and return the results
        return [callback(item) for item in iterable]

    def find(self, iterable, callback):
        # Return the first item where callback(item) is True
        for item in iterable:
            if callback(item):
                return item
        return None

    def filter(self, iterable, callback):
        # Return a list of items where callback(item) is True
        return [item for item in iterable if callback(item)]

    def reject(self, iterable, callback):
        # Return a list of items where callback(item) is False
        return [item for item in iterable if not callback(item)]

# Create an instance of the Underscore class
_ = Underscore()
print(_.map([1, 2, 3], lambda x: x * 2))  
# Output: [2, 4, 6]

# 2. find: first value > 4
print(_.find([1, 2, 3, 4, 5, 6], lambda x: x > 4))  
# Output: 5

# 3. filter: only even numbers
print(_.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))  
# Output: [2, 4, 6]

# 4. reject: remove even numbers (i.e., keep odd numbers)
print(_.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))  
# Output: [1, 3, 5]

# Example usage:
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)  # Output: [2, 4, 6]
_.map([1,2,3], lambda x: x*2) # should return [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]