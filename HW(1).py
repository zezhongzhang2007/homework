def update_frequencies(old, new):
    a = 0
    c = 0
    t = 0
    g = 0
    for word in new:
        y = 0
        for number in old:
            number_ = list(number)
            if word == number_[0]:
                number_[1] += 1
                old[y] = tuple(number_)
                if y == 0:
                    a += 1
                elif y == 1:
                    c += 1
                elif y == 2:
                    t += 1
                elif y == 3:
                    g += 1
                break
            else:
                y += 1
    print('A-->', a, end=' | ')
    print('C-->', c, end=' | ')
    print('T-->', t, end=' | ')
    print('G-->', g, end=' | \n')
    return old


old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
new_sequence = "ACCCGTTA"
print(update_frequencies(old_frequencies, new_sequence))
