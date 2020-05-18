def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # figute out the total size of the arr
    low = 0
    high = len(arr) -1 

    while low <= high:
        # find the midpoint
        midpoint = (low + high) // 2

        # check to see if the midpoint element is our target
        if arr[midpoint] == target:
            return midpoint

        # check to see if the element should be low or high of the midpoint
        if arr[midpoint] < target:
            # toss out the low of the arr
            # update out `low` index
            low = midpoint + 1

        # otherwise, arr[mid] > target
        else:
            # toss out the high of the arr because the element has to be low
            high = midpoint -1

    return -1  # not found
