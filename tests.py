import unittest
from main import solver

class TestStringMethods(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(solver('data/skos.dot', 'data/grammar1CNF'), 810)

    def test_2_1(self):
        self.assertEqual(solver('data/generations.dot', 'data/grammar1CNF'), 2164)

    def test_3_1(self):
        self.assertEqual(solver('data/travel.dot', 'data/grammar1CNF'), 2499)

    def test_4_1(self):
        self.assertEqual(solver('data/univ-bench.dot', 'data/grammar1CNF'), 2540)

    def test_5_1(self):
        self.assertEqual(solver('data/atom-primitive.dot', 'data/grammar1CNF'), 15454)

    def test_6_1(self):
        self.assertEqual(solver('data/biomedical-mesure-primitive.dot', 'data/grammar1CNF'), 15156)

    def test_7_1(self):
        self.assertEqual(solver('data/foaf.dot', 'data/grammar1CNF'), 4118)

    def test_8_1(self):
        self.assertEqual(solver('data/people_pets.dot', 'data/grammar1CNF'), 9472)

    def test_9_1(self):
        self.assertEqual(solver('data/funding.dot', 'data/grammar1CNF'), 17634)

    def test_10_1(self):
        self.assertEqual(solver('data/wine.dot', 'data/grammar1CNF'), 66572)

    def test_11_1(self):
        self.assertEqual(solver('data/pizza.dot', 'data/grammar1CNF'), 56195)
    #
    # #     sad
    # # sad
    # #     sad
    #
    def test_1_2(self):
        self.assertEqual(solver('data/skos.dot', 'data/grammar2CNF'), 1)

    def test_2_2(self):
        self.assertEqual(solver('data/generations.dot', 'data/grammar2CNF'), 0)

    def test_3_2(self):
        self.assertEqual(solver('data/travel.dot', 'data/grammar2CNF'), 63)

    def test_4_2(self):
        self.assertEqual(solver('data/univ-bench.dot', 'data/grammar2CNF'), 81)

    def test_5_2(self):
        self.assertEqual(solver('data/atom-primitive.dot', 'data/grammar2CNF'), 122)

    def test_6_2(self):
        self.assertEqual(solver('data/biomedical-mesure-primitive.dot', 'data/grammar2CNF'), 2871)

    def test_7_2(self):
        self.assertEqual(solver('data/foaf.dot', 'data/grammar2CNF'), 10)

    def test_8_2(self):
        self.assertEqual(solver('data/people_pets.dot', 'data/grammar2CNF'), 37)

    def test_9_2(self):
        self.assertEqual(solver('data/funding.dot', 'data/grammar2CNF'), 1158)

    def test_10_2(self):
        self.assertEqual(solver('data/wine.dot', 'data/grammar2CNF'), 133)

    def test_11_2(self):
        self.assertEqual(solver('data/pizza.dot', 'data/grammar2CNF'), 1262)


if __name__ == '__main__':
    unittest.main()