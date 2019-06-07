# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkBluetoothSettingsModel(object):

    """Implementation of the 'updateNetworkBluetoothSettings' model.

    TODO: type model description here.

    Attributes:
        scanning_enabled (bool): Whether APs will scan for Bluetooth enabled
            clients. (true, false)
        advertising_enabled (bool): Whether APs will advertise beacons. (true,
            false)
        uuid (string): The UUID to be used in the beacon identifier.
        major_minor_assignment_mode (string): The way major and minor number
            should be assigned to nodes in the network. ('Unique',
            'Non-unique')
        major (int): The major number to be used in the beacon identifier.
            Only valid in 'Non-unique' mode.
        minor (int): The minor number to be used in the beacon identifier.
            Only valid in 'Non-unique' mode.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scanning_enabled":'scanningEnabled',
        "advertising_enabled":'advertisingEnabled',
        "uuid":'uuid',
        "major_minor_assignment_mode":'majorMinorAssignmentMode',
        "major":'major',
        "minor":'minor'
    }

    def __init__(self,
                 scanning_enabled=None,
                 advertising_enabled=None,
                 uuid=None,
                 major_minor_assignment_mode=None,
                 major=None,
                 minor=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkBluetoothSettingsModel class"""

        # Initialize members of the class
        self.scanning_enabled = scanning_enabled
        self.advertising_enabled = advertising_enabled
        self.uuid = uuid
        self.major_minor_assignment_mode = major_minor_assignment_mode
        self.major = major
        self.minor = minor

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
        scanning_enabled = dictionary.get('scanningEnabled')
        advertising_enabled = dictionary.get('advertisingEnabled')
        uuid = dictionary.get('uuid')
        major_minor_assignment_mode = dictionary.get('majorMinorAssignmentMode')
        major = dictionary.get('major')
        minor = dictionary.get('minor')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(scanning_enabled,
                   advertising_enabled,
                   uuid,
                   major_minor_assignment_mode,
                   major,
                   minor,
                   dictionary)


