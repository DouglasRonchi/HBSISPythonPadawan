def db_sort(matriz):
    list_strings = []
    list_numbers = []
    for item in matriz:
        if type(item) == str:
            list_strings.append(item)
        if type(item) == int:
            list_numbers.append(item)
    list_numbers.sort()
    list_strings.sort()
    final_list = list_numbers.copy() + list_strings.copy()
    return final_list

