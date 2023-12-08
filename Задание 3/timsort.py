def insertion_sort(arr, left_index=0, right_index=None):
    if right_index is None:
        right_index = len(arr) - 1
    for i in range(left_index + 1, right_index + 1):
        insertion_key = arr[i]
        j = i - 1
        while j >= left_index and (abs(arr[j] ** 2) > abs(insertion_key ** 2) or (abs(arr[j] ** 2) == abs(insertion_key ** 2) and arr[j] < insertion_key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insertion_key
    return arr


def merge(sorted_left, sorted_right):
    merged_result = []
    while sorted_left and sorted_right:
        left_value, left_squared = sorted_left[0], abs(sorted_left[0] ** 2)
        right_value, right_squared = sorted_right[0], abs(sorted_right[0] ** 2)
        if left_squared < right_squared or (left_squared == right_squared and left_value > right_value):
            merged_result.append(left_value)
            sorted_left.pop(0)
        else:
            merged_result.append(right_value)
            sorted_right.pop(0)
    merged_result.extend(sorted_left or sorted_right)
    return merged_result


def tim_sort(arr, elements_count):
    min_run_length = 32
    for i in range(0, elements_count, min_run_length):
        insertion_sort(arr, i, min((i + min_run_length - 1), (elements_count - 1)))
        print(f"Part {i // min_run_length }: {' '.join(map(str, arr[i:min(i + min_run_length, elements_count)]))}")

    merge_size = min_run_length
    while merge_size < elements_count:
        for start_index in range(0, elements_count, merge_size * 2):
            mid_point = start_index + merge_size - 1
            end_point = min(start_index + merge_size * 2 - 1, (elements_count - 1))

            merged_parts = merge(sorted_left=arr[start_index:mid_point + 1], sorted_right=arr[mid_point + 1:end_point + 1])

            arr[start_index:start_index + len(merged_parts)] = merged_parts

        merge_size *= 2
    return arr

### Почему TimSort соответствует критериям:
1. Производительность на случайных данных:
- TimSort обеспечивает высокую производительность на случайных и разнообразных массивах данных, благодаря эффективной обработке крайних случаев и частично отсортированных последовательностей.
2. Производительность на больших массивах:
- TimSort хорошо масштабируется и обладает оптимальным поведением на больших объемах данных, что позволяет быстро сортировать массивы большого размера.
3. Реализован в стандартной библиотеке Python:
- Алгоритм TimSort реализован в стандартной библиотеке Python, что упрощает его использование и обеспечивает оптимальную производительность при работе с массивами любого размера и разнообразной структурой.
### Завершение:
В итоге алгоритм TimSort демонстрирует высокую производительность на случайных и больших массивах данных, что делает его отличным выбором для обработки массивов любого размера и структуры.(можно ознакомиться с проведенным мною исследованием алгоритма)
