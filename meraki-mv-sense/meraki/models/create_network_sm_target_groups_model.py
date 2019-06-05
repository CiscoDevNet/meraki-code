# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkSmTargetGroupsModel(object):

    """Implementation of the 'createNetworkSmTargetGroups' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of this target group
        scope (string): The scope and tag options of the target group. Comma
            separated values beginning with one of withAny, withAll,
            withoutAny, withoutAll, all, none, followed by tags

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "scope":'scope'
    }

    def __init__(self,
                 name=None,
                 scope=None,
                 additional_properties = {}):
        """Constructor for the CreateNetworkSmTargetGroupsModel class"""

        # Initialize members of the class
        self.name = name
        self.scope = scope

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
        scope = dictionary.get('scope')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   scope,
                   dictionary)


