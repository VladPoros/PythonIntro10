"""
for val in iterable_obj:
    operator1

operatorN

for _ in iterable_obj:
    operator1

"""

s = 'Process finished with exit code 0'
for symbol in s:
    print(symbol, end=', ')
print()

# range(start, stop, step)
for i in range(10, 30, 2):
    print(i, end=', ')
print()

for i in range(30):
    print(i, end=', ')
print()

for idx in range(0, len(s), 2):
    print(s[idx], end=', ')
print()



