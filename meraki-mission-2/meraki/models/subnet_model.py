# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class SubnetModel(object):

    """Implementation of the 'Subnet' model.

    TODO: type model description here.

    Attributes:
        local_subnet (string): The CIDR notation subnet used within the VPN
        use_vpn (bool): Indicates the presence of the subnet in the VPN

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "local_subnet":'localSubnet',
        "use_vpn":'useVpn'
    }

    def __init__(self,
                 local_subnet=None,
                 use_vpn=None,
                 additional_properties = {}):
        """Constructor for the SubnetModel class"""

        # Initialize members of the class
        self.local_subnet = local_subnet
        self.use_vpn = use_vpn

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
        local_subnet = dictionary.get('localSubnet')
        use_vpn = dictionary.get('useVpn')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(local_subnet,
                   use_vpn,
                   dictionary)


