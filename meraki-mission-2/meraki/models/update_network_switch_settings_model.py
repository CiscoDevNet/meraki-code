# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.power_exception_model

class UpdateNetworkSwitchSettingsModel(object):

    """Implementation of the 'updateNetworkSwitchSettings' model.

    TODO: type model description here.

    Attributes:
        use_combined_power (bool): The behavior of secondary power supplies on
            supported devices ("redundant", "combined")
        power_exceptions (list of PowerExceptionModel): Exceptions on a per
            switch basis to "useCombinedPower"

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "use_combined_power":'useCombinedPower',
        "power_exceptions":'powerExceptions'
    }

    def __init__(self,
                 use_combined_power=None,
                 power_exceptions=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkSwitchSettingsModel class"""

        # Initialize members of the class
        self.use_combined_power = use_combined_power
        self.power_exceptions = power_exceptions

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
        use_combined_power = dictionary.get('useCombinedPower')
        power_exceptions = None
        if dictionary.get('powerExceptions') != None:
            power_exceptions = list()
            for structure in dictionary.get('powerExceptions'):
                power_exceptions.append(meraki.models.power_exception_model.PowerExceptionModel.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(use_combined_power,
                   power_exceptions,
                   dictionary)


