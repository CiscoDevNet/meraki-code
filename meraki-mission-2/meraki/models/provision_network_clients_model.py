# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ProvisionNetworkClientsModel(object):

    """Implementation of the 'provisionNetworkClients' model.

    TODO: type model description here.

    Attributes:
        mac (string): The MAC address of the client. Required.
        name (string): The display name for the client. Optional. Limited to
            255 bytes.
        device_policy (string): The policy to apply to the specified client.
            Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group policy'.
            Required.
        group_policy_id (string): The ID of the desired group policy to apply
            to the client. Required if 'devicePolicy' is set to "Group
            policy". Otherwise this is ignored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mac":'mac',
        "name":'name',
        "device_policy":'devicePolicy',
        "group_policy_id":'groupPolicyId'
    }

    def __init__(self,
                 mac=None,
                 name=None,
                 device_policy=None,
                 group_policy_id=None,
                 additional_properties = {}):
        """Constructor for the ProvisionNetworkClientsModel class"""

        # Initialize members of the class
        self.mac = mac
        self.name = name
        self.device_policy = device_policy
        self.group_policy_id = group_policy_id

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
        mac = dictionary.get('mac')
        name = dictionary.get('name')
        device_policy = dictionary.get('devicePolicy')
        group_policy_id = dictionary.get('groupPolicyId')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(mac,
                   name,
                   device_policy,
                   group_policy_id,
                   dictionary)


