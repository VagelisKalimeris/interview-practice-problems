from collections import Counter


################################################################################
# Objective         : Given an array of integers, nums, and an integer value,  #
#                     target, determine if there are any three integers in     #
#                     nums whose sum equals the target. Return TRUE if three   #
#                     such integers are found in the array. Otherwise, return  #
#                     FALSE.                                                   #
# Time Complexity   : O(n^2)                                                   #
# Space Complexity  : O(n)                                                     #
################################################################################
def contains_sum_of_3(target, nums):
    hash_arr = Counter(nums)

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and (hash_arr[target - nums[i] - nums[j]]
                           - hash_arr[i] - hash_arr[j]) > 0:
                return True

    return False


################################################################################
# Objective         : Given a sorted array arr with possibly duplicate         #
#                     elements, the task is to find indexes of the first and   #
#                     last occurrences of an element n in the given array.     #
# Time Complexity   : O(n)                                                     #
# Space Complexity  : O(1)                                                     #
################################################################################
def first_and_last(arr, n):
    first = last = None

    for i in range(len(arr)):
        if arr[i] == n:
            if first is None:
                first = last = i
            else:
                last = i
    return first, last


print(first_and_last([123, 3, 5, 5, 5, 5, 67, 123, 125], 123))
