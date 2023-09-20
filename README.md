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


Challenge Title: Message Encryption

Description:
This coding challenge involves the creation of a function to encrypt messages using a given key. The encryption algorithm involves dividing the message into two parts and reversing them based on the provided key.

Function Signature:

python
Copy code
def encrypt_message(message: str, key: int) -> str:
    # Function to encrypt a message using a key
    pass
Input:

message (str): The input message to be encrypted.
key (int): The encryption key used to determine the division and reversal of the message.
Output:

Returns the encrypted message as a string.
Example:

python
Copy code
encrypted = encrypt_message("Hello, World!", 3)
print(encrypted)  # Output: "leHlo, Wo_dlr!"

encrypted = encrypt_message("Python is fun", 6)
print(encrypted)  # Output: "sixf___nys htoP"
Explanation:
The encrypt_message function takes an input message and an encryption key. It performs the following steps:

It checks the validity of the input types and raises a TypeError if either the key is not an integer or the message is not a string.

It checks if the key is within a valid range (1 to the length of the message). If not, it reverses the entire message.

If the key is within the valid range, it divides the message into two parts: the first part contains the characters before the key index, and the second part contains the characters after the key index.

Depending on whether the key is even or odd, it reverses the order of the two parts.

It joins the reversed parts with an underscore "_" and returns the encrypted message.

Note:

The encryption algorithm involves reversing portions of the message based on the key.
The key must be an integer, and the message must be a string for the function to work properly.
