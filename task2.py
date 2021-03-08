#!/usr/bin/python3

"""
Author: Matthew Kriz
Module Name: task2
Date: 08/03/2021
"""
from functools import reduce
from typing import Optional


class task2:
    @staticmethod
    def find_max(array: list) -> int:
        maximum = array[0]
        for i in array[1:]:
            if i > maximum:
                maximum = i
        return maximum

    @staticmethod
    def linear_research(array: list, what: object) -> Optional[object]:
        for i in array:
            if i == what:
                return array.index(i)
        return None

    @staticmethod
    def reverse(string: str) -> str:
        return reduce(lambda x, y: x + y, [i for i in string[::-1]])

    @staticmethod
    def caesar(string: str, rotation: int) -> str:
        return reduce(lambda x, y: x + y, [chr((ord(i) - 65 + rotation) % 26 + 65) for i in string if i.isupper()] +
                      [chr((ord(i) - 97 + rotation) % 26 + 97) for i in string if i.islower()])

    @staticmethod
    def selection_sort(array: list) -> list:
        for i in range(len(array) - 1):
            max_pos = i
            for j in range(i + 1, len(array)):
                if array[j] > array[max_pos]:
                    max_pos = j

            array[i], array[max_pos] = array[max_pos], array[i]

        return array

    @staticmethod
    def frequency_analysis(string: str, not_case: bool = True) -> dict:
        string = string.upper() if not_case else string

        dictionary = {i: 0 for i in string if i.isalnum()}
        for i in dictionary.keys():
            dictionary[i] = string.count(i)

        return dictionary

