# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.tag2_model
import meraki.models.network2_model

class CreateOrganizationSamlRolesModel(object):

    """Implementation of the 'createOrganizationSamlRoles' model.

    TODO: type model description here.

    Attributes:
        role (string): The role of the SAML administrator
        org_access (string): The privilege of the SAML administrator on the
            organization
        tags (list of Tag2Model): The list of tags that the SAML administrator
            has privileges on
        networks (list of Network2Model): The list of networks that the SAML
            administrator has privileges on

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "role":'role',
        "org_access":'orgAccess',
        "tags":'tags',
        "networks":'networks'
    }

    def __init__(self,
                 role=None,
                 org_access=None,
                 tags=None,
                 networks=None,
                 additional_properties = {}):
        """Constructor for the CreateOrganizationSamlRolesModel class"""

        # Initialize members of the class
        self.role = role
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
        role = dictionary.get('role')
        org_access = dictionary.get('orgAccess')
        tags = None
        if dictionary.get('tags') != None:
            tags = list()
            for structure in dictionary.get('tags'):
                tags.append(meraki.models.tag2_model.Tag2Model.from_dictionary(structure))
        networks = None
        if dictionary.get('networks') != None:
            networks = list()
            for structure in dictionary.get('networks'):
                networks.append(meraki.models.network2_model.Network2Model.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(role,
                   org_access,
                   tags,
                   networks,
                   dictionary)


