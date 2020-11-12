"""
    Function to convert Fahrenheit to Celsius
"""
def convert_temp(temp):
    """Converts and prints temperature in celsius"""
    celsius = (temp - 32) * 5/9
    print('Temperature in celsius: ', celsius)
    
def main():
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    convert_temp(fahrenheit)
    
if __name__ == "__main__":
    main()


"""
    Convert seconds to minutes and seconds
"""
def convert_time(time):
   """Converts and prints seconds in minutes and seconds""" 
    minutes = time // 60
    time %= 60
    seconds = time
    print("m:s-> %d:%d" % (minutes, seconds))

def main():
    time_seconds = float(input("Input time in seconds: "))
    convert_time(time_seconds)
    
if __name__ == "__main__":
    main()


"""
    Print length of the list.
    Print the first and fourth element of the list.
"""

#Globals
lst = []
n = int(input("Enter number of elements : "))

def create_list():
    for i in range(0, n): 
        element = int(input()) 
        lst.append(element)
    return lst

def first_element():
    if(n<1):
        print("No sufficient numbers to display the first element")
    else:
        print("First element is:", lst[0])

def fourth_element():
    if(n<4):
        print("No sufficient numbers to display the fourth element")
    else:
        print("Fourth element is:", lst[3])
    
def main():
    lst = create_list()
    print(lst)
    """Display length of list"""
    print('Length: ', len(lst))
    first_element()
    fourth_element()
    
if __name__ == "__main__":
    main()


"""
    List methods pop,insert and remove
"""

def list_methods(lst):
    """Pop"""
    print("Popping third element:", lst.pop(2))
    print("After popping:", lst)
    """Insert"""
    lst.insert(2, 3.1)
    print("After inserting at 2: ", lst)
    """Remove"""
    lst.remove(4.3)
    print("After removing 4.3: ", lst)

def main():
    my_lst = [1.1, 2.3, 3.4, 4.3]
    print(my_lst)
    list_methods(my_lst)
                 
if __name__ == "__main__":
    main()









