# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule5Model(object):

    """Implementation of the 'Rule5' model.

    TODO: type model description here.

    Attributes:
        public_ip (string): The IP address that will be used to access the
            internal resource from the WAN
        uplink (string): The physical WAN interface on which the traffic will
            arrive ('internet1' or, if available, 'internet2')
        port_rules (list of object): An array of associated forwarding rules
        name (string): A description of the rule
        protocol (string): 'tcp' or 'udp'
        public_port (string): Destination port of the traffic that is arriving
            on the WAN
        local_ip (string): Local IP address to which traffic will be
            forwarded
        local_port (string): Destination port of the forwarded traffic that
            will be sent from the MX to the specified host on the LAN. If you
            simply wish to forward the traffic without translating the port,
            this should be the same as the Public port
        allowed_ips (string): Remote IP addresses or ranges that are permitted
            to access the internal resource via this port forwarding rule, or
            'any'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "public_ip":'publicIp',
        "uplink":'uplink',
        "port_rules":'portRules',
        "name":'name',
        "protocol":'protocol',
        "public_port":'publicPort',
        "local_ip":'localIp',
        "local_port":'localPort',
        "allowed_ips":'allowedIps'
    }

    def __init__(self,
                 public_ip=None,
                 uplink=None,
                 port_rules=None,
                 name=None,
                 protocol=None,
                 public_port=None,
                 local_ip=None,
                 local_port=None,
                 allowed_ips=None,
                 additional_properties = {}):
        """Constructor for the Rule5Model class"""

        # Initialize members of the class
        self.public_ip = public_ip
        self.uplink = uplink
        self.port_rules = port_rules
        self.name = name
        self.protocol = protocol
        self.public_port = public_port
        self.local_ip = local_ip
        self.local_port = local_port
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
        public_ip = dictionary.get('publicIp')
        uplink = dictionary.get('uplink')
        port_rules = dictionary.get('portRules')
        name = dictionary.get('name')
        protocol = dictionary.get('protocol')
        public_port = dictionary.get('publicPort')
        local_ip = dictionary.get('localIp')
        local_port = dictionary.get('localPort')
        allowed_ips = dictionary.get('allowedIps')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(public_ip,
                   uplink,
                   port_rules,
                   name,
                   protocol,
                   public_port,
                   local_ip,
                   local_port,
                   allowed_ips,
                   dictionary)


