# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.reserved_ip_range_model
import meraki.models.dhcp_option_model

class UpdateNetworkVlanModel(object):

    """Implementation of the 'updateNetworkVlan' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the VLAN
        subnet (string): The subnet of the VLAN
        appliance_ip (string): The local IP of the appliance on the VLAN
        vpn_nat_subnet (string): The translated VPN subnet if VPN and VPN
            subnet translation are enabled on the VLAN
        dhcp_handling (string): The appliance's handling of DHCP requests on
            this VLAN. One of: "Run a DHCP server", "Relay DHCP to another
            server", or "Do not respond to DHCP requests"
        dhcp_relay_server_ips (list of string): The IPs of the DHCP servers
            that DHCP requests should be relayed to
        dhcp_lease_time (string): The term of DHCP leases if the appliance is
            running a DHCP server on this VLAN. One of: "30 minutes", "1
            hour", "4 hours", "12 hours", "1 day", "1 week".
        dhcp_boot_options_enabled (bool): Use DHCP boot options specified in
            other properties
        dhcp_boot_next_server (string): DHCP boot option to direct boot
            clients to the server to load the boot file from
        dhcp_boot_filename (string): DHCP boot option for boot filename
        fixed_ip_assignments (object): The DHCP fixed IP assignments on the
            VLAN. This should be an object that contains mappings from MAC
            addresses to objects that themselves each contain "ip" and "name"
            string fields. See the sample request/response for more details.
        reserved_ip_ranges (list of ReservedIpRangeModel): The DHCP reserved
            IP ranges on the VLAN
        dns_nameservers (string): The DNS nameservers used for DHCP responses,
            either "upstream_dns", "google_dns", "opendns", or a newline
            seperated string of IP addresses or domain names
        dhcp_options (list of DhcpOptionModel): The list of DHCP options that
            will be included in DHCP responses. Each object in the list should
            have "code", "type", and "value" properties.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "subnet":'subnet',
        "appliance_ip":'applianceIp',
        "vpn_nat_subnet":'vpnNatSubnet',
        "dhcp_handling":'dhcpHandling',
        "dhcp_relay_server_ips":'dhcpRelayServerIps',
        "dhcp_lease_time":'dhcpLeaseTime',
        "dhcp_boot_options_enabled":'dhcpBootOptionsEnabled',
        "dhcp_boot_next_server":'dhcpBootNextServer',
        "dhcp_boot_filename":'dhcpBootFilename',
        "fixed_ip_assignments":'fixedIpAssignments',
        "reserved_ip_ranges":'reservedIpRanges',
        "dns_nameservers":'dnsNameservers',
        "dhcp_options":'dhcpOptions'
    }

    def __init__(self,
                 name=None,
                 subnet=None,
                 appliance_ip=None,
                 vpn_nat_subnet=None,
                 dhcp_handling=None,
                 dhcp_relay_server_ips=None,
                 dhcp_lease_time=None,
                 dhcp_boot_options_enabled=None,
                 dhcp_boot_next_server=None,
                 dhcp_boot_filename=None,
                 fixed_ip_assignments=None,
                 reserved_ip_ranges=None,
                 dns_nameservers=None,
                 dhcp_options=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkVlanModel class"""

        # Initialize members of the class
        self.name = name
        self.subnet = subnet
        self.appliance_ip = appliance_ip
        self.vpn_nat_subnet = vpn_nat_subnet
        self.dhcp_handling = dhcp_handling
        self.dhcp_relay_server_ips = dhcp_relay_server_ips
        self.dhcp_lease_time = dhcp_lease_time
        self.dhcp_boot_options_enabled = dhcp_boot_options_enabled
        self.dhcp_boot_next_server = dhcp_boot_next_server
        self.dhcp_boot_filename = dhcp_boot_filename
        self.fixed_ip_assignments = fixed_ip_assignments
        self.reserved_ip_ranges = reserved_ip_ranges
        self.dns_nameservers = dns_nameservers
        self.dhcp_options = dhcp_options

        # Add additional model properties to the instance
        self.additional_properties = additional_properties


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get('name')
        subnet = dictionary.get('subnet')
        appliance_ip = dictionary.get('applianceIp')
        vpn_nat_subnet = dictionary.get('vpnNatSubnet')
        dhcp_handling = dictionary.get('dhcpHandling')
        dhcp_relay_server_ips = dictionary.get('dhcpRelayServerIps')
        dhcp_lease_time = dictionary.get('dhcpLeaseTime')
        dhcp_boot_options_enabled = dictionary.get('dhcpBootOptionsEnabled')
        dhcp_boot_next_server = dictionary.get('dhcpBootNextServer')
        dhcp_boot_filename = dictionary.get('dhcpBootFilename')
        fixed_ip_assignments = dictionary.get('fixedIpAssignments')
        reserved_ip_ranges = None
        if dictionary.get('reservedIpRanges') != None:
            reserved_ip_ranges = list()
            for structure in dictionary.get('reservedIpRanges'):
                reserved_ip_ranges.append(meraki.models.reserved_ip_range_model.ReservedIpRangeModel.from_dictionary(structure))
        dns_nameservers = dictionary.get('dnsNameservers')
        dhcp_options = None
        if dictionary.get('dhcpOptions') != None:
            dhcp_options = list()
            for structure in dictionary.get('dhcpOptions'):
                dhcp_options.append(meraki.models.dhcp_option_model.DhcpOptionModel.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   subnet,
                   appliance_ip,
                   vpn_nat_subnet,
                   dhcp_handling,
                   dhcp_relay_server_ips,
                   dhcp_lease_time,
                   dhcp_boot_options_enabled,
                   dhcp_boot_next_server,
                   dhcp_boot_filename,
                   fixed_ip_assignments,
                   reserved_ip_ranges,
                   dns_nameservers,
                   dhcp_options,
                   dictionary)


