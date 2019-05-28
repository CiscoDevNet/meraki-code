# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RuleModel(object):

    """Implementation of the 'Rule' model.

    TODO: type model description here.

    Attributes:
        comment (string): Description of the rule (optional)
        policy (string): 'Allow' or 'Deny' traffic specified by this rule
        protocol (string): The type of protocol (must be 'tcp', 'udp', 'icmp'
            or 'any')
        src_port (string): Comma-separated list of source port(s) (integer in
            the range 1-65535), or 'any'
        src_cidr (string): Comma-separated list of source IP address(es) (in
            IP or CIDR notation), or 'any' (note: FQDN not supported for
            source addresses)
        dest_port (string): Comma-separated list of destination port(s)
            (integer in the range 1-65535), or 'any'
        dest_cidr (string): Comma-separated list of destination IP address(es)
            (in IP or CIDR notation), fully-qualified domain names (FQDN) or
            'any'
        syslog_enabled (bool): Log this rule to syslog (true or false, boolean
            value) - only applicable if a syslog has been configured
            (optional)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "policy":'policy',
        "protocol":'protocol',
        "src_cidr":'srcCidr',
        "dest_cidr":'destCidr',
        "comment":'comment',
        "src_port":'srcPort',
        "dest_port":'destPort',
        "syslog_enabled":'syslogEnabled'
    }

    def __init__(self,
                 policy=None,
                 protocol=None,
                 src_cidr=None,
                 dest_cidr=None,
                 comment=None,
                 src_port=None,
                 dest_port=None,
                 syslog_enabled=None,
                 additional_properties = {}):
        """Constructor for the RuleModel class"""

        # Initialize members of the class
        self.comment = comment
        self.policy = policy
        self.protocol = protocol
        self.src_port = src_port
        self.src_cidr = src_cidr
        self.dest_port = dest_port
        self.dest_cidr = dest_cidr
        self.syslog_enabled = syslog_enabled

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
        policy = dictionary.get('policy')
        protocol = dictionary.get('protocol')
        src_cidr = dictionary.get('srcCidr')
        dest_cidr = dictionary.get('destCidr')
        comment = dictionary.get('comment')
        src_port = dictionary.get('srcPort')
        dest_port = dictionary.get('destPort')
        syslog_enabled = dictionary.get('syslogEnabled')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(policy,
                   protocol,
                   src_cidr,
                   dest_cidr,
                   comment,
                   src_port,
                   dest_port,
                   syslog_enabled,
                   dictionary)


