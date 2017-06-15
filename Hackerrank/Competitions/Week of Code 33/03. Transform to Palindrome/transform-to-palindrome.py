#!/bin/python3


import sys
from functools import lru_cache


def transform(unique_trans: list, items: list) -> list:
    # Loop through all items in list
    for i in range(len(items)):
        # Loop through each transformation
        for j in range(len(unique_trans)):
            # If the item is in the transformation, transform it then break and move to the next item
            if items[i] in unique_trans[j][1]:
                items[i] = unique_trans[j][0]
                break
    return items


def unique_transformations(trans: list) -> list:
    # Sort each tranformation
    for i in range(len(trans)):
        trans[i] = sorted(trans[i])
    # Sort all the transformations
    trans.sort()

    # Loop through all transformations
    unique_trans = []
    for i in range(len(trans)):
        matched = False
        # Loop through all unique transformation sets
        for j in range(len(unique_trans)):
            # If transformation has an overlapping value get the union of the transformation and the set
            if trans[i][0] in unique_trans[j] or trans[i][1] in unique_trans[j]:
                unique_trans[j] = unique_trans[j].union({trans[i][0], trans[i][1]})
                matched = True

        # If there was no matching transformations yet, append a new set to the unique transformations
        if not matched:
            unique_trans.append({trans[i][0], trans[i][1]})

    # Get a value from each set and store it outside the set for replacing any occurances of the values in the set
    for i in range(len(unique_trans)):
        unique_trans[i] = (next(iter(unique_trans[i])), unique_trans[i])

    return unique_trans


@lru_cache(maxsize=None)
def longest_palindrome_subsequence(items: tuple, i: int, j: int):
    # Base Case 1: If there is only 1 item in items
    if i == j:
        return 1

    # Base Case 2: If there are only 2 items and they are both the same
    if items[i] == items[j] and i + 1 == j:
        return 2

    # If the first and last items are matching
    if items[i] == items[j]:
        return longest_palindrome_subsequence(items, i + 1, j - 1) + 2

    # If the first and last items are not matching
    return max(longest_palindrome_subsequence(items, i, j - 1), longest_palindrome_subsequence(items, i + 1, j))


def main():
    # Read the number of orion letters, number of transformations and length of string being checked
    n, k, m = map(int, input().strip().split(' '))

    # Read in the transformations
    transformations = []
    for _ in range(k):
        x, y = map(int, input().strip().split(' '))
        transformations.append((x, y))

    # Simplify transformations
    transformations = unique_transformations(transformations)

    # Read in the string
    S = list(map(int, input().strip().split(' ')))

    # Transform the string using the transformations
    S = tuple(transform(transformations, S))

    # Print the longest palindrome subsequence
    print(longest_palindrome_subsequence(S, 0, len(S)-1))


if __name__ == "__main__":
    main()
