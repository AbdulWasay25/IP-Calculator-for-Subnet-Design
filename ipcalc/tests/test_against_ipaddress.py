"""Cross-check each feature with Python's ipaddress library. Add your own tests here.
Run from the repo root:  python -m unittest discover tests"""
import unittest
import ipaddress
from ipcalc import core


class TestCore(unittest.TestCase):
    def test_ip_roundtrip(self):
        self.assertEqual(core.int_to_ip(core.ip_to_int("192.168.1.1")), "192.168.1.1")

    def test_mask(self):
        self.assertEqual(core.mask_to_prefix(core.ip_to_int("255.255.255.0")), 24)


# Wasay: add tests for f4, f5, f7, f8 below
# Saad:  add tests for f1, f2, f3, f6 below

if __name__ == "__main__":
    unittest.main()
