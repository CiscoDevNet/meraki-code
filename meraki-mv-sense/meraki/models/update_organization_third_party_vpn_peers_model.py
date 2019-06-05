# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.peer_model

class UpdateOrganizationThirdPartyVPNPeersModel(object):

    """Implementation of the 'updateOrganizationThirdPartyVPNPeers' model.

    TODO: type model description here.

    Attributes:
        peers (list of PeerModel): The list of VPN peers

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "peers":'peers'
    }

    def __init__(self,
                 peers=None,
                 additional_properties = {}):
        """Constructor for the UpdateOrganizationThirdPartyVPNPeersModel class"""

        # Initialize members of the class
        self.peers = peers

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
        peers = None
        if dictionary.get('peers') != None:
            peers = list()
            for structure in dictionary.get('peers'):
                peers.append(meraki.models.peer_model.PeerModel.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(peers,
                   dictionary)


