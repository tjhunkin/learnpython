import re

# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

# Character	Description	Example
# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"world$"
# *	Zero or more occurrences	"aix*"
# +	One or more occurrences	"aix+"
# {}	Exactly the specified number of occurrences	"al{2}"
# |	Either or	"falls|stays"
# ()	Capture and group

# Character	Description	Example
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

# Set	Description
# [arn]	Returns a match where one of the specified characters (a, r, or n) are present
# [a-n]	Returns a match for any lower case character, alphabetically between a and n
# [^arn]	Returns a match for any character EXCEPT a, r, and n
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	Returns a match for any digit between 0 and 9
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+] In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)

# findall
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# no matches
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# search
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# no search result
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# split at whitespace
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# split max
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# replace / substitute
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# only replace x amount
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# match object
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# start and end position
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# string passed
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# group
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

# Note: If there is no match, the value None will be returned, instead of the Match Object.
