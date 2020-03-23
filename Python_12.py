# 模块
' a test module '

__author__ = "dong"

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print("Hello , %s!" % args[0])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
