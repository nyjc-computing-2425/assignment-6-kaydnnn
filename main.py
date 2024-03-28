from datetime import datetime
import time


# Part 1
def clock(n):
    """
    shows the time and updates it every second for n seconds

    Parameters
    ---------
    n : int
        number of seconds to update

    Returns
    ---------
    string
        string to display the time per n seconds
    """
    for second in range(n):
        now = str(datetime.now()).split()
        now = (now[1].split("."))[0]
        print(now, end = "\r")
        time.sleep(1)

# Part 2
def lcm(a, b):
    """
    finds the lowest common multiple for a and b

    Parameters
    ---------
    a : int
        first number
    b : int
        second number

    Returns
    ---------
    integer
        an integer for lowest common multiple
    """
    lcm = 0
    not_found = True
    b_original = b
    a_original = a
    while not_found is True:
        if(a == b):
            lcm = a
            not_found = False
        else:
            if a > b:
                b += b_original
            if b > a:
                a += a_original

    return lcm


# Part 3
def gcf(a, b):
    """
    finds the greatest common factor for a and b

    Parameters
    ---------
    a : int
        first number
    b : int
        second number

    Returns
    ---------
    integer
        an integer for greatest common factor
    """
    gcf = 0
    found = False
    while found == False:
        if(b == 0):
            gcf = a
            found = True
        else:
            r = a % b
            a = b
            b = r

    return gcf

