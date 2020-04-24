class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price):
        self.balance = 0
        self.goods_name = name
        self.goods_price = price
        self.goods_num = 0
    
    def vend(self):
        if self.goods_num > 0:
            oldBalance = self.balance
            if oldBalance >= self.goods_price:
                self.balance = 0
                self.goods_num -= 1
                if oldBalance == self.goods_price:
                    return "Here is your {0}.".format(self.goods_name)
                else:
                    return "Here is your {0} and ${1} change.".format(self.goods_name, oldBalance - self.goods_price)
            else:
                moreBalance = self.goods_price - self.balance
                return "You must add ${0} more funds.".format(moreBalance)
        else:
            return "Machine is out of stock."

    def add_funds(self, fund):
        if self.goods_num > 0:
            self.balance += fund
            return "Current balance: ${0}".format(self.balance)
        else:
            return "Machine is out of stock. Here is your ${0}.".format(fund)
        
    def restock(self, num):
        self.goods_num += num
        return "Current {0} stock: {1}".format(self.goods_name, self.goods_num)
        
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(Tree(2, [Tree(4, [Tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    "flattened"
    # return [label(t)] + [preorder(branches(t))]
    "answer"
    if t.branches == []:
        return [t.label]
    flattened_children = []
    for child in t.branches:
        flattened_children += preorder(child)
    return [t.label] + flattened_children

def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    "*** YOUR CODE HERE ***"
    rest = link.empty
    while n > 0 :
        rest = link(n % 10, rest)
        n = n // 10
    return rest
        
def generate_paths(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """

    "*** YOUR CODE HERE ***"
    if t.label == value:
        yield[value]
    for b in t.branches:
        for path in generate_paths(b, value):
            yield[value] + path
        
    