n = int(input('Введите число: ')) 

def s(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(s(n))
print(round(sum(s(n))))