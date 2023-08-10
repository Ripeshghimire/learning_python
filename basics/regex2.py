import re
with open(r'files/regexfiles/RegexSample.txt','r') as file:
    fileContent = file.read()
    # print(fileContent)

#extract Emergency number
pattern = re.compile(r'\b10[0124]\b')
matches = pattern.finditer(fileContent)
for match in matches:
    print(f'The emergency no are {match.group()}')
#Pan number
# pattern = re.compile(r'\b[6|1|3]\d{8}\b')
# matches = pattern.finditer(fileContent)
# for match in matches:
#     print(f'The pan numbers are {match.group()}')
#+ numbers
# pattern = re.compile(r'[+]\d+')
# matches = pattern.finditer(fileContent)
# for match in matches:
#     print(f'The numbers having + sign {match.group()}')