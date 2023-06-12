# quicksort and partition functions are based on:
# https://github.com/tryber/sd-025-b-live-lectures
# /blob/lecture/cs/2.3/sort/quick_sort.py

def quicksort(array, low, high):
    # Recursive function to sort the array using the Quicksort algorithm
    if low < high:
        # If the lower index is less than the higher index,
        #  there are elements to be sorted
        partition_index = partition(array, low, high)
        # Finds the partition index by rearranging the array elements
        quicksort(array, low, partition_index - 1)
        # Recursively sorts the elements before the partition index
        quicksort(array, partition_index + 1, high)
        # Recursively sorts the elements after the partition index


def partition(array, low, high):
    # Function to find the partition index
    #  and rearrange the array elements accordingly
    i = low - 1
    # Initializes a variable to keep track of the smaller elements
    pivot = array[high]
    # Selects the last element of the array as the pivot

    for j in range(low, high):
        # Iterates through the array from low to high-1
        if array[j] <= pivot:
            # If the current element is less than or equal to the pivot
            i = i + 1
            # Increments the smaller element index
            array[i], array[j] = array[j], array[i]
            # Swaps the current element with the smaller element

    array[i + 1], array[high] = array[high], array[i + 1]
    # Swaps the pivot element with the element at the partition index

    return i + 1
    # Returns the partition index


# is_anagram function is based on:
# https://www.geeksforgeeks.org/python-program-to-check-whether-two-strings-are-anagram-of-each-other/
def is_anagram(first_string, second_string):
    # Function to check if two strings are anagrams
    if first_string == "" and second_string == "":
        # If both strings are empty, they are not anagrams
        return "", "", False

    first_string = list(first_string.lower())
    second_string = list(second_string.lower())
    # Converts the strings to lowercase
    #  and converts them to lists of characters

    quicksort(first_string, 0, len(first_string) - 1)
    quicksort(second_string, 0, len(second_string) - 1)
    # Sorts the lists using the Quicksort algorithm

    first_string = "".join(first_string)
    second_string = "".join(second_string)
    # Converts the sorted lists back to strings

    if first_string == second_string:
        # If the sorted strings are equal, they are anagrams
        return first_string, second_string, True

    return first_string, second_string, False
    # Returns the sorted strings and a boolean
    #  indicating if they are anagrams or not
