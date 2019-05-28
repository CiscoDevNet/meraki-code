# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class NetworkModel(object):

    """Implementation of the 'Network' model.

    TODO: type model description here.

    Attributes:
        id (string): The network ID
        access (string): The privilege of the dashboard administrator on the
            network

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "access":'access'
    }

    def __init__(self,
                 id=None,
                 access=None,
                 additional_properties = {}):
        """Constructor for the NetworkModel class"""

        # Initialize members of the class
        self.id = id
        self.access = access

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
        id = dictionary.get('id')
        access = dictionary.get('access')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   access,
                   dictionary)


