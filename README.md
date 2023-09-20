Challenge Title: Anagram Detector

Description:
This coding challenge focuses on implementing a function to detect whether two given strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once.

Function Signature:

python
Copy code
def is_anagram(first_string, second_string):
    # Function to check if two strings are anagrams
    pass
Input:

first_string (str): The first input string.
second_string (str): The second input string.
Output:

Returns a boolean value indicating whether the two input strings are anagrams.
Example:

python
Copy code
result = is_anagram("listen", "silent")
print(result)  # Output: True

result = is_anagram("hello", "world")
print(result)  # Output: False
Explanation:
The is_anagram function takes two input strings, converts them to lowercase, sorts them using the Quicksort algorithm, and then compares them. If the sorted strings are equal, the function returns True, indicating that the input strings are anagrams of each other. Otherwise, it returns False.

Note:

The code uses the Quicksort algorithm for efficient string sorting.
Empty strings are not considered anagrams.
