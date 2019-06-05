# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ClaimOrganizationModel(object):

    """Implementation of the 'claimOrganization' model.

    TODO: type model description here.

    Attributes:
        order (string): The order number that should be claimed
        serial (string): The serial of the device that should be claimed
        license_key (string): The license key that should be claimed
        license_mode (string): Either 'renew' or 'addDevices'. 'addDevices'
            will increase the license limit, while 'renew' will extend the
            amount of time until expiration. This parameter is required when
            claiming by licenseKey. Please see <a target='_blank'
            href='https://documentation.meraki.com/zGeneral_Administration/Lice
            nsing/Adding_an_Enterprise_license_to_an_existing_Dashboard_account
            '>this article</a> for more information.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "order":'order',
        "serial":'serial',
        "license_key":'licenseKey',
        "license_mode":'licenseMode'
    }

    def __init__(self,
                 order=None,
                 serial=None,
                 license_key=None,
                 license_mode=None,
                 additional_properties = {}):
        """Constructor for the ClaimOrganizationModel class"""

        # Initialize members of the class
        self.order = order
        self.serial = serial
        self.license_key = license_key
        self.license_mode = license_mode

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
        order = dictionary.get('order')
        serial = dictionary.get('serial')
        license_key = dictionary.get('licenseKey')
        license_mode = dictionary.get('licenseMode')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(order,
                   serial,
                   license_key,
                   license_mode,
                   dictionary)


