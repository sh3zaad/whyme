def bubble_sort(items):

    '''Returns array of items, sorted in ascending order'''

    # iterate through entire array comparing two pairs of numbers and swapping if it passes a condition
    for x in range(len(items)):
        for y in range(len(items)-1-x):
            if items[y] > items[y+1]:
                items[y], items[y+1] = items[y+1], items[y]

    return items


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

    # define a linear merge in order to merge the two resulting lists
    def linear_merge(list1, list2):

        # initialize a new list
        new_list = []
        while (len(list1) > 0  and len(list2) > 0):
            if list1[0] < list2[0]:
                new_list.append(list1.pop(0))
            else:
                new_list.append(list2.pop(0))

        return new_list + list1 + list2

    # split items in half
    len_items = len(items)
    if len_items == 1:
        return items

    middle = int(len_items/2)
    list1 = merge_sort(items[:middle])
    list2 = merge_sort(items[middle:])

    # megre the two sorted lists
    return linear_merge(list1, list2)


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

    len_items = len(items)

    if len_items <= 1:
        return items

    pivot = items[-1] # start with last value in items
    small = []
    large = []
    duplicate = []

    for x in items:
        if x < pivot:
            small.append(x)
        elif x > pivot:
            large.append(x)
        elif x == pivot:
            duplicate.append(x)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + duplicate + large
