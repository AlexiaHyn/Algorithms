import math

# running time: O(logn) using Master Theorem
def binary_search(L, x):
    """
    check if element x is in L
    :param L: an ordered list
    :param x: an element
    :return: true if found, false if not found
    """
    n = len(L)
    if n == 0:
        return False
    if n == 1:
        return L[0] == x

    if n > 1:
        mid_idx = math.floor(n / 2)
        mid = L[mid_idx]
        if mid == x:
            return True
        if mid < x:
            return binary_search(L[mid_idx:], x)
        elif mid > x:
            return binary_search(L[0:mid_idx], x)


# # Uncomment to run the test case
# # test binary_search on one element
# test_true = binary_search([3], 3)
# print(test_true)
# test_false = binary_search([2], 3)
# print(test_false)
#
# # test binary search on two elements
# print(binary_search([3, 4], 3)) # test true
# print(binary_search([1, 2], 3)) # test false
# print(binary_search([5, 6], 3)) # test false

# # test binary search on list with larger size
# # L = [1, 4, 7, 8, 9, 13, 17]
# # print(binary_search(L, 8)) # test true: x right in the middle
# # print(binary_search(L, 1)) # test true: x on left side
# # print(binary_search(L, 13)) # test true: x on right side
# # print(binary_search(L, 6)) # test false: x on right side