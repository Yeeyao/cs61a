from math import sqrt


def couple(lst1, lst2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> lst1 = [1, 2, 3]
    >>> lst2 = [4, 5, 6]
    >>> couple(lst1, lst2)
    [[1, 4], [2, 5], [3, 6]]
    >>> lst3 = ['c', 6]
    >>> lst4 = ['s', '1']
    >>> couple(lst3, lst4)
    [['c', 's'], [6, '1']]
    """
    assert len(lst1) == len(lst2)
    "*** YOUR CODE HERE ***"
    return [[lst1[i], lst2[i]] for i in range(len(lst1))]


def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    "*** YOUR CODE HERE ***"
    c1Lat = get_lat(city1)
    c1Lon = get_lon(city1)
    c2Lat = get_lat(city2)
    c2Lon = get_lon(city2)
    return sqrt((c1Lat - c2Lat) ** 2 + (c1Lon - c2Lon) ** 2)


def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    "don't know how to use distance(city1, city2)"
    # c1Lat = get_lat(city1)
    # c1Lon = get_lon(city1)
    # c2Lat = get_lat(city2)
    # c2Lon = get_lon(city2)
    # c1dist = sqrt((c1Lat - lat) ** 2 + (c1Lon - lon) ** 2)
    # c2dist = sqrt((c2Lat - lat) ** 2 + (c2Lon - lon) ** 2)
    # if c1dist < c2dist:
    #     return get_name(city1)
    # else:
    #     return get_name(city2)
    "answer"
    "just make a new city"
    new_city = make_city('one', lat, lon)
    dist1 = distance(new_city, city1)
    dist2 = distance(new_city, city2)
    if dist1 < dist2:
        return get_name(city1)
    else:
        return get_name(city2)


def nut_finder(t):
    """Returns True if t contains a node with the value 'nut' and
    False otherwise.

    >>> scrat = tree('nut')
    >>> nut_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('nut')]), tree('branch2')])
    >>> nut_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> nut_finder(numbers)
    False
    >>> t = tree(1, [tree('nut',[tree('not nut')])])
    >>> nut_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    # if label(tree) == 'nut':
    #     return True
    # elif is_leaf(t):
    #     return False
    # else:
    #     nut_finder(branches(t))
    "answer1"
    if label(t) == 'nut':
        return True
    for b in branches(t):
        if nut_finder(b):
            return True
    return False
    "answer2"
    if label(t) == 'nut':
        return True
        return True in [nut_finder(b) for b in branches(t)]


def sprout_leaves(t, values):
    """Sprout new leaves containing the data in values at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    "最后的leaves中加上数值"
    # if is_leaf(t):
    #     return tree(label(t), [tree(v) for v in values])
    # for b in branches(t):
    #     if is_leaf(b):
    #         [b] + values
    # return t
    "answer"
    if is_leaf(t):
        return tree(label(t), [tree(v) for v in values])
    return tree(label(t), [sprout_leaves(s, values) for s in branches(t)])


def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # ban iteration and sets
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    "*** YOUR CODE HERE ***"
    "this is not considered"
    if not w1:
        return w2
    elif w1[0] == w2[0]:
        return add_chars(w1[1:], w2[1:])
    else:
        w2[0] + add_chars(w1, w2[1:])


def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"


def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            "*** YOUR CODE HERE ***"
            table[prev] = []
        "*** YOUR CODE HERE ***"
        table[prev] += [word]
        prev = word
    return table


def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        "*** YOUR CODE HERE ***"
        result += word + ' '
        word = random.choice(table[word])
    return result.strip() + word


def height(t):
    """Return the height of a tree. 
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        1 + max([height(branch) for branch in branches[t]])


def square_tree(t):
    sq_branches = [square_tree(branches) for branches in branches(t)]
    return tree(label(t) ** 2, sq_branches)


def find_path(tree, x):
    if label(tree) == x:
        return [label(tree)]
    for branch in branches(tree):
        path = find_path(branch, x)
        if path:
            return [label(tree)] + path

def add_this_many(x, el, lst):
    times = 0
    for i in lst:
        if i == x:
            times += 1
    while times > 0:
        lst.append(el)

def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    table = {}
    for i in s:
        key = fn(i)
        if key in table:
            table[key] += [i]
        else:
            table[key] = [i]
    return table