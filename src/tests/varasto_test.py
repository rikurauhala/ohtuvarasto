import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_uudella_varastolla_vaara_tilavuus(self):
        uusi_varasto = Varasto(-10)
        self.assertAlmostEqual(uusi_varasto.tilavuus, 0.0)

    def test_uudella_varastolla_vaara_alkusaldo(self):
        uusi_varasto = Varasto(tilavuus=10, alku_saldo=-1)
        self.assertAlmostEqual(uusi_varasto.saldo, 0.0)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ylimeneva_lisays_ei_muuttaa_saldoa_oikein(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_negatiivinen_ottaminen_ei_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 9)
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 9)

    def test_ylimenava_ottaminen_vie_kaiken(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.saldo, 1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        self.varasto.ota_varastosta(1000)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_merkkijonoesitys_toimii_oikein(self):
        merkkijonoesitys = str(self.varasto)
        self.assertEqual(merkkijonoesitys, "saldo = 0, vielä tilaa 10")
