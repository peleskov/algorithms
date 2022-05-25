from hashlib import sha256


def count_subst(txt):
    out = set()
    for len_ in range(1, len(txt)):
        for i in range(0, len(txt)):
            if i + len_ > len(txt):
                break
            subst = txt[i:i + len_]
            if subst != ' ':
                out.add(sha256(subst.encode()).hexdigest())
    return len(out)


text = input('Введите строку: ')
print(count_subst(text))
