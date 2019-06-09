# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ApTagsAndVlanIdModel(object):

    """Implementation of the 'ApTagsAndVlanId' model.

    TODO: type model description here.

    Attributes:
        tags (string): Comma-separated list of AP tags
        vlan_id (string): Numerical identifier that is assigned to the VLAN

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tags":'tags',
        "vlan_id":'vlanId'
    }

    def __init__(self,
                 tags=None,
                 vlan_id=None,
                 additional_properties = {}):
        """Constructor for the ApTagsAndVlanIdModel class"""

        # Initialize members of the class
        self.tags = tags
        self.vlan_id = vlan_id

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
        tags = dictionary.get('tags')
        vlan_id = dictionary.get('vlanId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(tags,
                   vlan_id,
                   dictionary)


