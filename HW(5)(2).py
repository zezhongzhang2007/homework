def get_matryoshka_list(list):
    last_value = 0
    start = 0
    end = 0
    x = 0
    while x < len(list):
        e = list[x]
        if last_value <= e:
            end += 1
            last_value = e
            x += 1
        elif last_value > e:
            list[start:end] = [list[start:end]]
            start += 1
            list[start] = [list[start]]
            start += 1
            last_value = 0
            x = start
            end = start
    list[start:end] = [list[start:end]]
    return list


original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 1, 3]
matryoshka_list = get_matryoshka_list(original_list)
print(matryoshka_list)