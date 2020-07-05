```python
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# Returns True if input in a phone number, else returns False.
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# Searches through a string for phone numbers.
def num_search(string):
    for i in range(len(string)):
        chunk = string[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done')

print(message + '\n')
num_search(message)
```

### re.compile(), .search(), .group(), .groups()


```python
import re

message = 'My number is 415-555-4242.'
message_1 = 'My phone number is (415)-555-4242.'

# Finds phone number in message

print('Regex: (\d\d\d)-(\d\d\d-\d\d\d\d)')
regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = regex.search(message)
print(mo.group() + '\n')

print('Regex: (\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
# Finds phone number in message_1.
regex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = regex.search(message_1)
print(mo.group())
```

### | (pipe)


```python
message = 'My number is 415-555-4242.'
message_1 = 'My phone number is 415 555 4242.'

# Finds phone number in message and message_1. Uses pipe to indicate a - or ' '.
print('Regex: ((\d\d\d)(-|\s)\d\d\d(-|\s)\d\d\d\d)')
for item in [message, message_1]:
    regex = re.compile(r'((\d\d\d)(-|\s)\d\d\d(-|\s)\d\d\d\d)')
    mo = regex.search(item)
    print(mo.group())
```

### ? (optional)


```python
message = 'My number is 415-555-4242.'
message_1 = 'My phone number is 415 555 4242.'
message_2 = 'My phone number is 4155554242.'

# Finds phone number in message, message_1, and message_2. Uses ? to indicate - or ' ' is optional.
print('Regex: ((\d\d\d)(-|\s)?\d\d\d(-|\s)?\d\d\d\d)')
for item in [message, message_1, message_2]:
    regex = re.compile(r'((\d\d\d)(-|\s)?\d\d\d(-|\s)?\d\d\d\d)')
    mo = regex.search(item)
    print(mo.group())
```

### * (star), + (plus)


```python
message = 'My number is 415-555-4242.'
message_1 = 'My phone number is (415)-555-4242.'
message_2 = 'My phone number is 4155554242.'

# Finds phone number using \d*.
print('This is the result of using \d* in place of \d\d\d or \d\d\d\d:')
for item in [message, message_1, message_2]:
    regex = re.compile(r'((\d*)(-|\s)?\d*(-|\s)?\d*)')
    mo = regex.search(item)
    print(mo.group())

# Finds phone number using \d+.
print('This is the result of using \d+ in place of \d\d\d or \d\d\d\d:')
for item in [message, message_1, message_2]:
    regex = re.compile(r'((\d+)(-|\s)?\d+(-|\s)?\d+)')
    mo = regex.search(item)
    print(mo.group())
```

### {} (brace)


```python
message = 'My number is 415-555-4242.'
message_1 = 'My phone number is 415 555 4242.'
message_2 = 'My phone number is 4155554242.'

# Finds phone number using \d{3} or \d{4}
print('This is the result of using \d{3} for \d\d\d and \d{4} for \d\d\d\d:')
for item in [message, message_1, message_2]:
    regex = re.compile(r'((\d{3})(-|\s)?\d{3}(-|\s)?\d{4})')
    mo = regex.search(item)
    print(mo.group())
```

### .findall() and greedy matching

https://pythex.org/


```python
message = 'My number is 415-555-4242. My phone number is 415 555 4242. My phone number is 4155554242.'
message_1 = 'hahahahaha'

# Finds phone number using search(). This only returns the first number found.
print('This is what search() returns:')
regex = re.compile(r'((\d{3})(-|\s)?\d{3}(-|\s)?\d{4})')
mo = regex.search(message)
print(mo.group())
print('\n')

# Finds phone number using findall(). This only returns a list containing tuples of all groups.
print('This is what findall() returns:')
regex = re.compile(r'((\d{3})(-|\s)?\d{3}(-|\s)?\d{4})')
mo = regex.findall(message)
print(mo)
print('\n')
```


```python
print('This is the message: ' + message_1 + '\n')
# Greedy
print('Regex: (ha){3,5}')
regex = re.compile(r'(ha){3,5}')
mo = regex.search(message_1)
print(mo.group())

# Not greedy
print('Regex: (ha){3,5}?')
regex = re.compile(r'(ha){3,5}?')
mo = regex.search(message_1)
print(mo.group())
```

### /d, /D, /w, /W, /s, /S


