"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".
def hello_world():
    print("Hello World")

# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.
def say_hi(name):
    print(f'Hi {name}')

# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.
def print_product(int_1, int_2):
    print(int_1 * int_2)

# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times
def repeat_string(str, intigerr):
    l=''
    for i in range(0,intigerr):
        l += str
    print(l)
        


# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".
def print_sign(num):
    if num > 0:
        print("Higher than 0")
    elif num == 0:
        print("Zero")
    else:
        print("Lower than 0")



# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.
def is_divisible_by_three(num):
    if  num%3 == 0:
        return True
    else:
        return False


# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.
def num_spaces(sent):
    total = 0
    for i in sent:
        if i == " ":
            total+=1
    return total

# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.
def total_meal_price(meal_price,tip = .15):
    tips = meal_price *tip
    total = meal_price + tips
    return total
# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.
def sign_and_parity(num):
    array = []
    if num > 0:
        array.append("Positive")
    else:
        array.append("Negative")
    if num%2 == 0:
        array.append("Even")
    else:
        array.append("Odd")
    return array


###############################################################################

# PART TWO

# 1. Write a function called full_title that takes a name and a job title as
#    parameters, making it so the job title defaults to "Engineer" if a job
#    title is not passed in. Return the person's title and name in one string.
def full_title(name, job_title="Engineer"):
    
    return f"{job_title} {name}"

# 2. Write a function called write_letter that, given a recipient name & job
#    title and a sender name, prints the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.

def write_letter(name, title, sender):
    """Print filled in form letter"""

    receiver = full_title(name, title)

    print(f"Dear {receiver}, I think you are amazing! Sincerely, {sender}")







###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
