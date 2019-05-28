# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule6Model(object):

    """Implementation of the 'Rule6' model.

    TODO: type model description here.

    Attributes:
        name (string): A descriptive name for the rule
        public_ip (string): The IP address that will be used to access the
            internal resource from the WAN
        lan_ip (string): The IP address of the server or device that hosts the
            internal resource that you wish to make available on the WAN
        uplink (string): The physical WAN interface on which the traffic will
            arrive ('internet1' or, if available, 'internet2')
        allowed_inbound (list of object): The ports this mapping will provide
            access on, and the remote IPs that will be allowed access to the
            resource
        protocol (string): Either of the following: 'tcp', 'udp', 'icmp-ping'
            or 'any'
        destination_ports (string): An array of ports or port ranges that will
            be forwarded to the host on the LAN
        allowed_ips (string): An array of ranges of WAN IP addresses that are
            allowed to make inbound connections on the specified ports or port
            ranges, or 'any'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "public_ip":'publicIp',
        "lan_ip":'lanIp',
        "uplink":'uplink',
        "allowed_inbound":'allowedInbound',
        "protocol":'protocol',
        "destination_ports":'destinationPorts',
        "allowed_ips":'allowedIps'
    }

    def __init__(self,
                 name=None,
                 public_ip=None,
                 lan_ip=None,
                 uplink=None,
                 allowed_inbound=None,
                 protocol=None,
                 destination_ports=None,
                 allowed_ips=None,
                 additional_properties = {}):
        """Constructor for the Rule6Model class"""

        # Initialize members of the class
        self.name = name
        self.public_ip = public_ip
        self.lan_ip = lan_ip
        self.uplink = uplink
        self.allowed_inbound = allowed_inbound
        self.protocol = protocol
        self.destination_ports = destination_ports
        self.allowed_ips = allowed_ips

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
        public_ip = dictionary.get('publicIp')
        lan_ip = dictionary.get('lanIp')
        uplink = dictionary.get('uplink')
        allowed_inbound = dictionary.get('allowedInbound')
        protocol = dictionary.get('protocol')
        destination_ports = dictionary.get('destinationPorts')
        allowed_ips = dictionary.get('allowedIps')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   public_ip,
                   lan_ip,
                   uplink,
                   allowed_inbound,
                   protocol,
                   destination_ports,
                   allowed_ips,
                   dictionary)


