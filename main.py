import unittest
import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score() == 0

    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):  # changed name to something accurate and not repeated
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24

    def testPerfectGame(self):
        self.rollMany(10, 12)
        assert self.game.score() == 300

    def testAllSpare(self):
        self.rollMany(5, 21)
        assert self.game.score() == 150

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)

    # my test cases
    def testAddingAfterAllSpares(self):
        self.rollMany(5, 21)
        self.assertRaises(ValueError, self.game.roll, 3)
        assert self.game.score() == 150

    def testAddingAfterAllSStrikes(self):
        self.rollMany(10, 12)
        self.assertRaises(ValueError, self.game.roll, 3)
        assert self.game.score() == 300

    def testAddingNegativeNumber(self):
        self.assertRaises(ValueError, self.game.roll, -1)

    def testAddingTooBigNumber(self):
        self.assertRaises(ValueError, self.game.roll, 11)

    def testUnfinishedGame(self):
        self.rollMany(3, 4)
        self.assertRaises(ValueError, self.game.score)
