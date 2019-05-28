# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule2Model(object):

    """Implementation of the 'Rule2' model.

    TODO: type model description here.

    Attributes:
        policy (PolicyEnum): 'Deny' traffic specified by this rule
        mtype (TypeEnum): Type of the L7 rule. One of: 'application',
            'applicationCategory', 'host', 'port', 'ipRange'
        value (string): The 'value' of what you want to block. Format of
            'value' varies depending on type of the rule. See sample request.
            The application categories and application ids can be retrieved
            from the the 'MX L7 application categories' endpoint. The
            countries follow the two-letter ISO 3166-1 alpha-2 format.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "policy":'policy',
        "mtype":'type',
        "value":'value'
    }

    def __init__(self,
                 policy=None,
                 mtype=None,
                 value=None,
                 additional_properties = {}):
        """Constructor for the Rule2Model class"""

        # Initialize members of the class
        self.policy = policy
        self.mtype = mtype
        self.value = value

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
        policy = dictionary.get('policy')
        mtype = dictionary.get('type')
        value = dictionary.get('value')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(policy,
                   mtype,
                   value,
                   dictionary)


