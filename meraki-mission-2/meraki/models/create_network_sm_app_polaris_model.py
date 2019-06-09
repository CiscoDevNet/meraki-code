# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkSmAppPolarisModel(object):

    """Implementation of the 'createNetworkSmAppPolaris' model.

    TODO: type model description here.

    Attributes:
        scope (string): The scope (one of all, none, automatic, withAny,
            withAll, withoutAny, or withoutAll) and a set of tags of the
            devices to be assigned
        manifest_url (string): The manifest URL of the Polaris app (one of
            manifestUrl and bundleId must be provided)
        bundle_id (string): The bundleId of the Polaris app (one of
            manifestUrl and bundleId must be provided)
        prevent_auto_install (string): (optional) Whether or not SM should
            auto-install this app (one of true or false). False by default.
        uses_vpp (string): (optional) Whether or not the app should use VPP by
            device assignment (one of true or false). False by default.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scope":'scope',
        "manifest_url":'manifestUrl',
        "bundle_id":'bundleId',
        "prevent_auto_install":'preventAutoInstall',
        "uses_vpp":'usesVPP'
    }

    def __init__(self,
                 scope=None,
                 manifest_url=None,
                 bundle_id=None,
                 prevent_auto_install=None,
                 uses_vpp=None,
                 additional_properties = {}):
        """Constructor for the CreateNetworkSmAppPolarisModel class"""

        # Initialize members of the class
        self.scope = scope
        self.manifest_url = manifest_url
        self.bundle_id = bundle_id
        self.prevent_auto_install = prevent_auto_install
        self.uses_vpp = uses_vpp

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
        scope = dictionary.get('scope')
        manifest_url = dictionary.get('manifestUrl')
        bundle_id = dictionary.get('bundleId')
        prevent_auto_install = dictionary.get('preventAutoInstall')
        uses_vpp = dictionary.get('usesVPP')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(scope,
                   manifest_url,
                   bundle_id,
                   prevent_auto_install,
                   uses_vpp,
                   dictionary)


