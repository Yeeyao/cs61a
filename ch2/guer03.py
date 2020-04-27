def has_cycle(link):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    """
    # 不能仅仅判断 label
    # if link is Link.empty:
    #     return False
    # has_cycle(link.rest)
    # if link.rest == link.label:
    #     return True
    # 不是很懂这个方法
    tortoise = link
    hare = link.rest
    while tortoise.rest and hare.rest and hare.rest.rest:
        if tortoise is hare:
            return True
        tortoise = tortoise.rest
        hare = hare.rest.rest
    return False

    # 保存下所有已经遍历的元素
    seen = []
    while link.rest:
        if link in seen:
            return True
        seen.append(link)
        link = link.rest
    return False

def seq_in_link(link, sub_link):
    if sub_link is Link.empty:
        return True
    if link is Link.empty:
        return False
    if link.first == sub_link.first:
        return seq_in_link(link.rest, sub_link.rest)
    else:
        return seq_in_link(link.rest, sub_link)
    
class Cat():
    noise = 'meow'
    def __init__(self, name):
        self.name = name
        self.hungry = True
    def memo(self):
        if self.hungry:
            print(self.noise + ', ' + self.name + ' is hungry')
        else:
            print(self.noise + ' my name is ' + self.name)
    def eat(self):
        print(self.noise)
        self.hungry = False
    
class Kitten(Cat):
    noise = "i'm baby"
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
    def memo(self):
        Cat.memo(self)
        print('I want mama' + parent.name)