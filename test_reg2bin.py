import unittest

import reg2bin

class TestFunctions(unittest.TestCase):
    def test_cut_line(self):
        hex_values = '57,00,69,00'
        hex_list = ['57', '00', '69', '00']
        self.assertEqual(reg2bin.cut_line(hex_values), hex_list)

if __name__ == '__main__':
    unittest.main()
