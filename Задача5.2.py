import random
lst = [random.randint(0,5) for i in range(random.randint(5,10))]
print(f"Начальный список:\n {lst}")
random.shuffle(lst)
print(f"Перемешанный список:\n{lst}")