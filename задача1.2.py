print('Введите число')
N = float (input())
def sum(N):
    sum = 0
    for i in str(N):
        if i != ".":
            sum += int(i)
    return sum
print(f"Сумма цифр равна = {sum(N)}")