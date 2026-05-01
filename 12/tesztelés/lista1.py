def match_ends(words: list) -> int:
    num_of_w = 0
    for w in words:
        if len(w) > 1 and w[0] == w[-1]:
            num_of_w += 1
    return num_of_w

def front_x(words: list) -> list:
    x_words = []
    other_words = []
    for w in words:
        if w[0] == 'x':
            x_words.append(w)
        else:
            other_words.append(w)
    x_words.sort()
    other_words.sort()
    x_words += other_words[:]
    return x_words