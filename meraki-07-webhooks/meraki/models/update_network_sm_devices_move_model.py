# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSmDevicesMoveModel(object):

    """Implementation of the 'updateNetworkSmDevicesMove' model.

    TODO: type model description here.

    Attributes:
        wifi_macs (string): The wifiMacs of the devices to be moved.
        ids (string): The ids of the devices to be moved.
        serials (string): The serials of the devices to be moved.
        scope (string): The scope (one of all, none, withAny, withAll,
            withoutAny, or withoutAll) and a set of tags of the devices to be
            moved.
        new_network (string): The new network to which the devices will be
            moved.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wifi_macs":'wifiMacs',
        "ids":'ids',
        "serials":'serials',
        "scope":'scope',
        "new_network":'newNetwork'
    }

    def __init__(self,
                 wifi_macs=None,
                 ids=None,
                 serials=None,
                 scope=None,
                 new_network=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkSmDevicesMoveModel class"""

        # Initialize members of the class
        self.wifi_macs = wifi_macs
        self.ids = ids
        self.serials = serials
        self.scope = scope
        self.new_network = new_network

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
        wifi_macs = dictionary.get('wifiMacs')
        ids = dictionary.get('ids')
        serials = dictionary.get('serials')
        scope = dictionary.get('scope')
        new_network = dictionary.get('newNetwork')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(wifi_macs,
                   ids,
                   serials,
                   scope,
                   new_network,
                   dictionary)


