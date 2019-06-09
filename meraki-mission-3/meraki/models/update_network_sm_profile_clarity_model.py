# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSmProfileClarityModel(object):

    """Implementation of the 'updateNetworkSmProfileClarity' model.

    TODO: type model description here.

    Attributes:
        name (string): optional: A new name for the profile
        scope (string): optional: A new scope for the profile (one of all,
            none, withAny, withAll, withoutAny, or withoutAll) and a set of
            tags of the devices to be assigned
        plugin_bundle_id (string): optional: The new bundle ID of the
            application
        filter_browsers (string): optional: Whether or not to enable browser
            traffic filtering (one of true, false).
        filter_sockets (string): optional: Whether or not to enable socket
            traffic filtering (one of true, false).
        vendor_config (string): optional: The specific VendorConfig to be
            passed to the filtering framework, as JSON. VendorConfig should be
            an array of objects, as: [ { "key": "some_key", type: "some_type",
            "value": "some_value" }, ... ]  type is one of manual_string,
            manual_int, manual_boolean, manual_choice, manual_multiselect,
            manual_list, auto_username, auto_email, auto_mac_address,
            auto_serial_number, auto_notes, auto_name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "scope":'scope',
        "plugin_bundle_id":'PluginBundleID',
        "filter_browsers":'FilterBrowsers',
        "filter_sockets":'FilterSockets',
        "vendor_config":'VendorConfig'
    }

    def __init__(self,
                 name=None,
                 scope=None,
                 plugin_bundle_id=None,
                 filter_browsers=None,
                 filter_sockets=None,
                 vendor_config=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkSmProfileClarityModel class"""

        # Initialize members of the class
        self.name = name
        self.scope = scope
        self.plugin_bundle_id = plugin_bundle_id
        self.filter_browsers = filter_browsers
        self.filter_sockets = filter_sockets
        self.vendor_config = vendor_config

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
        scope = dictionary.get('scope')
        plugin_bundle_id = dictionary.get('PluginBundleID')
        filter_browsers = dictionary.get('FilterBrowsers')
        filter_sockets = dictionary.get('FilterSockets')
        vendor_config = dictionary.get('VendorConfig')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   scope,
                   plugin_bundle_id,
                   filter_browsers,
                   filter_sockets,
                   vendor_config,
                   dictionary)


