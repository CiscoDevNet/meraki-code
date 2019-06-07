# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSmDevicesLockModel(object):

    """Implementation of the 'updateNetworkSmDevicesLock' model.

    TODO: type model description here.

    Attributes:
        wifi_macs (string): The wifiMacs of the devices to be locked.
        ids (string): The ids of the devices to be locked.
        serials (string): The serials of the devices to be locked.
        scope (string): The scope (one of all, none, withAny, withAll,
            withoutAny, or withoutAll) and a set of tags of the devices to be
            wiped.
        pin (string): The pin number for locking macOS devices (a six digit
            number). Required only for macOS devices.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wifi_macs":'wifiMacs',
        "ids":'ids',
        "serials":'serials',
        "scope":'scope',
        "pin":'pin'
    }

    def __init__(self,
                 wifi_macs=None,
                 ids=None,
                 serials=None,
                 scope=None,
                 pin=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkSmDevicesLockModel class"""

        # Initialize members of the class
        self.wifi_macs = wifi_macs
        self.ids = ids
        self.serials = serials
        self.scope = scope
        self.pin = pin

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
        pin = dictionary.get('pin')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(wifi_macs,
                   ids,
                   serials,
                   scope,
                   pin,
                   dictionary)


