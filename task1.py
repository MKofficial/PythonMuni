"""
Author: Matthew Kriz
Module Name: task1
Date: 27/02/2021
"""

from random import randint


class task1:

    @staticmethod
    def numbers(how_many: int) -> list:
        assert how_many >= 0
        return [i for i in range(how_many + 1)]

    @staticmethod
    def even_numbers(upper_bound: int) -> list:
        assert upper_bound > 0
        return [i for i in range(upper_bound + 1) if i % 2 == 0]

    @staticmethod
    def power(how_many: int, base: int) -> list:
        assert how_many >= 0 and base > 0
        return [i ** base for i in range(how_many + 1)]

    @staticmethod
    def fibonacci(how_many: int) -> list:
        assert how_many > 0

        count = 0
        first = 0
        second = 1

        sequence = []
        while count < how_many:
            sequence.append(first)

            next_element = first + second
            first = second
            second = next_element

            count += 1

        return sequence

    @staticmethod
    def factorial(how_many: int) -> int:
        assert how_many >= 0

        summary = 1

        for i in range(how_many):
            summary *= i

        return summary

    @staticmethod
    def test_prime_number(number: int) -> bool:
        assert number > 0

        flag = True

        for i in range(2, number // 2 + 1):
            if number % i == 0:
                flag = False
                break

        return flag

    @staticmethod
    def number_divisors(number: int) -> list:
        assert number >= 0

        return [i for i in range(2, number // 2 + 1) if number % i == 0]

    @staticmethod
    def test_prime_number2(number: int) -> bool:
        assert number >= 0

        flag = True

        for i in range(2, number // 2 + 1):
            if number % i == 0:
                flag = False
                break

        return flag

    @staticmethod
    def prime_numbers(how_many: int) -> list:
        assert how_many >= 0

        number = 3
        numbers = []

        while True:
            if task1.test_prime_number(number):
                numbers.append(number)
                how_many -= 1

            if how_many == 0:
                break

            number += 1

        return numbers

    @staticmethod
    def digital_sum(number: int) -> int:
        assert number >= 0

        number_str = str(number)
        summary = 0

        for i in number_str:
            summary += int(i)

        return summary

    @staticmethod
    def print_randoms(how_many: int) -> None:
        assert how_many > 0
        max_number = 100

        numbers = [randint(0, max_number) for _ in range(how_many)]
        max_number = max(numbers)
        min_number = min(numbers)
        avg_number = sum(numbers) / len(numbers)

        print("Numbers: " + str(numbers))
        print("Max number: " + str(max_number))
        print("Min number: " + str(min_number))
        print("Average number: " + str(avg_number))
