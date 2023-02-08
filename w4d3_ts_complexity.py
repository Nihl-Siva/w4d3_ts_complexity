# PROBLEM 1:
#   Write a function that takes in two non-empty arrays of integers, finds the
#   pair of numbers (one from each array) whose absolute difference is closest to
#   zero, and returns an array containing these two numbers, with the number from
#   the first array in the first position.
#   Note that the absolute difference of two integers is the distance between
#   them on the real number line. For example, the absolute difference of -5 and 5
#   is 10, and the absolute difference of -5 and -4 is 1.

#  You can assume that there will only be one pair of numbers with the smallest
#   difference.

# EXAMPLE
# input arrayOne = [-1, 5, 10, 20, 28, 3]
# input arrayTwo = [ 26, 134, 135, 15, 17]

# output = [28, 26]
# Explanation: The absolute difference between 28 & 26 is 2 which is the lowest absolute difference.

# Original Solution: (Time: O(n^2))

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [ 26, 134, 135, 15, 17]

# def abs_diff(arrayOne, arrayTwo):
#     min_pair = [arrayOne[0], arrayTwo[0]]
#     min_diff = abs(arrayOne[0] - arrayTwo[0])
#     for num1 in arrayOne:
#         for num2 in arrayTwo:
#             diff = abs(num1 - num2)
#             if diff < min_diff:
#                 min_diff = diff
#                 min_pair = [num1, num2]
#     print(min_pair)
# abs_diff(arrayOne, arrayTwo)


# Optimized Solution: (Time: O(n log n))

def abs_diff(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    min_pair = [arrayOne[0], arrayTwo[0]]
    min_diff = abs(arrayOne[0] - arrayTwo[0])
    i = 0
    j = 0
    while i < len(arrayOne) and j < len(arrayTwo):
        diff = abs(arrayOne[i] - arrayTwo[j])
        if diff < min_diff:
            min_diff = diff
            min_pair = [arrayOne[i], arrayTwo[j]]
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1
    print(min_pair)

abs_diff(arrayOne, arrayTwo)



# PROBLEM 2:
# Check if Number and its double exists
# Given an array arr of integers, check if there exists two integers N and M 
# such that N is the double of M ( i.e. N = 2 * M).

# Example 1:
# arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
# Example 2:
# arr = [7,1,14,11]
# Output: true
# Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
# Example 3:
# arr = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist N and M, such that N = 2 * M.

# Original Solution: (Time: O(n^2))

arr1 = [10,2,5,3] #T
arr2 = [7,1,14,11] #T
arr3 = [3,1,7,11] #F

# def doubles(n):
#     dub=[]
#     for single in n:
#         m=single*2
#         if m in n:
#             dub.append(m)    
#     for i in dub:
#         if i in n:
#             return True
#     return False

# print(doubles(arr1))
# print(doubles(arr2))
# print(doubles(arr3))


# Optimized Solution: (Time: O(n))
def doubles(n):
    dub=[]
    n_set = set(n)
    for single in n:
        m=single*2
        if m in n_set:
            dub.append(m)
    for i in dub:
        if i in n_set:
            return True
    return False

print(doubles(arr1))
print(doubles(arr2))
print(doubles(arr3))

