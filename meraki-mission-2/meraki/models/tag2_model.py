# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Tag2Model(object):

    """Implementation of the 'Tag2' model.

    TODO: type model description here.

    Attributes:
        tag (string): The name of the tag
        access (string): The privilege of the SAML administrator on the tag

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tag":'tag',
        "access":'access'
    }

    def __init__(self,
                 tag=None,
                 access=None,
                 additional_properties = {}):
        """Constructor for the Tag2Model class"""

        # Initialize members of the class
        self.tag = tag
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
        tag = dictionary.get('tag')
        access = dictionary.get('access')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(tag,
                   access,
                   dictionary)


