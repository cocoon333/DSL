print '''
String Functions:

    capitalize, center, count, decode, encode, endswith, expandtabs, find, format, index, isalnum, isalpha, isdigit, islower, isspace, istitile, isupper, join, ljust, lower, lstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
-----------------------------------------------------------------------------------------
str.capitalize()
Capitalizes the first letter of str.

>>> 'abc'.capitalize()
'Abc'
-----------------------------------------------------------------------------------------
str.center(width)

returns a str that has a len at least as big as the width. If the len of the str is less than width\
, then a serie of spaces is added to the str to match the len with width. The orginal str stays in \
the middle. The string will not be shortened.

>>> 'abc'.center(5)
' abc '
-----------------------------------------------------------------------------------------
str.count(char)

returns how many char is in str

>>> 'aaabbbccc'.count('a')
3
-----------------------------------------------------------------------------------------
str.endswith(char)

returns True if the str endswith char, otherwise is false

>>> 'aaa'.endswith('a')
True
>>> 'bbb'.endswith('a')
False
-----------------------------------------------------------------------------------------
str.expandtabs()

Transforms tabs depending on position

>>>'    a   b   c'.expandtabs()
'    a   b   c'
>>> '   a       '.expandtabs()
'        a       '
-----------------------------------------------------------------------------------------
str.find(sub)

Find the index of the first place where the sub is found in str. If sub is not in str, then return -1
-----------------------------------------------------------------------------------------
str.format(*args, **kwargs)
Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.

>>>
>>> "The sum of 1 + 2 is {0}".format(1+2)
'The sum of 1 + 2 is 3'
-----------------------------------------------------------------------------------------
str.index(sub[, start[, end]])
Like find(), but raise ValueError when the substring is not found.
>>> 'abc'.index('a')
0
------------------------------------------------------------------------------------------
str.isalnum()
Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.

For 8-bit strings, this method is locale-dependent.
-----------------------------------------------------------------------------------------
str.isalpha()
Return true if all characters in the string are alphabetic and there is at least one character, false otherwise.

For 8-bit strings, this method is locale-dependent.
---------------------------------------------------------------------------------------
str.isdigit()
Return true if all characters in the string are digits and there is at least one character, false otherwise.

For 8-bit strings, this method is locale-dependent.
-------------------------------------------------------------------------------------
str.islower()
Return true if all cased characters [4] in the string are lowercase and there is at least one cased character, false otherwise.

For 8-bit strings, this method is locale-dependent.
-----------------------------------------------------------------------------------------
str.isspace()
Return true if there are only whitespace characters in the string and there is at least one character, false otherwise.

For 8-bit strings, this method is locale-dependent.
----------------------------------------------------------------------------------------
str.istitle()
Return true if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return false otherwise.

For 8-bit strings, this method is locale-dependent.
------------------------------------------------------------------------------------------------
str.isupper()
Return true if all cased characters [4] in the string are uppercase and there is at least one cased character, false otherwise.
-----------------------------------------------------------------------------------
str.join(iterable)
Return a string which is the concatenation of the strings in the iterable iterable. The separator between elements is the string providing this method.
-----------------------------------------------------------------------------------------
str.ljust(width[, fillchar])
Return the string left justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than or equal to len(s).

-------------------------------------------------------------------------------------
str.lower()
Return a copy of the string with all the cased characters [4] converted to lowercase.
-----------------------------------------------------------------------------------
str.lstrip([chars])
Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are stripped:

>>>
>>> '   spacious   '.lstrip()
'spacious   '
>>> 'www.example.com'.lstrip('cmowz.')
'example.com'
----------------------------------------------------------------------------------------------
str.partition(sep)
Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.

------------------------------------------------------------------------------------
str.replace(old, new[, count])
Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
--------------------------------------------------------------------------------------
str.rfind(sub[, start[, end]])
Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
-----------------------------------------------------------------------------------------
str.rindex(sub[, start[, end]])
Like rfind() but raises ValueError when the substring sub is not found.
-----------------------------------------------------------------------------------------
str.rjust(width[, fillchar])
Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than or equal to len(s).

------------------------------------------------------------------------------------
str.rpartition(sep)
Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself.
-----------------------------------------------------------------------------------
str.rsplit([sep[, maxsplit]])
Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done, the rightmost ones. If sep is not specified or None, any whitespace string is a separator. Except for splitting from the right, rsplit() behaves like split() which is described in detail below.
-------------------------------------------------------------------------------------------------
str.rstrip([chars])
Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:

>>>
>>> '   spacious   '.rstrip()
'   spacious'
>>> 'mississippi'.rstrip('ipz')
'mississ'
------------------------------------------------------------------------------
str.split([sep[, maxsplit]])
Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).

If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns [''].

If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].

For example, ' 1  2   3  '.split() returns ['1', '2', '3'], and '  1  2   3  '.split(None, 1) returns ['1', '2   3  '].
-----------------------------------------------------------------------------
str.splitlines([keepends])
Return a list of the lines in the string, breaking at line boundaries. This method uses the universal newlines approach to splitting lines. Line breaks are not included in the resulting list unless keepends is given and true.

For example, 'ab c\n\nde fg\rkl\r\n'.splitlines() returns ['ab c', '', 'de fg', 'kl'], while the same call with splitlines(True) returns ['ab c\n', '\n', 'de fg\r', 'kl\r\n'].

----------------------------------------------------------------------------
str.startswith(prefix[, start[, end]])
Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.

-------------------------------------------------------------------------
str.strip([chars])
Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:

>>>
>>> '   spacious   '.strip()
'spacious'
>>> 'www.example.com'.strip('cmowz.')
'example'
------------------------------------------------------------------------
str.swapcase()
Return a copy of the string with uppercase characters converted to lowercase and vice versa.
------------------------------------------------------------------------
str.title()
Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.

>>>
>>> "they're bill's friends from the UK".title()
"They'Re Bill'S Friends From The Uk"

>>>
>>> import re
>>> def titlecase(s):
...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0)[0].upper() +
...                              mo.group(0)[1:].lower(),
...                   s)
...
>>> titlecase("they're bill's friends.")
"They're Bill's Friends."
--------------------------------------------------------------------------
str.translate(table[, deletechars])
Return a copy of the string where all characters occurring in the optional argument deletechars are removed, and the remaining characters have been mapped through the given translation table, which must be a string of length 256.

>>>
>>> 'read this short text'.translate(None, 'aeiou')
'rd ths shrt txt'
---------------------------------------------------------------------------
str.upper()
Return str with all characters uppercased
---------------------------------------------------------------------------
str.zfill(width)
Return the numeric string left filled with zeros in a string of length width. A sign prefix is handled correctly. The original string is returned if width is less than or equal to len(s)
'''
