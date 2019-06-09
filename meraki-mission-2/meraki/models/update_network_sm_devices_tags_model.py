# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSmDevicesTagsModel(object):

    """Implementation of the 'updateNetworkSmDevicesTags' model.

    TODO: type model description here.

    Attributes:
        wifi_macs (string): The wifiMacs of the devices to be modified.
        ids (string): The ids of the devices to be modified.
        serials (string): The serials of the devices to be modified.
        scope (string): The scope (one of all, none, withAny, withAll,
            withoutAny, or withoutAll) and a set of tags of the devices to be
            modified.
        tags (string): The tags to be added, deleted, or updated.
        update_action (string): One of add, delete, or update. Only devices
            that have been modified will be returned.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wifi_macs":'wifiMacs',
        "ids":'ids',
        "serials":'serials',
        "scope":'scope',
        "tags":'tags',
        "update_action":'updateAction'
    }

    def __init__(self,
                 wifi_macs=None,
                 ids=None,
                 serials=None,
                 scope=None,
                 tags=None,
                 update_action=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkSmDevicesTagsModel class"""

        # Initialize members of the class
        self.wifi_macs = wifi_macs
        self.ids = ids
        self.serials = serials
        self.scope = scope
        self.tags = tags
        self.update_action = update_action

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
        tags = dictionary.get('tags')
        update_action = dictionary.get('updateAction')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(wifi_macs,
                   ids,
                   serials,
                   scope,
                   tags,
                   update_action,
                   dictionary)


