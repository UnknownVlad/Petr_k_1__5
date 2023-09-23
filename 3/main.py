
def read_array_from_file(file_name):
    array = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]
            array.append(row)
    return array

def find_max_length_segments(segments):
    segments.sort(key=lambda x: x[1])  # Сортируем отрезки по правому концу
    total_length = 0
    #Инициализируем 3 отрезка
    first, second, third = None, None, None

    for segment in segments:
        if first is None:
            first = segment
        elif second is None:
            second = segment
        elif third is None:
            third = segment
        else:

            min_length = min(first[1] - first[0], second[1] - second[0], third[1] - third[0])
            # Находим минимальную длину отрезка для замены
            if segment[1] - segment[0] > min_length:
                if first[1] - first[0] == min_length:
                    first = segment
                elif second[1] - second[0] == min_length:
                    second = segment
                else:
                    third = segment
    # Находим максимальный ищем сумарную длину
    total_length = (first[1] - first[0]) + (second[1] - second[0]) + (third[1] - third[0])
    return total_length, first, second, third



print(find_max_length_segments(read_array_from_file("f.txt")))