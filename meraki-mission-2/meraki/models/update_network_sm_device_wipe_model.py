# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSmDeviceWipeModel(object):

    """Implementation of the 'updateNetworkSmDeviceWipe' model.

    TODO: type model description here.

    Attributes:
        wifi_mac (string): The wifiMac of the device to be wiped.
        id (string): The id of the device to be wiped.
        serial (string): The serial of the device to be wiped.
        pin (string): The pin number (a six digit value) for wiping a macOS
            device. Required only for macOS devices.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wifi_mac":'wifiMac',
        "id":'id',
        "serial":'serial',
        "pin":'pin'
    }

    def __init__(self,
                 wifi_mac=None,
                 id=None,
                 serial=None,
                 pin=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkSmDeviceWipeModel class"""

        # Initialize members of the class
        self.wifi_mac = wifi_mac
        self.id = id
        self.serial = serial
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
        wifi_mac = dictionary.get('wifiMac')
        id = dictionary.get('id')
        serial = dictionary.get('serial')
        pin = dictionary.get('pin')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(wifi_mac,
                   id,
                   serial,
                   pin,
                   dictionary)


