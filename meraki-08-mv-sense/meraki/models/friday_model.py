# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class FridayModel(object):

    """Implementation of the 'Friday' model.

    The schedule object for Friday.

    Attributes:
        active (bool): Whether the schedule is active (true) or inactive
            (false) during the time specified between 'from' and 'to'.
            Defaults to true.
        mfrom (string): The time, from '00:00' to '24:00'. Must be less than
            the time specified in 'to'. Defaults to '00:00'. Only 30 minute
            increments are allowed.
        to (string): The time, from '00:00' to '24:00'. Must be greater than
            the time specified in 'from'. Defaults to '24:00'. Only 30 minute
            increments are allowed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "active":'active',
        "mfrom":'from',
        "to":'to'
    }

    def __init__(self,
                 active=None,
                 mfrom=None,
                 to=None,
                 additional_properties = {}):
        """Constructor for the FridayModel class"""

        # Initialize members of the class
        self.active = active
        self.mfrom = mfrom
        self.to = to

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
        active = dictionary.get('active')
        mfrom = dictionary.get('from')
        to = dictionary.get('to')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(active,
                   mfrom,
                   to,
                   dictionary)


