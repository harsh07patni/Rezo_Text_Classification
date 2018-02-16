import re

# + - Checks for one or more characters to its left.
print(re.search(r'Co+kie', 'Cooookie').group())

# * - Checks for zero or more characters to its left.
print(re.search(r'Ca*o*kie', 'Cookie').group())


# ? - Checks for exactly zero or one character to its left.
print(re.search(r'Colou?r', 'Color').group())

#check phone number
#{x} - Repeat exactly x number of times.
#{x,} - Repeat at least x times or more.
#{x, y} - Repeat at least x times but no more than y times.
print(re.search(r'\d{9,10}', '0987654321').group())



#Parts of a regular expression pattern bounded by parenthesis() are called groups.
#match emails
email_address = 'Please contact us at: support@rezo.ai'
match = re.search(r'([\w.-]+)@([\w.-]+)', email_address)

if match:
  print(match.group()) # The whole matched text
  print(match.group(1)) # The username (group 1)
  print(match.group(2)) # The host (group 2)



#Greedy vs Non-Greedy Matching
#When a special character matches as much of the search sequence (string) as possible, it is said to be a "Greedy Match".

heading  = r'<h1>TITLE</h1>'
#greedy
print(re.match(r'<.*>', heading).group())
#non-greedy
print(re.match(r'<.*?>', heading).group())

#search() versus match()
#The match() function checks for a match only at the beginning of the string (by default)
# whereas the search() function checks for a match anywhere in the string.


#findall
email_address = "Please contact us at: support@rezo.ai, xyz@rezo.ai"
#'addresses' is a list that stores all the possible match
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', email_address)
for address in addresses:
    print(address)

#sub(pattern, repl, string)
email_address = "Please contact us at: xyz@rezo.ai"
new_email_address = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'support@rezo.ai', email_address)
print(new_email_address)
