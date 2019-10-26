"""
Napisz test do kodu zawartego w src/rna.py
"""
import unittest
from parameterized import parameterized
​
from src.rna import transcribe_rna, validate_dna
​
class RnaTestCase(unittest.TestCase):
    @parameterized.expand([
        ['1', 'GCTA', 'CGAU'],
        ['2', 'G', 'C'],
        ['3', 'GCTAAAAT', 'CGAUUUUA'],
    ])
    def test_01_transcribe_rna(self, name, a, b):
        self.assertEqual(transcribe_rna(a), b)
​
    def test_03_transcribe_rna_key_error(self):
        with self.assertRaises(KeyError):
            transcribe_rna('x')
​
    def test_02_validate_dna(self):
        self.assertTrue(validate_dna('GCTA'))
        self.assertFalse(validate_dna('X'))