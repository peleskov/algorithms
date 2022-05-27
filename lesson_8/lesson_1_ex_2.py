from collections import Counter


def huffman(txt):
    text_dict = {}
    for key, val in Counter(txt).most_common():
        text_dict.setdefault(val, [])
        text_dict[val].append(key)
    list_tree = huffman_tree(text_dict)
    codes = code_table(list_tree)
    return text_encrypt(txt, codes)


def huffman_tree(dict_, el=None):
    if not dict_:
        return el[1]
    items_pop = dict_.popitem()
    if not el:
        el = [items_pop[0], items_pop[1].pop()]
    else:
        k = items_pop[0] + el[0]
        dict_.setdefault(k, [])
        dict_[k].append([el[1], items_pop[1].pop()])
        el = [items_pop[0], items_pop[1].pop()] if items_pop[1] else None
    if items_pop[1]:
        dict_.setdefault(items_pop[0], items_pop[1])
    dict_ = dict(sorted(dict_.items(), key=lambda x: x[0], reverse=True))
    return huffman_tree(dict_, el)


def code_table(tree, result=None, code=''):
    if result is None:
        result = {}
    if not tree:
        return result
    branch_1 = tree.pop()
    branch_0 = tree.pop()
    if isinstance(branch_0, list):
        code_table(branch_0, result, f'{code}0')
    else:
        result.setdefault(branch_0, f'{code}0')
    if isinstance(branch_1, list):
        code_table(branch_1, result, f'{code}1')
    else:
        result.setdefault(branch_1, f'{code}1')
    return code_table(tree, result)


def text_encrypt(txt, codes):
    out = ''
    for i in txt:
        out += codes[i]
    return ' '.join([out[i:i+4] for i in range(0, len(out), 4)])


text = 'beep boop beer!'
print(huffman(text))
