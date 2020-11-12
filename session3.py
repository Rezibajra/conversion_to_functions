"""
    Display all prime numbers from 1 to 100
"""
def is_prime(num):
    """Check whether number is prime or not"""
    if num == 1 or num == 2:
        return True
    
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

def main():
    for i in range(1, 100):
        if is_prime(i):
            print(i)
    
if __name__ == "__main__":
    main()


"""
    Ask user for a string
    Print whether the string is a palindrome or not.
"""
def is_palindrome(str):
    """Change the string to lowercase"""
    str = str.lower()
    """Reverse the string"""
    _reverse = str[::-1]
    print('Reversed string :', _reverse)
    """Comparing two strings"""
    if list(str) == list(_reverse):
        return True
    else:
        return False
    
def main():
    my_str = input('Enter a string: ')
    if is_palindrome(my_str):
        print('String is palindrome')
    else:
        print('String is not palindrome')
        
if __name__ == "__main__":
    main()


"""
    Dictionary with key value pair of letters
    and the number of occurrences of that letter in a string
"""
def create_dict(string):
    result =  {}
    for i in string:
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1
    return result
      
def main():
    my_str = input('Enter a string: ')
    my_dict = create_dict(my_str)
    print("Dictionary: ", my_dict)
    
if __name__ == "__main__":
    main()
    






