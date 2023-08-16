import re 
# 1) Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
# strd= "Ripesh123 is a good boy and is very humble and is a data scientist"
# pattern = re.compile(r'^[A-Za-z0-9]+$')
# matches = pattern.finditer(strd)
# for match in matches:
#     print(match.group())

# 2) Write a Python program that matches a string that has an a followed by zero or more c's
# string = 'Hey account is account failed'
# pattern = re.compile(r'\b(ac*\w+)')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match.group())

# 3) Write a Python program that matches a string that has an a followed by one or more c's 
# string = 'Hey account is account failed'
# pattern = re.compile(r'\b(ac+\w+)')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match.group())
# 4) Write a Python program that matches a string that has an a followed by zero or one 'c'
# string = 'Hey account is account failed'
# pattern = re.compile(r'\b(ac?\w+)')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match.group())
# 5) Write a Python program that matches a string that has an a followed by three 'b'
# string = 'abbbbb acccc adddd afff addddd abbb dabbb'
# pattern = re.compile(r'\b(ab{3}\b)')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 6) Write a Python program that matches a string that has an a followed by two to three 'b'. 
# string = 'abbb acccc adddd afff addddd abbb dabbb abb'
# pattern = re.compile(r'\bab{2,3}\b')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 7) Write a Python program to find sequences of lowercase letters joined with a underscore.
# string = 'hello ripesh_ghimire how are you are you fine_hello'
# pattern = re.compile(r'[a-z]+_[a-z]+')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 8) Write a Python program to find the sequences of one upper case letter followed by lower case letters.
# string = 'Hello i am Ripesh Ghimire'
# pattern = re.compile(r'[A-Z][a-z]+')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 9) Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# string = 'afasb adfasj afdafasfb asdfaja adfadb'
# pattern = re.compile(r'\ba\w*b\b')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 10) Write a Python program that matches a word at the beginning of a string.
# string = 'Start of the string and end of the String'
# pattern = re.compile(r'^Start')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 11) Write a Python program that matches a word at the end of string, with optional punctuation.

# 12) Write a Python program that matches a word containing 'z'
# string = 'zebra is a animal tha lives in the grass.'
# pattern = re.compile(r'\bz[a-z]+')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 13) Write a Python program that matches a word containing 'z', not at the start or end of the word.
# string = 'the quick brown fox jumped over the lazy dog zebra'
# pattern = re.compile(r'(\b[a-y]+[z][a-y])\b')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)

# 14) Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores
# string = 'The quick brown fox jumped over the lazy dog zebra 1233'
# pattern = re.compile(r'\b\w+')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 15) Write a Python program where a string will start with a specific number. 
# string = '123 the quick brown fox jumped over the lazy dog zebra'
# pattern = re.compile(r'\d\d\d+\w*')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 16) Write a Python program to remove leading zeros from an IP address
# string = '''001.002.003.004
# 00.01.02.03
# 00.100.200.300'''
# pattern = re.compile(r'00\b\w+')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 18) Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

# 19) Write a Python program to search some literals strings in a string. Go to the editor Sample text : 'The quick brown fox jumps over the lazy dog.' Searched words : 'fox', 'dog', 'horse'

# 20) Write a Python program to extract year, month and date from a an url.
# 21) Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
#  22) Write a Python program to separate and print the numbers of a given string.
# string = 'my age is 12. i live in kathmandu street-7'
# pattern = re.compile(r'\d+')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 23) Write a Python program to find all words starting with 'a' or 'e' in a given string.
# string = 'aeroplane eagle rider this girl is on fire aigh'
# pattern = re.compile(r'\b(a|e)[a-z]+\b')
# matches = pattern.finditer(string)
# for match in matches:
#     print(match)
# 24) Write a Python program to separate and print the numbers and their position of a given string.
