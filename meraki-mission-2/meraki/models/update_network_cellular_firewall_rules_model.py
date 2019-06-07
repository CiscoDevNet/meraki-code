# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.rule_model

class UpdateNetworkCellularFirewallRulesModel(object):

    """Implementation of the 'updateNetworkCellularFirewallRules' model.

    TODO: type model description here.

    Attributes:
        rules (list of RuleModel): An ordered array of the firewall rules (not
            including the default rule)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rules":'rules'
    }

    def __init__(self,
                 rules=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkCellularFirewallRulesModel class"""

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
                rules.append(meraki.models.rule_model.RuleModel.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(rules,
                   dictionary)


