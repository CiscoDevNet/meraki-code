# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ReservedIpRangeModel(object):

    """Implementation of the 'ReservedIpRange' model.

    TODO: type model description here.

    Attributes:
        start (string): The first IP in the reserved range
        end (string): The last IP in the reserved range
        comment (string): A text comment for the reserved range

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start":'start',
        "end":'end',
        "comment":'comment'
    }

    def __init__(self,
                 start=None,
                 end=None,
                 comment=None,
                 additional_properties = {}):
        """Constructor for the ReservedIpRangeModel class"""

        # Initialize members of the class
        self.start = start
        self.end = end
        self.comment = comment

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
        start = dictionary.get('start')
        end = dictionary.get('end')
        comment = dictionary.get('comment')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(start,
                   end,
                   comment,
                   dictionary)


