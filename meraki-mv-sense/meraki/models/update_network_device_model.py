# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkDeviceModel(object):

    """Implementation of the 'updateNetworkDevice' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of a device
        tags (string): The tags of a device
        lat (float): The latitude of a device
        lng (float): The longitude of a device
        address (string): The address of a device
        notes (string): The notes for the device. String. Limited to 255
            characters.
        move_map_marker (string): Whether or not to set the latitude and
            longitude of a device based on the new address. Only applies when
            lat and lng are not specified.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "tags":'tags',
        "lat":'lat',
        "lng":'lng',
        "address":'address',
        "notes":'notes',
        "move_map_marker":'moveMapMarker'
    }

    def __init__(self,
                 name=None,
                 tags=None,
                 lat=None,
                 lng=None,
                 address=None,
                 notes=None,
                 move_map_marker=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkDeviceModel class"""

        # Initialize members of the class
        self.name = name
        self.tags = tags
        self.lat = lat
        self.lng = lng
        self.address = address
        self.notes = notes
        self.move_map_marker = move_map_marker

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
        tags = dictionary.get('tags')
        lat = dictionary.get('lat')
        lng = dictionary.get('lng')
        address = dictionary.get('address')
        notes = dictionary.get('notes')
        move_map_marker = dictionary.get('moveMapMarker')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   tags,
                   lat,
                   lng,
                   address,
                   notes,
                   move_map_marker,
                   dictionary)


