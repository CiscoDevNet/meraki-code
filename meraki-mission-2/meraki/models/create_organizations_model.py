# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateOrganizationsModel(object):

    """Implementation of the 'createOrganizations' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the organization

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name'
    }

    def __init__(self,
                 name=None,
                 additional_properties = {}):
        """Constructor for the CreateOrganizationsModel class"""

        # Initialize members of the class
        self.name = name

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
        name = dictionary.get('name')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   dictionary)


