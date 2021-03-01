"""
Author: Matthew Kriz
Module Name: task1
Date: 27/02/2021
"""


class task1:

    @staticmethod
    def print_numbers(how_many: int) -> None:
        for i in range(how_many + 1):
            print(i)

    @staticmethod
    def print_even_numbers(upper_bound: int) -> None:
        for i in range(upper_bound + 1):
            if i % 2 == 0:
                print(i)

    @staticmethod
    def print_power(how_many: int, base: int) -> None:
        for i in range(how_many + 1):
            print(i ** base)

    @staticmethod
    def print_fibonacci(how_many: int) -> None:
        count = 0
        first = 0
        second = 1
        while count < how_many:
            print(first)

            next_element = first + second
            first = second
            second = next_element

            count += 1

    @staticmethod
    def print_factorial(how_many: int) -> None:
        summary = 1

        for i in range(how_many):
            summary *= i

        print(summary)

    @staticmethod
    def print_test_prime_number(number: int) -> None:
        flag = True

        for i in range(2, number // 2 + 1):
            if number % i == 0:
                flag = False
                break

        print(flag)

    @staticmethod
    def return_number_divisors(number: int) -> list:
        return [i for i in range(2, number // 2 + 1) if number % i == 0]

    @staticmethod
    def print_test_prime_number2(number: int) -> None:
        flag = True

        if len(return_number_divisors(number)) > 0:
            flag = False

        print(flag)

    @staticmethod
    def return_test_prime_number(number: int) -> bool:
        flag = True

        for i in range(2, number // 2 + 1):
            if number % i == 0:
                flag = False
                break

        return flag

    @staticmethod
    def print_prime_numbers(how_many: int) -> None:
        number = 3

        while True:
            if return_test_prime_number(number):
                print(number)
                how_many -= 1

            if how_many == 0:
                break

            number += 1

    @staticmethod
    def return_digital_sum(number: int) -> int:
        number_str = str(number)
        summary = 0

        for i in number_str:
            summary += int(i)

        return summary

    @staticmethod
    def print_randoms(how_many: int) -> None:
        pass
