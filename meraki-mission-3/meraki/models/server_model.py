# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ServerModel(object):

    """Implementation of the 'Server' model.

    TODO: type model description here.

    Attributes:
        host (string): The IP address of the syslog server
        port (int): The port of the syslog server
        roles (list of string): A list of roles for the syslog server. Options
            (case-insensitive): 'Wireless event log', 'Appliance event log',
            'Switch event log', 'Air Marshal events', 'Flows', 'URLs', 'IDS
            alerts', 'Security events'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "host":'host',
        "port":'port',
        "roles":'roles'
    }

    def __init__(self,
                 host=None,
                 port=None,
                 roles=None,
                 additional_properties = {}):
        """Constructor for the ServerModel class"""

        # Initialize members of the class
        self.host = host
        self.port = port
        self.roles = roles

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
        host = dictionary.get('host')
        port = dictionary.get('port')
        roles = dictionary.get('roles')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(host,
                   port,
                   roles,
                   dictionary)


