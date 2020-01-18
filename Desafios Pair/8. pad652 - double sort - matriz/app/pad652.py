def db_sort(matriz):
    list_strings = []
    list_numbers = []
    [list_numbers.append(item) if type(item) == int else list_strings.append(item) for item in matriz]
    list_numbers.sort()
    list_strings.sort()
    final_list = list_numbers.copy() + list_strings.copy()
    return final_list

