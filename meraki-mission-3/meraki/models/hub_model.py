# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class HubModel(object):

    """Implementation of the 'Hub' model.

    TODO: type model description here.

    Attributes:
        hub_id (string): The network ID of the hub.
        use_default_route (bool): Only valid in 'spoke' mode. Indicates
            whether default route traffic should be sent to this hub.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hub_id":'hubId',
        "use_default_route":'useDefaultRoute'
    }

    def __init__(self,
                 hub_id=None,
                 use_default_route=None,
                 additional_properties = {}):
        """Constructor for the HubModel class"""

        # Initialize members of the class
        self.hub_id = hub_id
        self.use_default_route = use_default_route

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
        hub_id = dictionary.get('hubId')
        use_default_route = dictionary.get('useDefaultRoute')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(hub_id,
                   use_default_route,
                   dictionary)


