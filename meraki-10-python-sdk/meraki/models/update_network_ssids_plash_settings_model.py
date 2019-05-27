# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSsidsPlashSettingsModel(object):

    """Implementation of the 'updateNetworkSsidSplashSettings' model.

    TODO: type model description here.

    Attributes:
        splash_url (string): The custom splash URL of the click-through splash
            page. Optional. Note that the URL can be configured without
            necessarily being used. In order to enable the custom URL, see
            'useSplashUrl'
        use_splash_url (bool): Boolean indicating whether the user will be
            redirected to the custom splash url. A custom splash URL must be
            set if this is true. Optional. Note that depending on your SSID's
            access control settings, it may not be possible to use the custom
            splash URL.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "splash_url":'splashUrl',
        "use_splash_url":'useSplashUrl'
    }

    def __init__(self,
                 splash_url=None,
                 use_splash_url=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkSsidsPlashSettingsModel class"""

        # Initialize members of the class
        self.splash_url = splash_url
        self.use_splash_url = use_splash_url

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
        splash_url = dictionary.get('splashUrl')
        use_splash_url = dictionary.get('useSplashUrl')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(splash_url,
                   use_splash_url,
                   dictionary)


