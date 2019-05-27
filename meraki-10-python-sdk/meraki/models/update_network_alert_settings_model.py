# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.default_destinations_model
import meraki.models.alert_model

class UpdateNetworkAlertSettingsModel(object):

    """Implementation of the 'updateNetworkAlertSettings' model.

    TODO: type model description here.

    Attributes:
        default_destinations (DefaultDestinationsModel): The network_wide
            destinations for all alerts on the network.
        alerts (list of AlertModel): Alert-specific configuration for each
            type. Only alerts that pertain to the network can be updated.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_destinations":'defaultDestinations',
        "alerts":'alerts'
    }

    def __init__(self,
                 default_destinations=None,
                 alerts=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkAlertSettingsModel class"""

        # Initialize members of the class
        self.default_destinations = default_destinations
        self.alerts = alerts

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
        default_destinations = meraki.models.default_destinations_model.DefaultDestinationsModel.from_dictionary(dictionary.get('defaultDestinations')) if dictionary.get('defaultDestinations') else None
        alerts = None
        if dictionary.get('alerts') != None:
            alerts = list()
            for structure in dictionary.get('alerts'):
                alerts.append(meraki.models.alert_model.AlertModel.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(default_destinations,
                   alerts,
                   dictionary)


