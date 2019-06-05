# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class DhcpOptionModel(object):

    """Implementation of the 'DhcpOption' model.

    TODO: type model description here.

    Attributes:
        code (string): The code for the DHCP option. This should be an integer
            between 2 and 254.
        mtype (string): The type for the DHCP option. One of: "text", "ip",
            "hex", or "integer".
        value (string): The value for the DHCP option

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code":'code',
        "mtype":'type',
        "value":'value'
    }

    def __init__(self,
                 code=None,
                 mtype=None,
                 value=None,
                 additional_properties = {}):
        """Constructor for the DhcpOptionModel class"""

        # Initialize members of the class
        self.code = code
        self.mtype = mtype
        self.value = value

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
        code = dictionary.get('code')
        mtype = dictionary.get('type')
        value = dictionary.get('value')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(code,
                   mtype,
                   value,
                   dictionary)


