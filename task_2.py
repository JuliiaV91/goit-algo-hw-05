
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0
    upper_bound = None
 
    while low <= high: 
        mid = (high + low) // 2
        count +=1
         # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < target:
            low = mid + 1
         # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > target:
            high = mid - 1
         # інакше x присутній на позиції і повертаємо його
        else:
            return (count, arr[mid], mid)
        
        if arr[mid] >= target:
            upper_bound = arr[mid]
     # якщо елемент не знайдений
    return (count, upper_bound, None)

arr = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9]
target = 0.6

count, upper_bound, position = binary_search(arr, target)

if position is not None:
    print(f"Кількість ітерацій: {count}")
    print(f"Елемент присутній на позиції {position}, а верхня межа - {upper_bound}")
else:
    print(f"Елемент {target} відсутній в масиві. Верхня межа - {upper_bound}")