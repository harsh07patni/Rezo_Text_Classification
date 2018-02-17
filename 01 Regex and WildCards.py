import re

# r is a raw string literal

pattern = r"Cookie"
sequence = "Cookie"
if re.match(pattern, sequence):
  print("Match!")
else: print("Not a match!")


# . A period. Matches any single character
print(re.search(r'Co.k.e', 'Cookie').group())

# Lowercase w. Matches any single letter, digit or underscore.
print(re.search(r'Co\wk\we', 'Cookie').group())

#Uppercase W. Matches any character not part of \w (lowercase w)
print(re.search(r'C\Wke', 'C@ke is best').group())

#Lowercase s. Matches a single whitespace character like: space, newline, tab, return
print(re.search(r'Eat\scake', 'Eat cake').group())

#Uppercase s. Matches any character not part of \s (lowercase s)
print(re.search(r'Cook\Se', 'Cookie').group())

# Lowercase d. Matches decimal digit 0-9
print(re.search(r'c\d\dkie', 'c00kie').group())

# Caret. Matches a pattern at the start of the string.
print(re.search(r'^Eat', 'Eat cake').group())

# $ Matches a pattern at the end of string.
print(re.search(r'cake$', 'Eat cake').group())

# [abc] - Matches a or b or c.
#[a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9).
print(re.search(r'Number: [0-6]', 'Number: 5').group())

# Matches any character except 5
print(re.search(r'Number: [^5]', 'Number: 0').group())

