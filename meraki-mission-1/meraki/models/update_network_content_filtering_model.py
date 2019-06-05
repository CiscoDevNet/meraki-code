# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkContentFilteringModel(object):

    """Implementation of the 'updateNetworkContentFiltering' model.

    TODO: type model description here.

    Attributes:
        allowed_url_patterns (list of string): A whitelist of URL patterns to
            allow
        blocked_url_patterns (list of string): A blacklist of URL patterns to
            block
        blocked_url_categories (list of string): A list of URL categories to
            block
        url_category_list_size (string): URL category list size which is
            either 'topSites' or 'fullList'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allowed_url_patterns":'allowedUrlPatterns',
        "blocked_url_patterns":'blockedUrlPatterns',
        "blocked_url_categories":'blockedUrlCategories',
        "url_category_list_size":'urlCategoryListSize'
    }

    def __init__(self,
                 allowed_url_patterns=None,
                 blocked_url_patterns=None,
                 blocked_url_categories=None,
                 url_category_list_size=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkContentFilteringModel class"""

        # Initialize members of the class
        self.allowed_url_patterns = allowed_url_patterns
        self.blocked_url_patterns = blocked_url_patterns
        self.blocked_url_categories = blocked_url_categories
        self.url_category_list_size = url_category_list_size

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
        allowed_url_patterns = dictionary.get('allowedUrlPatterns')
        blocked_url_patterns = dictionary.get('blockedUrlPatterns')
        blocked_url_categories = dictionary.get('blockedUrlCategories')
        url_category_list_size = dictionary.get('urlCategoryListSize')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(allowed_url_patterns,
                   blocked_url_patterns,
                   blocked_url_categories,
                   url_category_list_size,
                   dictionary)


