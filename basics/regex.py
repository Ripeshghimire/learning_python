import re 
text = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

logisparktech.com

321-555-4321
123.444.1234
456*697*5566
800-123-234
900-234-123
700-234-121


192.168.1.91

Mr Rohit
Mr. Raunak
Ms. Anushka
Mrs. Nisha
Mr. T
Mr..P
Mr. p

cat
mat
pat
bat
'''
sentence = "Start a sentence and bring it to and end Start"
pattern = re.compile(r'def')
#matches all character except new line 
pattern = re.compile(r'.')
#use backslash to match only  . character
pattern  =re.compile(r'\.')
pattern = re.compile(r'logisparktech\.com')
#word boundary
pattern = re.compile(r'\bHa')
#third ha 
pattern = re.compile(r'\BHa\b')
#second ha 
pattern = re.compile(r'\bHa\B')
#start and end of string 
pattern = re.compile(r'^Start')
#matching the end of the string 
pattern = re.compile(r'Start$')

#Matching phone numbers
pattern = re.compile(r'\d\d\d\.\d\d\d\.\d\d\d\d')
#Matching two pattern
pattern = re.compile(r'\d\d\d[*.-]\d\d\d[*.-]\d\d\d\d')
#matching this 
pattern = re.compile(r'[89]00[*.-]\d\d\d[*.-]\d\d\d')
#matches a range of character 
pattern = re.compile(r'[a-zA-z0-9]')
# not range matches
pattern = re.compile(r'[^a-zA-Z]')
#match the words
pattern = re.compile(r'[a-z]at')
pattern = re.compile(r'[^b]at')
# 321-555-4321
# 123.444.1234
# 456*697*5566
# 800-123-234
# 900-234-123
# 700-234-124
pattern = re.compile(r'\d{3}[*.-]\d{3}[*.-]\d{4}')
pattern = re.compile(r'\d{3}[*.-]\d{3}[*.-]\d{3,4}')
#
pattern = re.compile(r'Mr\.')
pattern = re.compile(r'Mr\.?')
pattern = re.compile(r'Mr\.?\s[A-Za-z]+')
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# pattern = re.compile(r'Mr\.?\s\w\b')
pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*')
matches = pattern.finditer(text)
for match in matches:
    print(match)

