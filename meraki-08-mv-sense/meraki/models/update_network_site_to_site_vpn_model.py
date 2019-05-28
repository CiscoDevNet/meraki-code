# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.hub_model
import meraki.models.subnet_model

class UpdateNetworkSiteToSiteVpnModel(object):

    """Implementation of the 'updateNetworkSiteToSiteVpn' model.

    TODO: type model description here.

    Attributes:
        mode (string): The site-to-site VPN mode: hub, spoke, or none
        hubs (list of HubModel): The list of VPN hubs, in order of preference.
            In spoke mode, at least 1 hub is required.
        subnets (list of SubnetModel): The list of subnets and their VPN
            presence.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mode":'mode',
        "hubs":'hubs',
        "subnets":'subnets'
    }

    def __init__(self,
                 mode=None,
                 hubs=None,
                 subnets=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkSiteToSiteVpnModel class"""

        # Initialize members of the class
        self.mode = mode
        self.hubs = hubs
        self.subnets = subnets

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
        mode = dictionary.get('mode')
        hubs = None
        if dictionary.get('hubs') != None:
            hubs = list()
            for structure in dictionary.get('hubs'):
                hubs.append(meraki.models.hub_model.HubModel.from_dictionary(structure))
        subnets = None
        if dictionary.get('subnets') != None:
            subnets = list()
            for structure in dictionary.get('subnets'):
                subnets.append(meraki.models.subnet_model.SubnetModel.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(mode,
                   hubs,
                   subnets,
                   dictionary)


