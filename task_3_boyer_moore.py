
import timeit

def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    # Створюємо таблицю зсувів для патерну (підрядка)
    shift_table = build_shift_table(pattern)
    i = 0  # Ініціалізуємо початковий індекс для основного тексту

    # Проходимо по основному тексту, порівнюючи з підрядком
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Починаємо з кінця підрядка

        # Порівнюємо символи від кінця підрядка до його початку
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Зсуваємось до початку підрядка

        # Якщо весь підрядок збігається, повертаємо його позицію в тексті
        if j < 0:
            return i  # Підрядок знайдено

        # Зсуваємо індекс i на основі таблиці зсувів
        # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # Якщо підрядок не знайдено, повертаємо -1
    return -1
with open('стаття 1.txt', 'r', encoding='windows-1251') as file:
    article1 = file.read()

with open('стаття 2.txt', 'r', encoding='windows-1251') as file:
    article2 = file.read()

# Вимірюємо час виконання алгоритму для статті 1
start_time = timeit.default_timer()
real_1 = boyer_moore_search(article1, "звичайно являють собою послідовність кроків")
time_real_1 = timeit.default_timer() - start_time

start_time = timeit.default_timer()
unreal_1 = boyer_moore_search(article1, "Якби ви вчилися так, як треба, то й мудрість би була своя")
time_unreal_1 = timeit.default_timer() - start_time

# Вимірюємо час виконання алгоритму для статті 2
start_time = timeit.default_timer()
real_2 = boyer_moore_search(article2, "Графові моделі СУБД надають")
time_real_2 = timeit.default_timer() - start_time

start_time = timeit.default_timer()
unreal_2 = boyer_moore_search(article2, "Вогонь запеклих не пече")
time_unreal_2 = timeit.default_timer() - start_time

# Виведення результатів
print("Час виконання для статті 1 (існуючий підрядок):", time_real_1)
print("Час виконання для статті 1 (вигаданий підрядок):", time_unreal_1)
print("Час виконання для статті 2 (існуючий підрядок):", time_real_2)
print("Час виконання для статті 2 (вигаданий підрядок):", time_unreal_2)


