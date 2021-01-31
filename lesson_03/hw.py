num = int(input('Pleas enter a number: '))

n1 = num % 10
n2 = num // 10 % 10
n3 = num // 100

num1 = n1 * 100 + n2 * 10 + n3
print(num1)
