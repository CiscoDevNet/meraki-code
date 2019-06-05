# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkFirewalledServiceModel(object):

    """Implementation of the 'updateNetworkFirewalledService' model.

    TODO: type model description here.

    Attributes:
        access (string): A string indicating the rule for which IPs are
            allowed to use the specified service. Acceptable values are
            "blocked" (no remote IPs can access the service), "restricted"
            (only whitelisted IPs can access the service), and "unrestriced"
            (any remote IP can access the service). This field is required
        allowed_ips (list of string): An array of whitelisted IPs that can
            access the service. This field is required if "access" is set to
            "restricted". Otherwise this field is ignored

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access":'access',
        "allowed_ips":'allowedIps'
    }

    def __init__(self,
                 access=None,
                 allowed_ips=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkFirewalledServiceModel class"""

        # Initialize members of the class
        self.access = access
        self.allowed_ips = allowed_ips

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
        access = dictionary.get('access')
        allowed_ips = dictionary.get('allowedIps')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(access,
                   allowed_ips,
                   dictionary)


