# A palindrome is a string that reads the same forward and backward
# Example radar or madam

# Solution 1 brute force

def is_palindrome(str):
    original_str = str
    reverse_str = str[::-1]

    if original_str == reverse_str:
        return True

    return False

#Solution 2 Elegant solution

def is_palindrome_py(str):
    return str==''.join(str[::-1])

str = 'rada'
print(is_palindrome(str))