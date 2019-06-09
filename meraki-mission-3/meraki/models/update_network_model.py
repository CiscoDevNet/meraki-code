# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkModel(object):

    """Implementation of the 'updateNetwork' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the new network
        time_zone (string): The timezone of the network. For a list of allowed
            timezones, please see the 'TZ' column in the table in <a
            target='_blank'
            href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'
            >this article.</a>
        tags (string): A space-separated list of tags to be applied to the
            network
        disable_my_meraki_com (bool): Disables the local device status pages
            (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com,
            </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com,
            </a><a target='_blank'
            href='http://switch.meraki.com/'>switch.meraki.com, </a><a
            target='_blank'
            href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional
            (defaults to false)
        disable_remote_status_page (bool): Disables access to the device
            status page (<a target='_blank'>http://[device's LAN IP])</a>.
            Optional. Can only be set if disableMyMerakiCom is set to false

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "time_zone":'timeZone',
        "tags":'tags',
        "disable_my_meraki_com":'disableMyMerakiCom',
        "disable_remote_status_page":'disableRemoteStatusPage'
    }

    def __init__(self,
                 name=None,
                 time_zone=None,
                 tags=None,
                 disable_my_meraki_com=None,
                 disable_remote_status_page=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkModel class"""

        # Initialize members of the class
        self.name = name
        self.time_zone = time_zone
        self.tags = tags
        self.disable_my_meraki_com = disable_my_meraki_com
        self.disable_remote_status_page = disable_remote_status_page

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
        time_zone = dictionary.get('timeZone')
        tags = dictionary.get('tags')
        disable_my_meraki_com = dictionary.get('disableMyMerakiCom')
        disable_remote_status_page = dictionary.get('disableRemoteStatusPage')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   time_zone,
                   tags,
                   disable_my_meraki_com,
                   disable_remote_status_page,
                   dictionary)