```python
# \d = digit
# \w = letter character, cap or lower, _
# \s = ' '
# \D = not digit
# \W = not letter
# \S = not space
```


```python
message = '''This is the shopping list for Christmas last year: 12 drummers, 11 pipers, 10 lords, 9 ladies, 
8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'''

# Returns a list of all gifts from last year Christmas.
print('This is the message: ' + message + '\n')
print('Regex: \d+\s\w+')
regex = re.compile(r'\d+\s\w+')
mo = regex.findall(message)
print(mo)
```

### [ ] (brace) and [^ ] (not)


```python
message = '''Eunoia is the shortest word in English to contain all five vowels, 
and the word quite literally means beautiful thinking.'''

print('This is the message:')
print(message)
print('\n')

# Returns a list of all vowels in message.
print('Regex: [AEIOUaeiou]')
regex = re.compile(r'[AEIOUaeiou]')
mo = regex.findall(message)
print(mo)

# Returns a list of all consonants in message. Uses 
print('Regex: [^AEIOUaeiou\s.]): ')
regex = re.compile(r'[^AEIOUaeiou\s.]')
mo = regex.findall(message)
print(mo)
```

### ^ (caret) and $ (dollar sign)


```python
message = '''Eunoia is the shortest word in English to contain all five vowels, 
and the word quite literally means beautiful thinking.'''

print('This is the message: \n' + message + '\n')

print('Regex: ^Eunoia is ')
regex = re.compile(r'^Eunoia is')
mo = regex.findall(message)
print(mo)

print('Regex: Eunoia is$')
regex = re.compile(r'Eunoia$')
mo = regex.findall(message)
print(mo)

print('Regex: ^beautiful thinking.')
regex = re.compile(r'^beautiful thinking.')
mo = regex.findall(message)
print(mo)

print('Regex: beautiful thinking.$')
regex = re.compile(r'beautiful thinking.$')
mo = regex.findall(message)
print(mo)
```

### . (wildcard)


```python
message = 'The cat in the hat eats on the flat mat.'

# Returns all words with -at.
print('Regex: .at')
regex = re.compile(r'(.at)')
mo = regex.findall(message)
print(mo)

print('\n')

# Returns all words with -at.
print('Or:\nRegex: \w*at')
regex = re.compile(r'\w*at')
mo = regex.findall(message)
print(mo)
```

### re.DOTALL, re.I, re.VERBOSE


```python
message = 'The apparition of these faces in the crowd: \nPetals on a wet, black bough. \n-Ezra Pound'

print('This is the message: ' + '\n' + message + '\n')

# Finds everything, stoping at any new lines.
print('Regex: .*')
regex = re.compile(r'(.*)')
mo = regex.search(message)
print(mo.group())

print('\n')

# Finds everything.
print('Regex: .* with re.DOTALL')
regex = re.compile(r'(.*)', re.DOTALL)
mo = regex.search(message)
print(mo.group())
```


```python
favorite_pokemon = "'Marshtomp', 'MarshTomp', 'MARSHTOMP', 'marshtomp'"

print('This is the message: ' + favorite_pokemon + '\n')

# Finds marshtomp in any combination of cases.
print('Regex: marshtomp with re.I')
regex = re.compile(r'marshtomp', re.I)
mo = regex.findall(favorite_pokemon)
print(mo)
```


```python
message = '''415-555-4242, 415 555 4242, 4155554242, (415)-555-4242, 415.555.4242, (415) 555-4242, 555-4242, +13 415 555 4242'''

book = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)


regex = re.compile(r'''
    (\s?(\+\d+)? # international
    (-|\s|\.)? # international separator
    (\(?\d{3}\)?)? # area code (optional)
    (-|\s|\.)? # separator
    \d{3} # next 3 digits
    (-|\s|\.)? # separator
    \d{4} # last four digits
    )''', re.VERBOSE)

def result_filter(lst):
    return [item[0] for item in lst]

mo = book.findall(message)
print('This is the results of using the regex from the book: ')
print(mo)
print('Filtered:')
print(result_filter(mo))
print('\n')
result = regex.findall(message)
print('This is the results of using the regex we created: ')
print(result)
print('Filtered:')
print(result_filter(result))
```

### .sub()


```python
message = 'Agent Romanov gave the secret documents to Agent Barton.'

# Replace all 'Agent + name' with CENSORED
regex = re.compile(r'Agent\s\w+')
mo = regex.sub('CENSORED', message)
print(mo)
```


```python

```
