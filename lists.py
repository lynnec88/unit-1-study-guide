"""List Practice
Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.
    
    For example::
    
        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    for item in items:
        print(item)
print_list([1, 2, 6, 3, 9])

def long_words(words):
    """Return words in input list that longer than 4 characters.
    
    For example::
    
        >>> long_words(["hello", "a", "b", "hi", "muffin", "muffin"])
        ['hello', 'muffin', 'muffin']
    
    (If there are duplicates, show both --- notice "muffin" appears
    twice in output)
    
    If no words are longer than 4 characters, return an empty list::
    
        >>> long_words(["all", "are", "tiny"])
        []
    """
    #solution 1
    a_words = []
    for word in words:
        if len(word) > 4:
            a_words.append(word)
    return a_words
    
    #soltuion 2 
    # return [word for word in words if len(word) > 4]

long_words(["hello", "a", "b", "hi", "muffin", "muffin"])


def n_long_words(words, n):
    """Return words in list longer than `n` characters.
    
    For example::
    
        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "muffin", "muffin"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'muffin', 'muffin']
        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """
    a_words = []
    for word in words:
        if len(word) > n:
            a_words.append(word)
    return a_words
n_long_words(["I", "like", "apples", "bananas", "you"], 5)


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `min()`!
    
    For example::
    
        >>> smallest_int([-5, 2, -5, 7])
        -5
        >>> smallest_int([3, 7, 2, 8, 4])
        2
    
    If the input list is empty, return `None`::
    
        >>> smallest_int([]) is None
        True
    """

    small_int = None
    for i in numbers:
        if small_int is None or i < small_int:
            small_int = i
    return small_int
smallest_int([-5, 2, -5, 7])



def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `max()`!
    
    For example::
    
        >>> largest_int([-5, 2, -5, 7])
        7
        >>> largest_int([3, 7, 2, 8, 4])
        8
    
    If the input list is empty, return None::
    
        >>> largest_int([]) is None
        True
    """

    big_int = None
    for i in numbers:
        if big_int is None or i > big_int:
            big_int = i
    return big_int

largest_int([-5, 2, -5, 7])


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.
    
    For example::
    
        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]
   
    If any of the numbers are odd, make sure you don't round off
    the half::
   
        >>> halvesies([1, 5])
        [0.5, 2.5]
    """
    average_int = []
    for num in numbers:
        average_int.append(num / 2)
    return average_int

    # return [h / 2 for h in numbers]
halvesies([2, 6, -2])


def word_lengths(words):
    """Return the length of words in the input list.
    
    For example::
    
        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """
    a_words = []
    for word in words:
        a_words.append(len(word))
    return a_words
word_lengths(["hello", "hey", "hello", "spam"])


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.
    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.
    
    For example::
    
        >>> sum_numbers([1, 2, 3, 10])
        16
    
    Any empty list should return the sum of zero::
    
        >>> sum_numbers([])
        0
    """

    sum_int = 0
    for num in numbers:
        sum_int = sum_int + num
    return sum_int
sum_numbers([1, 2, 3, 10])

def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.
    
    For example::
    
        >>> mult_numbers([1, 2, 3])
        6
    
    Obviously, if there is a zero in input, the product is zero::
    
        >>> mult_numbers([10, 20, 0, 50])
        0
    
    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::
    
        >>> mult_numbers([])
        1
    """

    mult_int = 1
    for num in numbers:
        mult_int = mult_int * num
    return mult_int
mult_numbers([1, 2, 3])


def join_strings(words):
    """Return a string of all input strings joined together.
    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.
    
    For example::
    
        >>> join_strings(["spam", "spam", "muffin", "balloonicorn"])
        'spamspammuffinballoonicorn'
    
    For an empty list, you should return an empty string::
    
        >>> join_strings([])
        ''
    """

    strings = ""
    for a_word in words:
        strings = strings + a_word
    return strings
join_strings(["spam", "spam", "muffin", "balloonicorn"])

def average(numbers):
    """Return the average (mean) of the list of numbers given.
    
    For example::
    
        >>> average([2, 4])
        3.0
    
    This should handle cases where the result isn't an integer::
    
        >>> average([2, 12, 3])
        5.666666666666667
    
    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.
    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    total = sum(numbers)
    return total / len(numbers)
average([2, 12, 3])



def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".
    
    For example::
     
        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'
    
    If there's only one thing in the list, it should return just that
    thing, of course::
   
        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """
    strings = words[0]
    for a_word in words[1:]:
        strings = strings + ", " + a_word
    return strings
join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
    


def reverse_list(items):
    """Return the input list, reversed.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> reverse_list([1, 2, 3])
        [3, 2, 1]
        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']
    
    You should do this without changing the original list::
    
        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    return items[::-1]
reverse_list([1, 2, 3])



def reverse_list_in_place(items):
    """Reverse the input list `in place`.
    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]
        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """

    for i in range(len(items) // 2):
        order = items[i]
        items[i] = items[(i + 1) * -1]
        items[(i + 1) * -1] = order

orig = [1, 2, 3]
reverse_list_in_place(orig)
    
    



def duplicates(items):
    """Return list of words from input list which were duplicates.
    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.
   
    For example::
   
        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']
        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]
   
    You should do this without changing the original list::
   
        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']
        >>> orig
        ['apple', 'apple', 'berry']
    """

    product = []
    i = set()

    for item in items:
        if item in i:
            if item not in product:
             product.append(item)
        else:
            i.add(item)
    product.sort()
    return product
orig = ["apple", "apple", "berry"]
duplicates(orig)
orig


def find_letter_indices(words, letter):


    new_wordList = set()
    i = 0
    for letter in range(len(words)):
        if words[i]== letter:
            new_wordList.append()
            return i 
find_letter_indices(['odd', 'dog', 'who'], 'o')        
         



#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")