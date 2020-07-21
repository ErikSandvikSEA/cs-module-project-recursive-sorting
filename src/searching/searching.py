# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # if the pointers cross, means the target is not in the array
    # acts as a basecase
    if start > end:
        return -1

    # caputure mid point
    mid = (start + end) // 2

    # match checker and acting base case
    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        # move the end index to mid and back one and recurse
        return binary_search(arr, target, start, mid - 1)

        # move the start index to mid and forward one and recurse
    else:
        return binary_search(arr, target, mid + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here

