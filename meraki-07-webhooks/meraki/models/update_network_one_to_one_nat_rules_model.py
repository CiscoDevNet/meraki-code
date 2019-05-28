# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.rule6_model

class UpdateNetworkOneToOneNatRulesModel(object):

    """Implementation of the 'updateNetworkOneToOneNatRules' model.

    TODO: type model description here.

    Attributes:
        rules (list of Rule6Model): An array of 1:1 nat rules

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rules":'rules'
    }

    def __init__(self,
                 rules=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkOneToOneNatRulesModel class"""

        # Initialize members of the class
        self.rules = rules

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
        rules = None
        if dictionary.get('rules') != None:
            rules = list()
            for structure in dictionary.get('rules'):
                rules.append(meraki.models.rule6_model.Rule6Model.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(rules,
                   dictionary)


