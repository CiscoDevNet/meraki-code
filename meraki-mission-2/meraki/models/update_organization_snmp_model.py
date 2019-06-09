# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateOrganizationSnmpModel(object):

    """Implementation of the 'updateOrganizationSnmp' model.

    TODO: type model description here.

    Attributes:
        v_2_c_enabled (bool): Boolean indicating whether SNMP version 2c is
            enabled for the organization
        v_3_enabled (bool): Boolean indicating whether SNMP version 3 is
            enabled for the organization
        v_3_auth_mode (string): The SNMP version 3 authentication mode either
            MD5 or SHA
        v_3_auth_pass (string): The SNMP version 3 authentication password. 
            Must be at least 8 characters if specified.
        v_3_priv_mode (string): The SNMP version 3 privacy mode DES or AES128
        v_3_priv_pass (string): The SNMP version 3 privacy password.  Must be
            at least 8 characters if specified.
        peer_ips (string): The IPs that are allowed to access the SNMP server.
            This list should be IPv4 addresses separated by semi-colons (ie.
            "1.2.3.4;2.3.4.5").

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "v2c_enabled":'v2cEnabled',
        "v3_enabled":'v3Enabled',
        "v3_auth_mode":'v3AuthMode',
        "v3_auth_pass":'v3AuthPass',
        "v3_priv_mode":'v3PrivMode',
        "v3_priv_pass":'v3PrivPass',
        "peer_ips":'peerIps'
    }

    def __init__(self,
                 v2c_enabled=None,
                 v3_enabled=None,
                 v3_auth_mode=None,
                 v3_auth_pass=None,
                 v3_priv_mode=None,
                 v3_priv_pass=None,
                 peer_ips=None,
                 additional_properties = {}):
        """Constructor for the UpdateOrganizationSnmpModel class"""

        # Initialize members of the class
        self.v2c_enabled = v2c_enabled
        self.v3_enabled = v3_enabled
        self.v3_auth_mode = v3_auth_mode
        self.v3_auth_pass = v3_auth_pass
        self.v3_priv_mode = v3_priv_mode
        self.v3_priv_pass = v3_priv_pass
        self.peer_ips = peer_ips

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
        v2c_enabled = dictionary.get('v2cEnabled')
        v3_enabled = dictionary.get('v3Enabled')
        v3_auth_mode = dictionary.get('v3AuthMode')
        v3_auth_pass = dictionary.get('v3AuthPass')
        v3_priv_mode = dictionary.get('v3PrivMode')
        v3_priv_pass = dictionary.get('v3PrivPass')
        peer_ips = dictionary.get('peerIps')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(v2c_enabled,
                   v3_enabled,
                   v3_auth_mode,
                   v3_auth_pass,
                   v3_priv_mode,
                   v3_priv_pass,
                   peer_ips,
                   dictionary)


