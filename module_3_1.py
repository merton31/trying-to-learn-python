calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)


