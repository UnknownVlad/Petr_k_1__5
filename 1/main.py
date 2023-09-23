
def read_f(file):
    numbers = []
    with open(file, 'r') as file:
        for line in file:
            numbers += [int(num) for num in line.split()]
    return numbers

def write_f(file, list):
    with open(file, 'w') as f:
        for item in list:
            f.write(str(item) + ' ')

def create_new_list(file1, file2):
    # Чтение элементов из файлов
    list1 = read_f(file1)
    list2 = read_f(file2)

    # Отбор нужных элементов и сортировка
    new_list = sorted(
        set([x for x in list1 if x % 2 == 0 and x not in list2] + [x for x in list2 if x % 2 != 0 and x not in list1]))

    # Запись списка в файл
    write_f("new_file.txt", new_list)

    return new_list


create_new_list("f1.txt", "f2.txt")

