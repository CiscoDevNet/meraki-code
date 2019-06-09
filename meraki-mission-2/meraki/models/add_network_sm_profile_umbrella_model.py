# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class AddNetworkSmProfileUmbrellaModel(object):

    """Implementation of the 'addNetworkSmProfileUmbrella' model.

    TODO: type model description here.

    Attributes:
        app_bundle_identifier (string): The bundle ID of the application,
            defaults to com.cisco.ciscosecurity.app
        provider_bundle_identifier (string): The bundle ID of the provider,
            defaults to com.cisco.ciscosecurity.app.CiscoUmbrella
        provider_configuration (string): The specific ProviderConfiguration to
            be passed to the filtering framework, as JSON.
            ProviderConfiguration should be an array of objects, as: [ {
            "key": "some_key", type: "some_type", "value": "some_value" }, ...
            ]  type is one of manual_string, manual_int, manual_boolean,
            manual_choice, manual_multiselect, manual_list, auto_username,
            auto_email, auto_mac_address, auto_serial_number, auto_notes,
            auto_name
        uses_cert (string): Whether the certificate should be attached to this
            profile (one of true, false). False by default.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_bundle_identifier":'AppBundleIdentifier',
        "provider_bundle_identifier":'ProviderBundleIdentifier',
        "provider_configuration":'ProviderConfiguration',
        "uses_cert":'usesCert'
    }

    def __init__(self,
                 app_bundle_identifier=None,
                 provider_bundle_identifier=None,
                 provider_configuration=None,
                 uses_cert=None,
                 additional_properties = {}):
        """Constructor for the AddNetworkSmProfileUmbrellaModel class"""

        # Initialize members of the class
        self.app_bundle_identifier = app_bundle_identifier
        self.provider_bundle_identifier = provider_bundle_identifier
        self.provider_configuration = provider_configuration
        self.uses_cert = uses_cert

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
        app_bundle_identifier = dictionary.get('AppBundleIdentifier')
        provider_bundle_identifier = dictionary.get('ProviderBundleIdentifier')
        provider_configuration = dictionary.get('ProviderConfiguration')
        uses_cert = dictionary.get('usesCert')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(app_bundle_identifier,
                   provider_bundle_identifier,
                   provider_configuration,
                   uses_cert,
                   dictionary)


