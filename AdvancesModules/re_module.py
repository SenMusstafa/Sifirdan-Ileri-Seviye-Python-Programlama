import re

# re module
# result = dir(re)

# re.findall()

text = "Python Course: Your Python Programming Guide | 40 hours"

# result = re.findall("Python", text)
# result = len(result)

# re.split()

# result = re.split(" ", text)

# re.sub()

# result = re.sub(" ", "-", text)
# result = re.sub("\s", "*", text)

# re.search()

# result = re.search("Python", text)
# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()
# result = result.string
# print(result)

# Regular Expressions

'''
    [] - Matches any characters inside the square brackets.
    
    [abc] => a: 1 match
             ac: 2 matches
             Python: No matches

    [a-e] => [abcde]
    [1-5] => [12345]
    [0-39] => [01239]

    [^abc] => Any character except a, b, or c.
    [^0-9] => Any character except a digit.

'''

# result = re.findall("[abc]", text)
# result = re.findall("[0-5]", text)
# result = re.findall("[a-e]", text)
# result = re.findall("[sat]", text) - Only need one 'a' for "saat"
# result = re.findall("[^abc]", text)
# print(result)

"""
    . - Matches any character except a newline character.

    .. => a: No match
          b: 1 match
          abc: 1 match
          abcd: 2 matches

"""

# result = re.findall("...", text)
# result = re.findall("Py..on", text)


"""
    ^ - Matches the start of the string.

    ^a => a: 1 match
          abc: 1 match
          bac: No match
"""

result = re.findall("^a", text)
result = re.findall("^P", text)


"""
    $ - Matches the end of the string.

    a$ => a: 1 match
          lamb: 1 match
          Python: No match
"""

result = re.findall("t$", text)


"""

    * - Matches 0 or more occurrences of the preceding character.
    
    ma*n => mn: 1 match
             man: 1 match
             maaan: 1 match
             main: No match (no 'n' after 'a')
"""

result = re.findall("sa*t", text)


"""

    + - Matches 1 or more occurrences of the preceding character.

    ma+n => mn: No match
             man: 1 match
             maaan: 1 match
             main: No match (no 'n' after 'a')
"""

result = re.findall("sa+t", text)

"""
    ? - Matches 0 or 1 occurrence of the preceding character.

    ma?n => mn: No match
            man: 1 match
            maaan: 1 match
            main: No match (no 'n' after 'a')
"""

result = re.findall("sa?t", text)

"""

    {} - Specifies a specific number of occurrences.
    
    al{2} => 'l' must appear exactly 2 times after 'a'.
    al{2,3} => 'l' must appear between 2 and 3 times after 'a'.
    [0-9]{2,4} => Matches numbers with 2 to 4 digits.
"""

result = re.findall("a{2}", text)
result = re.findall("[0-9]{2}", text)


"""
    | - Specifies alternative options.

    a | b => a or b

    cde => No match
    ade => 1 match
    acdbea => 3 matches
"""

"""

    () - Groups for expression.

    (a|b|c)xz => Either 'a', 'b', or 'c' followed by 'xz'.
"""

"""

    \ - Escapes special characters to match them literally.
        \$a => Matches '$' followed by 'a'. Not interpreted as a regex.
    
    \A - Matches the start of the string.
        \Athe => Is 'the' at the start of the string?
    
    \Z - Matches the end of the string.
        the\Z => Is 'the' at the end of the string?
    
    \b - Matches a word boundary.
        \bthe => Is 'the' at the beginning of a word?
        the\b => Is 'the' at the end of a word?
    
    \B - Matches a non-word boundary.
        \Bthe => Is 'the' not at the beginning of a word?
        the\B => Is 'the' not at the end of a word?
    
    \d - Same as [0-9], matches digits.
        \d => 12abc34
    
    \D - Same as [^0-9], matches non-digits.
        \D => 1ab44_50
    
    \s - Matches whitespace characters, such as space or tab.
    \S - Matches non-whitespace characters.
    \w - Matches alphanumeric characters and underscore.
    \W - Matches non-alphanumeric characters.
"""

print(result)
