# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkHttpServersModel(object):

    """Implementation of the 'createNetworkHttpServers' model.

    TODO: type model description here.

    Attributes:
        name (string): A name for easy reference to the HTTP server
        url (string): The URL of the HTTP server
        shared_secret (string): A shared secret that will be included in POSTs
            sent to the HTTP server. This secret can be used to verify that
            the request was sent by Meraki.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "url":'url',
        "shared_secret":'sharedSecret'
    }

    def __init__(self,
                 name=None,
                 url=None,
                 shared_secret=None,
                 additional_properties = {}):
        """Constructor for the CreateNetworkHttpServersModel class"""

        # Initialize members of the class
        self.name = name
        self.url = url
        self.shared_secret = shared_secret

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
        name = dictionary.get('name')
        url = dictionary.get('url')
        shared_secret = dictionary.get('sharedSecret')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   url,
                   shared_secret,
                   dictionary)


