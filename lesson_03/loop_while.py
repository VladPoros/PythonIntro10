"""
while condition:
    operator1

operatorN
"""

i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=', ')
    i += 1
else:
    print('else')

print()
# break
# continue

i = 10
while i < 50:
    i += 1
    if i % 2:
        continue

    print(i, end=', ')


