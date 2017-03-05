#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    for i in range(len(lst) - 1):
        made_swap = False
        for j in range(len(lst) - 1 - i):  # Each round we have one less sort on the end

            if lst[j] > lst[j + 1]:

                # If the left is larger than the right, make the swap
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True

        # if no swap was made, the list is sorted
        if not made_swap:
            break

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    merged = []

    while len(list1) > 0 or len(list2) > 0:
        # if there are items left in one of the lists,
        # add to the merged list
        if list1 == []:
            merged.extend(list2)
            list2 = []
        elif list2 == []:
            merged.extend(list1)
            list1 = []
        elif list1[0] <= list2[0]:
            # append and remove first item of lst1
            merged.append(list1.pop(0))
        else:
            # append and remove first item of lst2
            merged.append(list2.pop(0))

    return merged


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    # This is the base case - a list of one, which is inherently sorted
    # This also takes care of an empty list being passed to the function
    if len(lst) <= 1:
        return lst

    # Cut the list in two halves
    mid = int(len(lst) / 2)
    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])

    return merge_lists(lst1, lst2)




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
