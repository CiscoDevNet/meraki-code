# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class SsidsModel(object):

    """Implementation of the 'Ssids' model.

    The target SSIDs. For each SSID where isAuthorized is true, the expiration
    time will automatically be set according to the SSID's splash frequency.

    Attributes:
        is_authorized (string): New authorization status for SSID (true,
            false).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_authorized":'isAuthorized'
    }

    def __init__(self,
                 is_authorized=None,
                 additional_properties = {}):
        """Constructor for the SsidsModel class"""

        # Initialize members of the class
        self.is_authorized = is_authorized

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
        is_authorized = dictionary.get('isAuthorized')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(is_authorized,
                   dictionary)


