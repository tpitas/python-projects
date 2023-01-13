"""
Using chardet.detect to verify the encoding of the file
"""

import chardet
# File can be : ascii, Windows-1252

# Enter the file path
file1 = "/Users/user01/PycharmProjects/test.csv"

raw_data = open(file1, "rb").read()
result = chardet.detect(raw_data)
char_encoded = result['encoding']

print(char_encoded)