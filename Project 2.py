from bakery import assert_equal

# Copy over existing code from earlier parts of the project

from bakery import assert_equal
from bakery import assert_equal
def rotate(original: int, rotation: int)-> int:
    """
    This function rotates the original integer by a certain amount 
    and produces a new integer, using the ASCII table equation.
    Args:
        original(int): original number before rotation 
        rotation: amount for rotation
    Returns:
        int: number after rotation
    """
    rotated = (original+rotation-32) % 94 + 32
    return rotated

# 1) Define encrypt_text
def encrypt_text(message:str, rotation:int)-> str:
    """
    This function consumes a string representing a user's message,
    and produces an encrypted version.
    Args: 
        message(str): original message
        rotation_amount(int): given amount for rotation on ASCII table
    Returns:
        str: encrypted version of message
    """
    #Convert the string to a list of integers using ord.
    result = []
    new_result = []
    final = ""
    for letter in message:
        result.append(ord(letter))
    for num in result:
    #Insert the tilde ASCII value (126, which translates to "~") after every integer less than 48. Hint: Append more than once.
        new_num = rotate(num, rotation)
        new_result.append(new_num)
        if num < 48:
            new_result.append(126)
   #Convert the list of integers back to a string using chr.
    for number in new_result:
        final += chr(number)
    return final
# 2) Define decrypt_text
def decrypt_text(message:str,rotation:int)-> str:
    """
    This function consumes the encrypted version and produces the user's message
    Args:
        message(str): original message
        rotation_amount(int): given amount for rotation on ASCII table
    Returns:
        str: decrypted version of message
    """
    result = []
    new_result = []
    final_result = []
    final = ""
    for letter in message:
        result.append(ord(letter))
    for num in result:
        if num != 126:
            new_result.append(num)
            rotated = rotate(num, -rotation)
            final_result.append(rotated)
    for number in final_result:
        final += chr(number)
    return final
assert_equal(decrypt_text("A",1), "@")  
assert_equal(decrypt_text("DBU",1), "CAT")  
assert_equal(encrypt_text("CAT", 1), "DBU")
assert_equal(encrypt_text("A", 1), "B")
assert_equal(encrypt_text("32", 3), "65")
assert_equal(encrypt_text("A", 0), "A")
assert_equal(encrypt_text("A", 0), "A")
def hash_text(message:str, base:int, hash_size:int)->int:
    """
    This function consumes a message and produces a unique hash.
    Args:
        message(str): original message
        base(int): arbitrarily chosen base
        hash_size(int): size of hash
    Returns:
        int: attempts to uniquely represent the text.
    """
    result = []
    total = 0
    for index, letter in enumerate(message):
        letter= ord(letter)
        new_value = (index + base) ** (letter)
        total += new_value
    answer = total % (hash_size)
    return answer
assert_equal(hash_text("Hello", 31,1000000000),590934605)
assert_equal(hash_text("A", 11, 100), 51)
assert_equal(hash_text("ABC", 33, 10000), 9484)
def main():
    """
    This function will encrypt, decrypt, and hash text and takes user input to encrypt or decrypt a message.
    """
    choice = input("Would you like to encrypt or decrypt text?")
    if choice == "encrypt":
        message = input("Please enter a message.")
        encrypt_value = encrypt_text(message, 1)
        hashed_value = hash_text(message, 31, 100000000)
        exp_hash = input("Please enter the expected hash.")
        if encrypt_value == exp_hash:
            print(encrypt_value, hashed_value)
        else: 
            print("error!")
    elif choice == "decrypt":
        message = input("Please enter a message.")
        decrypt_value = decrypt_text(message, 1)
        hashed_value = hash_text(message, 31, 100000000)
        exp_hash = input("Please enter the expected hash.")
        if decrypt_value == exp_hash:
            print (decrypt_value, hashed_value)
        else: 
            print("error!")
    print("error1!")
main()