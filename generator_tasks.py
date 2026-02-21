
def gensquares(N):
    for i in range(N):
        yield i ** 2

print("1. Квадраты чисел до 5:")
print(list(gensquares(5)))
print("-" * 30)

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

try:
    n_input = int(input("2. Введите n для четных чисел: "))
    print("   Результат:", end=" ")
    print(*even_numbers(n_input), sep=", ")
except ValueError:
    print("   Ошибка: введите целое число")
print("-" * 30)

def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n_div = 100
print(f"3. Числа кратные 3 и 4 (в диапазоне 0-{n_div}):")
print(list(div_by_3_and_4(n_div)))
print("-" * 30)

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

print("4. Квадраты от 3 до 7:")
for val in squares(3, 7):
    print(val)
print("-" * 30)

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

print("5. Обратный отсчет от 5:")
print(list(countdown(5)))