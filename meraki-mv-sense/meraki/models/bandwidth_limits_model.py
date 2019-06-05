# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BandwidthLimitsModel(object):

    """Implementation of the 'BandwidthLimits' model.

    The bandwidth limits object, specifying upload and download speed for
    clients bound to the group policy. These are only enforced if 'settings'
    is set to 'custom'.

    Attributes:
        limit_up (int): The maximum upload limit (integer, in Kbps). null
            indicates no limit
        limit_down (int): The maximum download limit (integer, in Kbps). null
            indicates no limit

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "limit_up":'limitUp',
        "limit_down":'limitDown'
    }

    def __init__(self,
                 limit_up=None,
                 limit_down=None,
                 additional_properties = {}):
        """Constructor for the BandwidthLimitsModel class"""

        # Initialize members of the class
        self.limit_up = limit_up
        self.limit_down = limit_down

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
        limit_up = dictionary.get('limitUp')
        limit_down = dictionary.get('limitDown')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(limit_up,
                   limit_down,
                   dictionary)


