# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkVlansEnabledStateModel(object):

    """Implementation of the 'updateNetworkVlansEnabledState' model.

    TODO: type model description here.

    Attributes:
        enabled (bool): Boolean indicating whether to enable (true) or disable
            (false) VLANs for the network

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled":'enabled'
    }

    def __init__(self,
                 enabled=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkVlansEnabledStateModel class"""

        # Initialize members of the class
        self.enabled = enabled

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
        enabled = dictionary.get('enabled')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(enabled,
                   dictionary)


