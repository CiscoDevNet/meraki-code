# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.server_model

class UpdateNetworkSyslogServersModel(object):

    """Implementation of the 'updateNetworkSyslogServers' model.

    TODO: type model description here.

    Attributes:
        servers (list of ServerModel): A list of the syslog servers for this
            network

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "servers":'servers'
    }

    def __init__(self,
                 servers=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkSyslogServersModel class"""

        # Initialize members of the class
        self.servers = servers

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
        servers = None
        if dictionary.get('servers') != None:
            servers = list()
            for structure in dictionary.get('servers'):
                servers.append(meraki.models.server_model.ServerModel.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(servers,
                   dictionary)


