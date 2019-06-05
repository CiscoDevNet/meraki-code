# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateOrganizationNetworksModel(object):

    """Implementation of the 'createOrganizationNetworks' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the new network
        mtype (string): The type of the new network. Valid types are wireless,
            appliance, switch, phone, systemsManager, camera or a
            space-separated list of those for a combined network.
        tags (string): A space-separated list of tags to be applied to the
            network
        time_zone (string): The timezone of the network. For a list of allowed
            timezones, please see the 'TZ' column in the table in <a
            target='_blank'
            href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'
            >this article.</a>
        copy_from_network_id (string): The ID of the network to copy
            configuration from. Other provided parameters will override the
            copied configuration, except type which must match this network's
            type exactly.
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
        "mtype":'type',
        "tags":'tags',
        "time_zone":'timeZone',
        "copy_from_network_id":'copyFromNetworkId',
        "disable_my_meraki_com":'disableMyMerakiCom',
        "disable_remote_status_page":'disableRemoteStatusPage'
    }

    def __init__(self,
                 name=None,
                 mtype=None,
                 tags=None,
                 time_zone=None,
                 copy_from_network_id=None,
                 disable_my_meraki_com=None,
                 disable_remote_status_page=None,
                 additional_properties = {}):
        """Constructor for the CreateOrganizationNetworksModel class"""

        # Initialize members of the class
        self.name = name
        self.mtype = mtype
        self.tags = tags
        self.time_zone = time_zone
        self.copy_from_network_id = copy_from_network_id
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
        mtype = dictionary.get('type')
        tags = dictionary.get('tags')
        time_zone = dictionary.get('timeZone')
        copy_from_network_id = dictionary.get('copyFromNetworkId')
        disable_my_meraki_com = dictionary.get('disableMyMerakiCom')
        disable_remote_status_page = dictionary.get('disableRemoteStatusPage')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   mtype,
                   tags,
                   time_zone,
                   copy_from_network_id,
                   disable_my_meraki_com,
                   disable_remote_status_page,
                   dictionary)


