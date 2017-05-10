import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2017, 5, 10)
        self.assertEqual(weekday, 2)

        weekday = calculate(2020, 2, 29)
        self.assertEqual(weekday, 6)

        weekday = calculate(2001, -1, 3)
        self.assertEqual(weekday, -1)

        weekday = calculate(2013, 13, 13)
        self.assertEqual(weekday, -1)

        weekday = calculate(2013, 'a', 13)
        self.assertEqual(weekday, -1)

        retcode3 = main(("--year", "2001", "--month", "1", "--day", "3", "abc", "sgsg"))
        self.assertEqual(retcode3, -1)

        retcode4 = main(("--year", "2020", "--month", "2", "--day", "29"))
        self.assertEqual(retcode4, 6)

        retcode5 = main(("--year", "1990", "--month", "2", "--day", "29"))
        self.assertEqual(retcode5, -1)

        retcode6 = main(("--year", "2017", "--month", "4", "--day", "31"))
        self.assertEqual(retcode6, -1)

        retcode7 = main(("--year", "2017", "--month", "5", "--day", "10"))
        self.assertEqual(retcode7, 2)


if __name__ == '__main__':
    unittest.main()
