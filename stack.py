# -*- coding: utf-8 -*-
"""Class implementation of a stack a LIFO list

Methods
    push(item): Adds items to the top of the stack
    pop(): Removes and returns item on top of the Stack
    peek(): Returns item on top of the Stack
    size(): Returns the size of the Stack
"""


class Stack:
    def __init__(self):
        self.items = []

    """
    Adds an item to the top of the Stack
    """

    def push(self, item):
        self.items.append(item)

    """
    Returns the item on top of the Stack
    """

    def pop(self):
        if not self.__is_empty():
            return self.items.pop()
        return None

    """
    Returns an Integer count of items in the Stack
    """

    def size(self):
        return len(self.items)

    """
    Returns items on top of the stack
    """

    def peek(self):
        if not self.__is_empty():
            return self.items[-1]
        return None

    """
    Returns a printable  string representation of the Stack
    """

    def __is_empty(self):
        return not self.items

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack)
    stack.push(1)
    stack.push(2)
    print(stack)
    assert [1, 2] == stack.items
    print(stack)
    print(f'item on top of the stack is {stack.peek()}')
    item3 = stack.pop()
    print(stack)
    assert item3 == 2
    stack.pop()
    stack.pop()
    stack.peek()
