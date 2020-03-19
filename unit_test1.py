import unittest
import re

class TestParse(unittest.TestCase):
    def test_parse_cust_name(self):
        cp = ConfigurationParser()
        expected_names = ['CUSTOMER_A', 'CUSTOMER_B']
        parsed_names = cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)

    def test_parse_cust_vlan(self):
        cp = ConfigurationParser()
        customer_name = "CUSTOMER_A"
        expected_vlan = 100
        parsed_vlan = cp.parseCustomerVlan(customer_name)
        self.assertEqual(expected_vlan, parsed_vlan)

    def test_parse_cust_ip_address(self):
        cp = ConfigurationParser()
        customer_vlan = 100
        expected_ip = "10.10.100.1"
        parsed_ip = cp.parseCustomerIPAddress(customer_vlan)
        self.assertEqual(expected_ip, parsed_ip)

class ConfigurationParser:
    deviceConfig = open("isp_config1", "r").read()
    def parseCustomerNames(self):
        customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, self.deviceConfig)
        return customerNames

    def parseCustomerVlan(self, customerName):
        intPattern = (
            r"interface GigabitEthernet0/0.([0-9]+)\n\s+encapsulation\s+"
            r"dot1Q [0-9]+\n\s+ip vrf forwarding %s" % (customerName)
        )
        allCustomerSubInterfaces = re.search(intPattern, self.deviceConfig)
        return int(allCustomerSubInterfaces.group(1))

    def parseCustomerIPAddress(self, vlan):
        customerIpPattern = r'GigabitEthernet0/0.%s[ ]+([0-9\.]+)'% (vlan)
        customerIpAddress = re.search(customerIpPattern, self.deviceConfig)
        return customerIpAddress.group(1)
