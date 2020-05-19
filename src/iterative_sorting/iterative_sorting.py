# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # sort the arr
    for i in range(1, len(arr)):
        curr_bubble = arr[i]
        j = i
        # put curr_bubble in the appropriate spot in our sorted half
        # loop through our sorted half and find the appropriate spot
        while j > 0 and curr_bubble < arr[j - 1]:
            # taking the j - 1th bubble and copying it over to the jth spot
            # arr[j], arr[j -1] = arr[j - 1], arr[j]
            arr[j] = arr[j - 1]
            j -= 1
        # insert the bubble at the correct position
        arr[j] = curr_bubble

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    if len(arr) == 0:
        return arr

    # if maximum is not given, we'll take the max value from the input array
    if maximum == -1:
        maximum = max(arr)

    # make a bunch of counter       always include +1
    counter = [0] * ( maximum + 1 )
    # counter = [0 for _ in range(maximum+1)] # this works as well

    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counter[i] += 1

    # we have the counts of every value in our input array
    # loop through our buckets, starting at the smallest index
    ndx = 0
    for i in range( len( counter ) ):
        while 0 < counter[i]:
            arr[ndx] = i
            ndx += 1
            counter[i] -= 1

    return arr
