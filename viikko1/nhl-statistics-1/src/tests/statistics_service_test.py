import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_etsii_pelaajan(self):
        kurri = self.stats.search("Kurri").name
        #print(kurri)
        testi = Player("Kurri", "EDM", 37,53).name
        #print(testi)
        self.assertAlmostEqual(kurri, testi)

    def test_etsii_pelaajan2(self):
        rantanen = self.stats.search("Rantanen")
        self.assertAlmostEqual(rantanen, None)

    def test_etsii_joukkueen(self):
        pit = self.stats.team("PIT")[0].name
        #print(pit)
        self.assertAlmostEqual(pit, Player("Lemieux", "PIT", 45,54).name)

    def test_etsii_joukkueen2(self):
        col = self.stats.team("COL")
        self.assertAlmostEqual(col, [])

    #def test_top(self):


        