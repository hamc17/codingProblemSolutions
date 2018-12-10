#!/usr/bin/python
from collections import deque
"""
Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular
expression.
"""

DOT = "."
ASTERISK = "*"


def regex(regex_string, check_string):
    """This function performs basic regex on an inputted string to check.
    Only accepts * and . as regex parameters. Evaluates all other characters
    exactly based on position in string compared to regex string.

    Arguments:
        regex_string {string} -- The regex string to compare check string to.
        check_string {string} -- The string to check against the regex string.

    Returns:
        bool -- True if match, else False
    """

    # chunks is the substrings containing chars or dot/asterisk
    chunks = deque(get_chunks(regex_string))
    check_string_deque = deque(list(check_string))
    while chunks:
        chunk = chunks.popleft()
        # if dot, need to consume 1 char from check string
        if chunk == DOT:
            try:
                check_string_deque.popleft()
            except IndexError:
                return False
        # if asterisk, need to consume 0 or more - sliding window
        elif chunk == ASTERISK:
            if chunks:
                window = chunks.popleft()
                while window == "*":
                    try:
                        window = chunks.popleft()
                    except IndexError:
                        return True
                if window == ".":
                    try:
                        check_string_deque.popleft()
                    except IndexError:
                        return False
                else:
                    if not check_sliding_window(window, check_string_deque):
                        return False
        else:
            check_chunk = []
            while len(check_chunk) != len(chunk):
                try:
                    check_chunk.append(check_string_deque.popleft())
                except IndexError:
                    return False
            if not check_chunk == chunk:
                return False
    if check_string_deque:
        return False
    return True


def check_sliding_window(window, check_string_deque):
    """Takes in a window of characters and tries to find a matching window in
    the provided deque of characters.

    Arguments:
        window {list} -- The window of characters to find.
        check_string_deque {deque} -- The deque of characters to find the
        window in.

    Returns:
        bool -- True if found, else False
    """

    check_window = []
    while True:
        if len(check_window) != len(window):
            try:
                check_window.append(check_string_deque.popleft())
            except IndexError:
                return False
        else:
            if window == check_window:
                return True
            else:
                check_window = check_window[1:]


def get_chunks(regex_string):
    """Breaks the regex string into regex chunks, namely letters,
    dots and asterisks.

    Arguments:
        regex_string {string} -- The regex string

    Returns:
        list -- The list of regex chunks
    """

    chunks = []
    letters = []
    for c in regex_string:
        print c, DOT, ASTERISK
        print c == DOT
        if c != DOT and c != ASTERISK:
            letters.append(c)
        else:
            print "not . *"
            if letters:
                chunks.append(letters)
                letters = []
            chunks.append(c)
    if letters:
        chunks.append(letters)
    return chunks
