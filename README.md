# Crypto

The Four Functions

In this project, you are going to create a program that will encrypt, decrypt, and hash text.

Your first goal is to define the encrypt_text function, which consumes a string representing a user's message, and produces an encrypted version.

You will also need to define the decrypt_text which consumes the encrypted version and produces the user's message.

Third, you need to define the hash_text which consumes a message and produces a unique hash. The hash is a way to convert text to a number that is likely to be unique for each possible string. If someone has tampered with the message, the hash value will be different from what was given.

Finally, you'll put it all together into a single main program. This will be a user interface for people who want to use your other functions.

Function Signatures

Over the course of this project, you will define the following four functions:
encrypt_text: Consumes a string (plaintext message) and an integer (rotation_amount), and produces a new string that is encrypted.
decrypt_text: Consumes a string (encrypted message) and an integer (rotation_amount), and produces a new string that is decrypted.
hash_text: Consumes a string (any kind of message) and two integers (base and hash_size), and produces an integer that attempts to uniquely represent the text.
main: Consumes nothing and produces nothing. Instead, takes user input to encrypt or decrypt a message.


Decomposition

A function to convert a string to a list of integers using ord
A function to convert a list of integers to a string using chr
A function to rotate a list of integers by a given amount.
If you complete these three helper functions, then the remaining functions are all much easier.

