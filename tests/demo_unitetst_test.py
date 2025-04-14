import unittest

def inc(x):
    return x + 1

def compare(x):
    return x > 10

class Demo:
    def __init__(self, name):
        self.name = name

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Run before all tests...")
        cls.demo = Demo("test_name")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Run after all tests...")

    def setUp(self) -> None:
        print("Run before each test..")

    def tearDown(self) -> None:
        print("Run after each test..")

    @unittest.skip("demonstration")
    def test_simple_skip(self):
        self.assertEqual(inc(3), 4)

    def test_equal(self):
        print(self.demo.name)
        self.assertEqual(inc(3), 4)
        self.assertEqual(inc(0), 1)
        self.assertEqual(inc(-9), -8)

        self.assertNotEqual(inc(5), 10)

    def test_bool(self):
        self.assertTrue(compare(11))
        self.assertTrue(compare(9))

        self.assertFalse(compare(6))
        self.assertFalse(compare(12))

    def test_in(self):
        fixtures  = [1,2,10,15]
        self.assertIn(10, fixtures )
        self.assertNotIn(11, fixtures )

    def test_none(self):
        self.assertIsNone(None)
        self.assertIsNotNone(5)

    def test_with_error(self):
        self.assertEqual(inc(8), 5, msg="Ожидаемое значение не равно полученному")

if __name__ == "__main__":
    unittest.main()