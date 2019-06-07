# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkVlansModel(object):

    """Implementation of the 'createNetworkVlans' model.

    TODO: type model description here.

    Attributes:
        id (string): The VLAN ID of the new VLAN (must be between 1 and 4094)
        name (string): The name of the new VLAN
        subnet (string): The subnet of the VLAN
        appliance_ip (string): The local IP of the appliance on the VLAN

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "subnet":'subnet',
        "appliance_ip":'applianceIp'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 subnet=None,
                 appliance_ip=None,
                 additional_properties = {}):
        """Constructor for the CreateNetworkVlansModel class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.subnet = subnet
        self.appliance_ip = appliance_ip

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
        id = dictionary.get('id')
        name = dictionary.get('name')
        subnet = dictionary.get('subnet')
        appliance_ip = dictionary.get('applianceIp')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   subnet,
                   appliance_ip,
                   dictionary)


