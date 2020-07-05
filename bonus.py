# Takes a list, and returns a list with all non-numerals removed.

def num_only(lst):
    processed = []
    for item in lst:
        num = []
        for i in range(len(item)):
            if item[i].isdecimal():
                num.append(item[i])
        processed.append(''.join(num))
    return processed

# Test sample
# message = ['415-555-4242', ' 415 555 4242', ' 4155554242', ' (415)-555-4242', ' 415.555.4242', ' (415) 555-4242', ' 555-4242', ' +13 415 555 4242']
# print(num_only(message))
