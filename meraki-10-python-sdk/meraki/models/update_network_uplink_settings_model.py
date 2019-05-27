# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.bandwidth_limits2_model

class UpdateNetworkUplinkSettingsModel(object):

    """Implementation of the 'updateNetworkUplinkSettings' model.

    TODO: type model description here.

    Attributes:
        bandwidth_limits (BandwidthLimits2Model): A mapping of uplinks
            ('wan1', 'wan2' or 'cellular') to their bandwidth settings (be
            sure to check which uplinks are supported for your network).
            Bandwidth setting objects have the following structure

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bandwidth_limits":'bandwidthLimits'
    }

    def __init__(self,
                 bandwidth_limits=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkUplinkSettingsModel class"""

        # Initialize members of the class
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
        bandwidth_limits = meraki.models.bandwidth_limits2_model.BandwidthLimits2Model.from_dictionary(dictionary.get('bandwidthLimits')) if dictionary.get('bandwidthLimits') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(bandwidth_limits,
                   dictionary)


