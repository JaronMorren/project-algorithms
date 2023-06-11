def is_palindrome_recursive(word, low_index, high_index):
    # Checks if the input word is empty
    if not word:
        return False
    # An empty string is not a palindrome

    # Checks if the low_index has surpassed or reached the high_index
    if low_index >= high_index:
        return True
    # All necessary comparisons have been made, indicating a palindrome

    # Checks if the characters at the low_index
    #  and high_index positions are not equal
    if word[low_index] != word[high_index]:
        return False
    # Characters do not match, indicating not a palindrome

    # Recursively calls the function with incremented low_index
    #  and decremented high_index
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
