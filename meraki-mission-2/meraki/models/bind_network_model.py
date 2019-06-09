# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BindNetworkModel(object):

    """Implementation of the 'bindNetwork' model.

    TODO: type model description here.

    Attributes:
        config_template_id (string): The ID of the template to which the
            network should be bound.
        auto_bind (bool): Optional boolean indicating whether the network's
            switches should automatically bind to profiles of the same model.
            Defaults to false if left unspecified. This option only affects
            switch networks and switch templates. Auto-bind is not valid
            unless the switch template has at least one profile and has at
            most one profile per switch model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "config_template_id":'configTemplateId',
        "auto_bind":'autoBind'
    }

    def __init__(self,
                 config_template_id=None,
                 auto_bind=None,
                 additional_properties = {}):
        """Constructor for the BindNetworkModel class"""

        # Initialize members of the class
        self.config_template_id = config_template_id
        self.auto_bind = auto_bind

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
        config_template_id = dictionary.get('configTemplateId')
        auto_bind = dictionary.get('autoBind')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(config_template_id,
                   auto_bind,
                   dictionary)


