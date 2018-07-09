#!/usr/bin/python
# coding: UTF-8
import sys

sys.setrecursionlimit(1500)  # set the maximum depth as 1500


def recursion(n):
    if (n <= 0):
        return
    print n
    recursion(n - 1)


if __name__ == "__main__":
    recursion(1000)
