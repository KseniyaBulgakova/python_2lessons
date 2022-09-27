n = int(input('Введите число: '))

def fact (n):
  if n == 1:
    return 1
  else:
    return n * fact(n - 1)


list = []
for e in range (1, n + 1):
    list.append(fact(e))

print(f'Набор произведений чисел от 1 до {n}: = {list} ')