# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.rule4_model

class UpdateNetworkSsidL3FirewallRulesModel(object):

    """Implementation of the 'updateNetworkSsidL3FirewallRules' model.

    TODO: type model description here.

    Attributes:
        rules (list of Rule4Model): An ordered array of the firewall rules for
            this SSID (not including the local LAN access rule or the default
            rule)
        allow_lan_access (bool): Allow wireless client access to local LAN
            (boolean value - true allows access and false denies access)
            (optional)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rules":'rules',
        "allow_lan_access":'allowLanAccess'
    }

    def __init__(self,
                 rules=None,
                 allow_lan_access=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkSsidL3FirewallRulesModel class"""

        # Initialize members of the class
        self.rules = rules
        self.allow_lan_access = allow_lan_access

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
                rules.append(meraki.models.rule4_model.Rule4Model.from_dictionary(structure))
        allow_lan_access = dictionary.get('allowLanAccess')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(rules,
                   allow_lan_access,
                   dictionary)


