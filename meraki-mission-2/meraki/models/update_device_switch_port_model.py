# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateDeviceSwitchPortModel(object):

    """Implementation of the 'updateDeviceSwitchPort' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the switch port
        tags (string): The tags of the switch port
        enabled (string): The status of the switch port
        mtype (string): The type of the switch port ("access" or "trunk")
        vlan (string): The VLAN of the switch port
        voice_vlan (string): The voice VLAN of the switch port. Only
            applicable to access ports.
        allowed_vlans (string): The VLANs allowed on the switch port. Only
            applicable to trunk ports.
        poe_enabled (string): The PoE status of the switch port
        isolation_enabled (string): The isolation status of the switch port
        rstp_enabled (string): The rapid spanning tree protocol status
        stp_guard (string): The state of the STP guard ("disabled", "Root
            guard", "BPDU guard", "Loop guard")
        access_policy_number (string): The number of the access policy of the
            switch port. Only applicable to access ports.
        link_negotiation (string): The link speed for the switch port

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "tags":'tags',
        "enabled":'enabled',
        "mtype":'type',
        "vlan":'vlan',
        "voice_vlan":'voiceVlan',
        "allowed_vlans":'allowedVlans',
        "poe_enabled":'poeEnabled',
        "isolation_enabled":'isolationEnabled',
        "rstp_enabled":'rstpEnabled',
        "stp_guard":'stpGuard',
        "access_policy_number":'accessPolicyNumber',
        "link_negotiation":'linkNegotiation'
    }

    def __init__(self,
                 name=None,
                 tags=None,
                 enabled=None,
                 mtype=None,
                 vlan=None,
                 voice_vlan=None,
                 allowed_vlans=None,
                 poe_enabled=None,
                 isolation_enabled=None,
                 rstp_enabled=None,
                 stp_guard=None,
                 access_policy_number=None,
                 link_negotiation=None,
                 additional_properties = {}):
        """Constructor for the UpdateDeviceSwitchPortModel class"""

        # Initialize members of the class
        self.name = name
        self.tags = tags
        self.enabled = enabled
        self.mtype = mtype
        self.vlan = vlan
        self.voice_vlan = voice_vlan
        self.allowed_vlans = allowed_vlans
        self.poe_enabled = poe_enabled
        self.isolation_enabled = isolation_enabled
        self.rstp_enabled = rstp_enabled
        self.stp_guard = stp_guard
        self.access_policy_number = access_policy_number
        self.link_negotiation = link_negotiation

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
        enabled = dictionary.get('enabled')
        mtype = dictionary.get('type')
        vlan = dictionary.get('vlan')
        voice_vlan = dictionary.get('voiceVlan')
        allowed_vlans = dictionary.get('allowedVlans')
        poe_enabled = dictionary.get('poeEnabled')
        isolation_enabled = dictionary.get('isolationEnabled')
        rstp_enabled = dictionary.get('rstpEnabled')
        stp_guard = dictionary.get('stpGuard')
        access_policy_number = dictionary.get('accessPolicyNumber')
        link_negotiation = dictionary.get('linkNegotiation')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   tags,
                   enabled,
                   mtype,
                   vlan,
                   voice_vlan,
                   allowed_vlans,
                   poe_enabled,
                   isolation_enabled,
                   rstp_enabled,
                   stp_guard,
                   access_policy_number,
                   link_negotiation,
                   dictionary)


