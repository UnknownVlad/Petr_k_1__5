

def check_array_overlap(file1, file2):
    array1 = read_array_from_file(file1)
    array2 = read_array_from_file(file2)
    t = [
        [0, 0],
        [0, len(array1)-1],
        [len(array1)-1, len(array1[0])],
        [len(array1)-1, 0]
    ]
    # поворачиваем вправо на 90 градусов матрицу 4 раза чтобы узнать на каком повороте совпадут массивы
    for i in range(0, 4):
        if(is_eq_size(array1, array2)) and is_eq_arr(array1, array2):
            return t[4 - i]

        array2 = rotate(array2)

    return None

def is_eq_arr(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i][j] != arr2[i][j]:
                return False
    return True
def is_eq_size(arr1, arr2):
    return len(arr1) == len(arr2) and len(arr1[0]) == len(arr2[0])
def read_array_from_file(file_name):
    array = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]
            array.append(row)
    return array

# функция поворота матрицы на 90 гр вправо
def rotate(arr):
    return tuple(zip(*arr[::-1]))


file1 = 'a1.txt'
file2 = 'a2.txt'
result = check_array_overlap(file1, file2)

if result is None:
    print("no way")
else:
    print(result)
