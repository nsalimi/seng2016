import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(1) != 1)
    def test_two(self):
        app = FizzBuzz()
        self.failIf(app.calc(6) != "fizz")
    def test_three(self):
        app = FizzBuzz()
        self.failIf(app.calc(10) != "buzz")
    def test_four(self):
        app = FizzBuzz()
        self.failIf(app.calc(30) != "fizzbuzz")
    def test_primes(self):
        app = FizzBuzz()
        for i in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97):
            self.failIf(app.calc(i) != "is a prime")

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100  )

    
def main():
    unittest.main()

if __name__ == "__main__":
    main()
