import unittest

class TestParse(unittest.TestCase):
    def test_parse_cust_name(self):
        cp = ConfigurationParser()
        expected_names = ['CUSTOMER A', 'CUSTOMER B']
        parsed_names = cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)
