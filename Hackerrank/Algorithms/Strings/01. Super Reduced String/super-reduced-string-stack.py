#!/bin/python3

import sys


class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]


def super_reduced_string(string):
    stack = Stack()
    i = 0
    while i < len(string):
        if stack.is_empty():
            stack.push(string[i])
        elif stack.peek() == string[i]:
            stack.pop()
        else:
            stack.push(string[i])
        i += 1
    string = ""
    while not stack.is_empty():
        string = stack.pop() + string
    return string if len(string) > 0 else "Empty String"


def main():
    print(super_reduced_string(input().strip()))


if __name__ == '__main__':
    main()
