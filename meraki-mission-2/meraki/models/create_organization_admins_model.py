# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.tag_model
import meraki.models.network_model

class CreateOrganizationAdminsModel(object):

    """Implementation of the 'createOrganizationAdmins' model.

    TODO: type model description here.

    Attributes:
        email (string): The email of the dashboard administrator. This
            attribute can not be updated.
        name (string): The name of the dashboard administrator
        org_access (string): The privilege of the dashboard administrator on
            the organization (full, read-only, none)
        tags (list of TagModel): The list of tags that the dashboard
            administrator has privileges on
        networks (list of NetworkModel): The list of networks that the
            dashboard administrator has privileges on

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email":'email',
        "name":'name',
        "org_access":'orgAccess',
        "tags":'tags',
        "networks":'networks'
    }

    def __init__(self,
                 email=None,
                 name=None,
                 org_access=None,
                 tags=None,
                 networks=None,
                 additional_properties = {}):
        """Constructor for the CreateOrganizationAdminsModel class"""

        # Initialize members of the class
        self.email = email
        self.name = name
        self.org_access = org_access
        self.tags = tags
        self.networks = networks

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
        email = dictionary.get('email')
        name = dictionary.get('name')
        org_access = dictionary.get('orgAccess')
        tags = None
        if dictionary.get('tags') != None:
            tags = list()
            for structure in dictionary.get('tags'):
                tags.append(meraki.models.tag_model.TagModel.from_dictionary(structure))
        networks = None
        if dictionary.get('networks') != None:
            networks = list()
            for structure in dictionary.get('networks'):
                networks.append(meraki.models.network_model.NetworkModel.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(email,
                   name,
                   org_access,
                   tags,
                   networks,
                   dictionary)


