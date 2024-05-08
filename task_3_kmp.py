
import timeit

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

with open('стаття 1.txt', 'r', encoding='windows-1251') as file:
    article1 = file.read()

with open('стаття 2.txt', 'r', encoding='windows-1251') as file:
    article2 = file.read()

# Вимірюємо час виконання алгоритму для статті 1
start_time = timeit.default_timer()
real_1 = kmp_search(article1, "звичайно являють собою послідовність кроків")
time_real_1 = timeit.default_timer() - start_time

start_time = timeit.default_timer()
unreal_1 = kmp_search(article1, "Якби ви вчилися так, як треба, то й мудрість би була своя")
time_unreal_1 = timeit.default_timer() - start_time

# Вимірюємо час виконання алгоритму для статті 2
start_time = timeit.default_timer()
real_2 = kmp_search(article2, "Графові моделі СУБД надають")
time_real_2 = timeit.default_timer() - start_time

start_time = timeit.default_timer()
unreal_2 = kmp_search(article2, "Вогонь запеклих не пече")
time_unreal_2 = timeit.default_timer() - start_time

# Виведення результатів
print("Час виконання для статті 1 (існуючий підрядок):", time_real_1)
print("Час виконання для статті 1 (вигаданий підрядок):", time_unreal_1)
print("Час виконання для статті 2 (існуючий підрядок):", time_real_2)
print("Час виконання для статті 2 (вигаданий підрядок):", time_unreal_2)

