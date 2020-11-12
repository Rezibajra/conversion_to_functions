"""
    Choose list of your choice.
    Sum of elements of a list.
    Cannot use sum() function.
"""
def find_sum(my_list):
    sum = 0
    for element in range(0, len(my_list)):
        sum = sum + my_list[element]
    return sum
    
def main():
    """Creating a list"""
    my_list = [6, 9, 7, 5, 4]
    print(my_list)
    sum = find_sum(my_list)
    print('Sum of elements in list: ', sum)
    
if __name__ ==  "__main__":
    main()


"""
    Returns a list containing common elements
    from two lists.
"""
def common_elements(l1, l2):
    """Convert list to set to perform intersection"""
    set_a = set(l1)
    set_b = set(l2)
    common = list(set_a.intersection(set_b))
    return common

def main():
    list1 = [1, 1, 3, 5, 7, 9, 9]
    list2 = [2, 1, 6, 9, 2, 1, 3, 5]
    print("List1 :", list1)
    print("List2 :", list2)
    common = common_elements(list1, list2)
    print("Common elements :", common)
    
if __name__ == "__main__":
    main()


"""
    Ask input from user.
    Input must be string.
    Display string along with its length
    Cannot use len()
"""
def calc_length(input_string):
    count = 0
    for s in input_string:
        count = count + 1
    return count
    
def main():
    input_string = str(input('Enter a string: '))
    print('String: ', input_string)
    length = calc_length(input_string)
    print("Length of {}:".format(input_string), length)
       
if __name__ == "__main__":
    main()



