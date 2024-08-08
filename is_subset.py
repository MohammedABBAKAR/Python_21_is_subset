# Is One List a Subset of Another?

# Create a function that returns True if the first list is a subset of the second. 
# Return False otherwise.
# Examples

# is_subset([3, 2, 5], [5, 3, 7, 9, 2]) ➞ True

# is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]) ➞ True

# is_subset([1, 2], [3, 5, 9, 1]) ➞ False



def is_subset(lst1, lst2):

    for ls1 in lst1:
        if ls1 in lst2:
            return True
        else:
            return False
print(is_subset([1, 2], [3, 5, 9, 1]) )




def is_subset(lst1, lst2):
    # Iterate through each element in lst1
    for element in lst1:
        # Check if the element is in lst2
        if element not in lst2:
            return False
    return True

# Test cases
print(is_subset([3, 2, 5], [5, 3, 7, 9, 2])) 
print(is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]))  
print(is_subset([1, 2], [3, 5, 9, 1]))



def is_subset(lst1, lst2):
    # Check if each element in lst1 is in lst2
    return all(element in lst2 for element in lst1)

# Test cases
print(is_subset([3, 2, 5], [5, 3, 7, 9, 2]))  # ➞ True
print(is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]))  # ➞ True
print(is_subset([1, 2], [3, 5, 9, 1]))  # ➞ False
