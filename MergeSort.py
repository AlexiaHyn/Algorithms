import math

# running time: O(nlogn) using Master Theorem
def merge_sort(L):
    """
    Sort list L in ascending order
    :param L: a list L[0...n-1] of "orderable" elements
    :return: None
    """
    n = len(L)
    if n == 0:
        print("Empty Input")
    # elif n == 1:
    #     do nothing
    elif n > 1:
        left = L[0: math.floor(n / 2)]
        right = L[math.floor(n / 2):]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, L)

# running time: O(n)
def merge(left, right, L):
    """
    Modifies list L to contain elements in ascending order
    :param left: a sorted list
    :param right: a sorted list
    :param L: a list containing the elements of left and right
    :return: None
    """
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[k] = left[i]
            i += 1
        else:
            L[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        L[k:] = right[j:]
    else:
        L[k:] = left[i:]

# # uncomment to run the test cases
# # test merge() prints expected result with left and right of short lengths
# left1 = [1]
# right1 = [2]
# L1 = [2, 1]
# merge(left1, right1, L1)
# print(L1)
#
# # test merge() prints expected result with left and right of equal lengths
# left2 = [1, 3, 5]
# right2 = [2, 4, 6]
# L2 = [1, 5, 3, 6, 4, 2]
# merge(left2, right2, L2)
# print(L2)
#
# # test merge() prints expected result with left and right of different lengths
# left3 = [1, 3, 8]
# right3 = [2, 4, 6, 7, 9]
# L3 = [8, 1, 3, 6, 4, 2, 9, 7]
# merge(left3, right3, L3)
# print(L3)
#
# # test merge() on duplicate elements
# left4 = [1, 3, 8]
# right4 = [3, 8, 9]
# L4 = [8, 1, 3, 8, 9, 3]
# merge(left4, right4, L4)
# print(L4)

# # test merge_sort() on one single element
# ms_L1 = [7]
# merge_sort(ms_L1)
# print(ms_L1)
#
# # test merge_sort() on two elements
# ms_L2 = [7, 1]
# merge_sort(ms_L2)
# print(ms_L2)
#
# # test merge_sort() on list of larger size
# ms_L3 = [7, 1, 4, 8, 5, 4, 9]
# merge_sort(ms_L3)
# print(ms_L3)


