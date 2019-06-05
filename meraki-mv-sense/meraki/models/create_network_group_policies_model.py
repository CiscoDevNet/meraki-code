# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.scheduling_model
import meraki.models.bandwidth_model

class CreateNetworkGroupPoliciesModel(object):

    """Implementation of the 'createNetworkGroupPolicies' model.

    TODO: type model description here.

    Attributes:
        name (string): The name for your group policy. Required.
        scheduling (SchedulingModel): The schedule for the group policy.
            Schedules are applied to days of the week.
        bandwidth (BandwidthModel): The bandwidth settings for clients bound
            to your group policy.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "scheduling":'scheduling',
        "bandwidth":'bandwidth'
    }

    def __init__(self,
                 name=None,
                 scheduling=None,
                 bandwidth=None,
                 additional_properties = {}):
        """Constructor for the CreateNetworkGroupPoliciesModel class"""

        # Initialize members of the class
        self.name = name
        self.scheduling = scheduling
        self.bandwidth = bandwidth

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
        scheduling = meraki.models.scheduling_model.SchedulingModel.from_dictionary(dictionary.get('scheduling')) if dictionary.get('scheduling') else None
        bandwidth = meraki.models.bandwidth_model.BandwidthModel.from_dictionary(dictionary.get('bandwidth')) if dictionary.get('bandwidth') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   scheduling,
                   bandwidth,
                   dictionary)


