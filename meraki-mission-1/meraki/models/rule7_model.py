# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule7Model(object):

    """Implementation of the 'Rule7' model.

    TODO: type model description here.

    Attributes:
        name (string): A descriptive name for the rule
        lan_ip (string): The IP address of the server or device that hosts the
            internal resource that you wish to make available on the WAN
        uplink (string): The physical WAN interface on which the traffic will
            arrive ('internet1' or, if available, 'internet2' or 'both')
        public_port (string): A port or port ranges that will be forwarded to
            the host on the LAN
        local_port (string): A port or port ranges that will receive the
            forwarded traffic from the WAN
        allowed_ips (list of string): An array of ranges of WAN IP addresses
            that are allowed to make inbound connections on the specified
            ports or port ranges (or any)
        protocol (string): TCP or UDP

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "lan_ip":'lanIp',
        "uplink":'uplink',
        "public_port":'publicPort',
        "local_port":'localPort',
        "allowed_ips":'allowedIps',
        "protocol":'protocol'
    }

    def __init__(self,
                 name=None,
                 lan_ip=None,
                 uplink=None,
                 public_port=None,
                 local_port=None,
                 allowed_ips=None,
                 protocol=None,
                 additional_properties = {}):
        """Constructor for the Rule7Model class"""

        # Initialize members of the class
        self.name = name
        self.lan_ip = lan_ip
        self.uplink = uplink
        self.public_port = public_port
        self.local_port = local_port
        self.allowed_ips = allowed_ips
        self.protocol = protocol

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
        lan_ip = dictionary.get('lanIp')
        uplink = dictionary.get('uplink')
        public_port = dictionary.get('publicPort')
        local_port = dictionary.get('localPort')
        allowed_ips = dictionary.get('allowedIps')
        protocol = dictionary.get('protocol')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   lan_ip,
                   uplink,
                   public_port,
                   local_port,
                   allowed_ips,
                   protocol,
                   dictionary)


