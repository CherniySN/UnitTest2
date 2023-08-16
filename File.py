#модeльное тестирование с использованием Unit test

import unittest
from  main import A

class Test(unittest.TestCase):

    def test(self):
        a = A(5)
        self.assertEqual(a.r(), 7)

        a = A(2)
        self.assertEqual(a.r(), 2)

unittest.main()





