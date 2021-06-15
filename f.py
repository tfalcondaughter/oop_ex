def find_b(word):
    b = 0
    bb = 0
    bb_c = 0
    for i in range(len(word)):
        if word[i] == 'b':
            b += 1
            bb_c += 1
        else:
            bb_c = 0

        if bb_c >= 2:
            bb += 1

    return b, bb


w = input()
print(find_b(w))
