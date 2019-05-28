# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Rule4Model(object):

    """Implementation of the 'Rule4' model.

    TODO: type model description here.

    Attributes:
        comment (string): Description of the rule (optional)
        policy (string): 'Allow' or 'Deny' traffic specified by this rule
        protocol (string): The type of protocol (must be 'tcp', 'udp', 'icmp'
            or 'any')
        dest_port (string): Comma-separated list of destination port(s)
            (integer in the range 1-65535), or 'any'
        dest_cidr (string): Comma-separated list of destination IP address(es)
            (in IP or CIDR notation), fully-qualified domain names (FQDN) or
            'any'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "policy":'policy',
        "protocol":'protocol',
        "dest_cidr":'destCidr',
        "comment":'comment',
        "dest_port":'destPort'
    }

    def __init__(self,
                 policy=None,
                 protocol=None,
                 dest_cidr=None,
                 comment=None,
                 dest_port=None,
                 additional_properties = {}):
        """Constructor for the Rule4Model class"""

        # Initialize members of the class
        self.comment = comment
        self.policy = policy
        self.protocol = protocol
        self.dest_port = dest_port
        self.dest_cidr = dest_cidr

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
        dest_cidr = dictionary.get('destCidr')
        comment = dictionary.get('comment')
        dest_port = dictionary.get('destPort')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(policy,
                   protocol,
                   dest_cidr,
                   comment,
                   dest_port,
                   dictionary)


