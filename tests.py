import unittest
from main import algo1
from main import algo2
from main import algo3

class TestSecondAlgo(unittest.TestCase):

    def test0001_1(self):
        self.assertEqual(len(algo2('data/simple1.dot', 'data/simple1')), 15)

    def test001_1(self):
        self.assertEqual(len(algo2('data/simple2.dot', 'data/simple2')), 12)

    def test01_1(self):
        self.assertEqual(len(algo2('data/simple4.dot', 'data/simple4')), 1)

    def test1_1(self):
        self.assertEqual(len(algo2('data/skos.dot', 'data/grammar1')), 810)

    def test2_1(self):
        self.assertEqual(len(algo2('data/generations.dot', 'data/grammar1')), 2164)

    def test3_1(self):
        self.assertEqual(len(algo2('data/travel.dot', 'data/grammar1')), 2499)

    def atest4_1(self):
        self.assertEqual(len(algo2('data/univ-bench.dot', 'data/grammar1')), 2540)

    def test995_1(self):
        self.assertEqual(len(algo2('data/atom-primitive.dot', 'data/grammar1')), 15454)

    def test996_1(self):
        self.assertEqual(len(algo2('data/biomedical-mesure-primitive.dot', 'data/grammar1')), 15156)

    def test7_1(self):
        self.assertEqual(len(algo2('data/foaf.dot', 'data/grammar1')), 4118)

    def test998_1(self):
        self.assertEqual(len(algo2('data/people_pets.dot', 'data/grammar1')), 9472)

    def test999_1(self):
        self.assertEqual(len(algo2('data/funding.dot', 'data/grammar1')), 17634)

    def test9910_1(self):
        self.assertEqual(len(algo2('data/wine.dot', 'data/grammar1')), 66572)

    def test9911_1(self):
        self.assertEqual(len(algo2('data/pizza.dot', 'data/grammar1')), 56195)

    #
    # #     sad
    # # sad
    # #     sad
    #

    def test1_2(self):
        self.assertEqual(len(algo2('data/skos.dot', 'data/grammar2')), 1)

    def test2_2(self):
        self.assertEqual(len(algo2('data/generations.dot', 'data/grammar2')), 0)

    def test3_2(self):
        self.assertEqual(len(algo2('data/travel.dot', 'data/grammar2')), 63)

    def test4_2(self):
        self.assertEqual(len(algo2('data/univ-bench.dot', 'data/grammar2')), 81)

    def test995_2(self):
        self.assertEqual(len(algo2('data/atom-primitive.dot', 'data/grammar2')), 122)

    def test996_2(self):
        self.assertEqual(len(algo2('data/biomedical-mesure-primitive.dot', 'data/grammar2')), 2871)

    def test7_2(self):
        self.assertEqual(len(algo2('data/foaf.dot', 'data/grammar2')), 10)

    def test998_2(self):
        self.assertEqual(len(algo2('data/people_pets.dot', 'data/grammar2')), 37)

    def test999_2(self):
        self.assertEqual(len(algo2('data/funding.dot', 'data/grammar2')), 1158)

    def test9910_2(self):
        self.assertEqual(len(algo2('data/wine.dot', 'data/grammar2')), 133)

    def test9911_2(self):
        self.assertEqual(len(algo2('data/pizza.dot', 'data/grammar2')), 1262)


class TestThirdAlgo(unittest.TestCase):

    def test0001_1(self):
        self.assertEqual(len(algo3('data/simple1.dot', 'data/simple1')), 15)

    def test001_1(self):
        self.assertEqual(len(algo3('data/simple2.dot', 'data/simple2')), 12)

    def test01_1(self):
        self.assertEqual(len(algo3('data/simple4.dot', 'data/simple4')), 1)

    def test1_1(self):
        self.assertEqual(len(algo3('data/skos.dot', 'data/grammar1')), 810)

    def test2_1(self):
        self.assertEqual(len(algo3('data/generations.dot', 'data/grammar1')), 2164)

    def test3_1(self):
        self.assertEqual(len(algo3('data/travel.dot', 'data/grammar1')), 2499)

    def atest4_1(self):
        self.assertEqual(len(algo3('data/univ-bench.dot', 'data/grammar1')), 2540)

    def test995_1(self):
        self.assertEqual(len(algo3('data/atom-primitive.dot', 'data/grammar1')), 15454)

    def test996_1(self):
        self.assertEqual(len(algo3('data/biomedical-mesure-primitive.dot', 'data/grammar1')), 15156)

    def test7_1(self):
        self.assertEqual(len(algo3('data/foaf.dot', 'data/grammar1')), 4118)

    def test998_1(self):
        self.assertEqual(len(algo3('data/people_pets.dot', 'data/grammar1')), 9472)

    def test999_1(self):
        self.assertEqual(len(algo3('data/funding.dot', 'data/grammar1')), 17634)

    def test9910_1(self):
        self.assertEqual(len(algo3('data/wine.dot', 'data/grammar1')), 66572)

    def test9911_1(self):
        self.assertEqual(len(algo3('data/pizza.dot', 'data/grammar1')), 56195)

    #
    # #     sad
    # # sad
    # #     sad
    #

    def test1_2(self):
        self.assertEqual(len(algo3('data/skos.dot', 'data/grammar2')), 1)

    def test2_2(self):
        self.assertEqual(len(algo3('data/generations.dot', 'data/grammar2')), 0)

    def test3_2(self):
        self.assertEqual(len(algo3('data/travel.dot', 'data/grammar2')), 63)

    def test4_2(self):
        self.assertEqual(len(algo3('data/univ-bench.dot', 'data/grammar2')), 81)

    def test995_2(self):
        self.assertEqual(len(algo3('data/atom-primitive.dot', 'data/grammar2')), 122)

    def test996_2(self):
        self.assertEqual(len(algo3('data/biomedical-mesure-primitive.dot', 'data/grammar2')), 2871)

    def test7_2(self):
        self.assertEqual(len(algo3('data/foaf.dot', 'data/grammar2')), 10)

    def test998_2(self):
        self.assertEqual(len(algo3('data/people_pets.dot', 'data/grammar2')), 37)

    def test999_2(self):
        self.assertEqual(len(algo3('data/funding.dot', 'data/grammar2')), 1158)

    def test9910_2(self):
        self.assertEqual(len(algo3('data/wine.dot', 'data/grammar2')), 133)

    def test9911_2(self):
        self.assertEqual(len(algo3('data/pizza.dot', 'data/grammar2')), 1262)


if __name__ == '__main__':
    unittest.main()