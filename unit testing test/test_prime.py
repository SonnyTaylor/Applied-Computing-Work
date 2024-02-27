import unittest
from prime import is_prime


# prime file for refererence
"""
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

"""


class TestPrime(unittest.TestCase):
    def test_is_prime_with_prime_number(self):
        # Test if a prime number returns True
        self.assertTrue(is_prime(7))

    def test_is_prime_with_non_prime_number(self):
        # Test if a non-prime number returns False
        self.assertFalse(is_prime(10))

    def test_is_prime_with_negative_number(self):
        # Test if a negative number returns False
        self.assertFalse(is_prime(-5))

    def test_is_prime_with_zero(self):
        # Test if zero returns False
        self.assertFalse(is_prime(0))

    def test_is_prime_with_one(self):
        # Test if one returns False
        self.assertFalse(is_prime(1))

    def test_is_prime_with_large_prime_number(self):
        # Test if a large prime number returns True
        self.assertTrue(is_prime(15485863))


if __name__ == "__main__":
    unittest.main()
