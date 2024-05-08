
import timeit

def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    # Базове число для хешування та модуль
    base = 256 
    modulus = 101  
    
    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

with open('стаття 1.txt', 'r', encoding='windows-1251') as file:
    article1 = file.read()

with open('стаття 2.txt', 'r', encoding='windows-1251') as file:
    article2 = file.read()

# Вимірюємо час виконання алгоритму для статті 1
start_time = timeit.default_timer()
real_1 = rabin_karp_search(article1, "звичайно являють собою послідовність кроків")
time_real_1 = timeit.default_timer() - start_time

start_time = timeit.default_timer()
unreal_1 = rabin_karp_search(article1, "Якби ви вчилися так, як треба, то й мудрість би була своя")
time_unreal_1 = timeit.default_timer() - start_time

# Вимірюємо час виконання алгоритму для статті 2
start_time = timeit.default_timer()
real_2 = rabin_karp_search(article2, "Графові моделі СУБД надають")
time_real_2 = timeit.default_timer() - start_time

start_time = timeit.default_timer()
unreal_2 = rabin_karp_search(article2, "Вогонь запеклих не пече")
time_unreal_2 = timeit.default_timer() - start_time

# Виведення результатів
print("Час виконання для статті 1 (існуючий підрядок):", time_real_1)
print("Час виконання для статті 1 (вигаданий підрядок):", time_unreal_1)
print("Час виконання для статті 2 (існуючий підрядок):", time_real_2)
print("Час виконання для статті 2 (вигаданий підрядок):", time_unreal_2)



