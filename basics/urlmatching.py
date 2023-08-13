import re
url = '''
https://www.google.com
http://logisparktech.com
https://logisparktech.com
https://www.ioost.gov'''
pattern = re.compile(r'https?://((w{3}\.))?[a-z0-9]+\.(com|gov)')
pattern = re.compile(r'https?://(w{3}\.)?(\w+)(\.\w+)')
matches = pattern.finditer(url)
subbed_urls = pattern.sub(r'\2\3',url)
print(subbed_urls)
for match in matches:
    print(match)

