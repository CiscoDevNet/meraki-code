# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.bandwidth_limits_model

class BandwidthModel(object):

    """Implementation of the 'Bandwidth' model.

    The bandwidth settings for clients bound to your group policy.

    Attributes:
        settings (string): How bandwidth limits are enforced. Can be 'network
            default', 'ignore' or 'custom'.
        bandwidth_limits (BandwidthLimitsModel): The bandwidth limits object,
            specifying upload and download speed for clients bound to the
            group policy. These are only enforced if 'settings' is set to
            'custom'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "settings":'settings',
        "bandwidth_limits":'bandwidthLimits'
    }

    def __init__(self,
                 settings=None,
                 bandwidth_limits=None,
                 additional_properties = {}):
        """Constructor for the BandwidthModel class"""

        # Initialize members of the class
        self.settings = settings
        self.bandwidth_limits = bandwidth_limits

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
        settings = dictionary.get('settings')
        bandwidth_limits = meraki.models.bandwidth_limits_model.BandwidthLimitsModel.from_dictionary(dictionary.get('bandwidthLimits')) if dictionary.get('bandwidthLimits') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(settings,
                   bandwidth_limits,
                   dictionary)


