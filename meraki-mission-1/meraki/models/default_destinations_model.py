# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class DefaultDestinationsModel(object):

    """Implementation of the 'DefaultDestinations' model.

    The network_wide destinations for all alerts on the network.

    Attributes:
        emails (list of string): A list of emails that will recieve the
            alert(s).
        all_admins (bool): If true, then all network admins will receive
            emails.
        snmp (bool): If true, then an SNMP trap will be sent if there is an
            SNMP trap server configured for this network.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "emails":'emails',
        "all_admins":'allAdmins',
        "snmp":'snmp'
    }

    def __init__(self,
                 emails=None,
                 all_admins=None,
                 snmp=None,
                 additional_properties = {}):
        """Constructor for the DefaultDestinationsModel class"""

        # Initialize members of the class
        self.emails = emails
        self.all_admins = all_admins
        self.snmp = snmp

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
        emails = dictionary.get('emails')
        all_admins = dictionary.get('allAdmins')
        snmp = dictionary.get('snmp')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(emails,
                   all_admins,
                   snmp,
                   dictionary)


