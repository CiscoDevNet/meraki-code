# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkStaticRoutesModel(object):

    """Implementation of the 'createNetworkStaticRoutes' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the new static route
        subnet (string): The subnet of the static route
        gateway_ip (string): The gateway IP (next hop) of the static route

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "subnet":'subnet',
        "gateway_ip":'gatewayIp'
    }

    def __init__(self,
                 name=None,
                 subnet=None,
                 gateway_ip=None,
                 additional_properties = {}):
        """Constructor for the CreateNetworkStaticRoutesModel class"""

        # Initialize members of the class
        self.name = name
        self.subnet = subnet
        self.gateway_ip = gateway_ip

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
        gateway_ip = dictionary.get('gatewayIp')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   subnet,
                   gateway_ip,
                   dictionary)


