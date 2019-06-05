# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkClientPolicyModel(object):

    """Implementation of the 'updateNetworkClientPolicy' model.

    TODO: type model description here.

    Attributes:
        device_policy (string): The group policy (Whitelisted, Blocked,
            Normal, Group policy)
        group_policy_id (string): [optional] If devicePolicy param is set to
            'Group policy' this param is used to specify the group ID.
        timespan (string): The timespan for which clients will be fetched.
            Must be in seconds and less than or equal to a month (2592000
            seconds).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_policy":'devicePolicy',
        "group_policy_id":'groupPolicyId',
        "timespan":'timespan'
    }

    def __init__(self,
                 device_policy=None,
                 group_policy_id=None,
                 timespan=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkClientPolicyModel class"""

        # Initialize members of the class
        self.device_policy = device_policy
        self.group_policy_id = group_policy_id
        self.timespan = timespan

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
        device_policy = dictionary.get('devicePolicy')
        group_policy_id = dictionary.get('groupPolicyId')
        timespan = dictionary.get('timespan')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(device_policy,
                   group_policy_id,
                   timespan,
                   dictionary)


