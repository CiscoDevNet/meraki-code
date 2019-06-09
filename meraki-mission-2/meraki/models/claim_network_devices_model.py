# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ClaimNetworkDevicesModel(object):

    """Implementation of the 'claimNetworkDevices' model.

    TODO: type model description here.

    Attributes:
        serial (string): The serial of a device

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "serial":'serial'
    }

    def __init__(self,
                 serial=None,
                 additional_properties = {}):
        """Constructor for the ClaimNetworkDevicesModel class"""

        # Initialize members of the class
        self.serial = serial

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
        serial = dictionary.get('serial')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(serial,
                   dictionary)


