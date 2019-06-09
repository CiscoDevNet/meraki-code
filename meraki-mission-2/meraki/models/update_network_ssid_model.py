# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.radius_server_model
import meraki.models.radius_accounting_server_model
import meraki.models.ap_tags_and_vlan_id_model

class UpdateNetworkSsidModel(object):

    """Implementation of the 'updateNetworkSsid' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of an SSID
        enabled (bool): Whether or not an SSID is enabled
        auth_mode (string): The association control method for the SSID
            ('open', 'psk', 'open-with-radius', '8021x-meraki',
            '8021x-radius')
        encryption_mode (string): The psk encryption mode for the SSID ('wpa',
            'wep', 'wpa-eap')
        psk (string): The passkey for the SSID. This param is only valid if
            the authMode is 'psk'
        wpa_encryption_mode (string): The types of WPA encryption. ('WPA1 and
            WPA2', 'WPA2 only')
        splash_page (string): The type of splash page for the SSID ('None',
            'Click-through splash page', 'Billing', 'Password-protected with
            Meraki RADIUS', 'Password-protected with custom RADIUS',
            'Password-protected with Active Directory', 'Password-protected
            with LDAP', 'SMS authentication', 'Systems Manager Sentry',
            'Facebook Wi-Fi', 'Google OAuth', 'Sponsored guest'). This
            attribute is not supported for template children.
        radius_servers (list of RadiusServerModel): The RADIUS 802.1x servers
            to be used for authentication. This param is only valid if the
            authMode is 'open-with-radius' or '8021x-radius'
        radius_coa_enabled (string): If true, Meraki devices will act as a
            RADIUS Dynamic Authorization Server and will respond to RADIUS
            Change-of-Authorization and Disconnect messages sent by the RADIUS
            server.
        radius_failover_policy (string): This policy determines how
            authentication requests should be handled in the event that all of
            the configured RADIUS servers are unreachable ('Deny access',
            'Allow access')
        radius_load_balancing_policy (string): This policy determines which
            RADIUS server will be contacted first in an authentication attempt
            and the ordering of any necessary retry attempts ('Strict priority
            order', 'Round robin')
        radius_accounting_enabled (string): Whether or not RADIUS accounting
            is enabled. This param is only valid if the authMode is
            'open-with-radius' or '8021x-radius'
        radius_accounting_servers (list of RadiusAccountingServerModel): The
            RADIUS accounting 802.1x servers to be used for authentication.
            This param is only valid if the authMode is 'open-with-radius' or
            '8021x-radius' and radiusAccountingEnabled is 'true'
        ip_assignment_mode (string): The client IP assignment mode ('NAT
            mode', 'Bridge mode', 'Layer 3 roaming', 'Layer 3 roaming with a
            concentrator', 'VPN')
        use_vlan_tagging (string): Direct trafic to use specific VLANs. This
            param is only valid with 'Bridge mode' and 'Layer 3 roaming'
        concentrator_network_id (string): The concentrator to use for 'Layer 3
            roaming with a concentrator' or 'VPN'.
        vlan_id (string): The VLAN ID used for VLAN tagging. This param is
            only valid with 'Layer 3 roaming with a concentrator' and 'VPN'
        default_vlan_id (string): The default VLAN ID used for 'all other
            APs'. This param is only valid with 'Bridge mode' and 'Layer 3
            roaming'
        ap_tags_and_vlan_ids (list of ApTagsAndVlanIdModel): The list of tags
            and VLAN IDs used for VLAN tagging. This param is only valid with
            'Bridge mode', 'Layer 3 roaming'
        walled_garden_enabled (string): Allow access to a configurable list of
            IP ranges, which users may access prior to sign-on.
        walled_garden_ranges (string): Specify your walled garden by entering
            space-separated addresses, ranges using CIDR notation, domain
            names, and domain wildcards (e.g. 192.168.1.1/24 192.168.37.10/32
            www.yahoo.com *.google.com). Meraki's splash page is automatically
            included in your walled garden.
        min_bitrate (string): The minimum bitrate in Mbps. (1, 2, 5.5, 6, 9,
            11, 12, 18, 24, 36, 48, 54)
        band_selection (string): The client-serving radio frequencies. (Dual
            band operation, 5 GHz band only, Dual band operation with Band
            Steering)
        per_client_bandwidth_limit_up (string): The upload bandwidth limit in
            Kbps. (0 represents no limit.)
        per_client_bandwidth_limit_down (string): The download bandwidth limit
            in Kbps. (0 represents no limit.)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "enabled":'enabled',
        "auth_mode":'authMode',
        "encryption_mode":'encryptionMode',
        "psk":'psk',
        "wpa_encryption_mode":'wpaEncryptionMode',
        "splash_page":'splashPage',
        "radius_servers":'radiusServers',
        "radius_coa_enabled":'radiusCoaEnabled',
        "radius_failover_policy":'radiusFailoverPolicy',
        "radius_load_balancing_policy":'radiusLoadBalancingPolicy',
        "radius_accounting_enabled":'radiusAccountingEnabled',
        "radius_accounting_servers":'radiusAccountingServers',
        "ip_assignment_mode":'ipAssignmentMode',
        "use_vlan_tagging":'useVlanTagging',
        "concentrator_network_id":'concentratorNetworkId',
        "vlan_id":'vlanId',
        "default_vlan_id":'defaultVlanId',
        "ap_tags_and_vlan_ids":'apTagsAndVlanIds',
        "walled_garden_enabled":'walledGardenEnabled',
        "walled_garden_ranges":'walledGardenRanges',
        "min_bitrate":'minBitrate',
        "band_selection":'bandSelection',
        "per_client_bandwidth_limit_up":'perClientBandwidthLimitUp',
        "per_client_bandwidth_limit_down":'perClientBandwidthLimitDown'
    }

    def __init__(self,
                 name=None,
                 enabled=None,
                 auth_mode=None,
                 encryption_mode=None,
                 psk=None,
                 wpa_encryption_mode=None,
                 splash_page=None,
                 radius_servers=None,
                 radius_coa_enabled=None,
                 radius_failover_policy=None,
                 radius_load_balancing_policy=None,
                 radius_accounting_enabled=None,
                 radius_accounting_servers=None,
                 ip_assignment_mode=None,
                 use_vlan_tagging=None,
                 concentrator_network_id=None,
                 vlan_id=None,
                 default_vlan_id=None,
                 ap_tags_and_vlan_ids=None,
                 walled_garden_enabled=None,
                 walled_garden_ranges=None,
                 min_bitrate=None,
                 band_selection=None,
                 per_client_bandwidth_limit_up=None,
                 per_client_bandwidth_limit_down=None,
                 additional_properties = {}):
        """Constructor for the UpdateNetworkSsidModel class"""

        # Initialize members of the class
        self.name = name
        self.enabled = enabled
        self.auth_mode = auth_mode
        self.encryption_mode = encryption_mode
        self.psk = psk
        self.wpa_encryption_mode = wpa_encryption_mode
        self.splash_page = splash_page
        self.radius_servers = radius_servers
        self.radius_coa_enabled = radius_coa_enabled
        self.radius_failover_policy = radius_failover_policy
        self.radius_load_balancing_policy = radius_load_balancing_policy
        self.radius_accounting_enabled = radius_accounting_enabled
        self.radius_accounting_servers = radius_accounting_servers
        self.ip_assignment_mode = ip_assignment_mode
        self.use_vlan_tagging = use_vlan_tagging
        self.concentrator_network_id = concentrator_network_id
        self.vlan_id = vlan_id
        self.default_vlan_id = default_vlan_id
        self.ap_tags_and_vlan_ids = ap_tags_and_vlan_ids
        self.walled_garden_enabled = walled_garden_enabled
        self.walled_garden_ranges = walled_garden_ranges
        self.min_bitrate = min_bitrate
        self.band_selection = band_selection
        self.per_client_bandwidth_limit_up = per_client_bandwidth_limit_up
        self.per_client_bandwidth_limit_down = per_client_bandwidth_limit_down

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
        enabled = dictionary.get('enabled')
        auth_mode = dictionary.get('authMode')
        encryption_mode = dictionary.get('encryptionMode')
        psk = dictionary.get('psk')
        wpa_encryption_mode = dictionary.get('wpaEncryptionMode')
        splash_page = dictionary.get('splashPage')
        radius_servers = None
        if dictionary.get('radiusServers') != None:
            radius_servers = list()
            for structure in dictionary.get('radiusServers'):
                radius_servers.append(meraki.models.radius_server_model.RadiusServerModel.from_dictionary(structure))
        radius_coa_enabled = dictionary.get('radiusCoaEnabled')
        radius_failover_policy = dictionary.get('radiusFailoverPolicy')
        radius_load_balancing_policy = dictionary.get('radiusLoadBalancingPolicy')
        radius_accounting_enabled = dictionary.get('radiusAccountingEnabled')
        radius_accounting_servers = None
        if dictionary.get('radiusAccountingServers') != None:
            radius_accounting_servers = list()
            for structure in dictionary.get('radiusAccountingServers'):
                radius_accounting_servers.append(meraki.models.radius_accounting_server_model.RadiusAccountingServerModel.from_dictionary(structure))
        ip_assignment_mode = dictionary.get('ipAssignmentMode')
        use_vlan_tagging = dictionary.get('useVlanTagging')
        concentrator_network_id = dictionary.get('concentratorNetworkId')
        vlan_id = dictionary.get('vlanId')
        default_vlan_id = dictionary.get('defaultVlanId')
        ap_tags_and_vlan_ids = None
        if dictionary.get('apTagsAndVlanIds') != None:
            ap_tags_and_vlan_ids = list()
            for structure in dictionary.get('apTagsAndVlanIds'):
                ap_tags_and_vlan_ids.append(meraki.models.ap_tags_and_vlan_id_model.ApTagsAndVlanIdModel.from_dictionary(structure))
        walled_garden_enabled = dictionary.get('walledGardenEnabled')
        walled_garden_ranges = dictionary.get('walledGardenRanges')
        min_bitrate = dictionary.get('minBitrate')
        band_selection = dictionary.get('bandSelection')
        per_client_bandwidth_limit_up = dictionary.get('perClientBandwidthLimitUp')
        per_client_bandwidth_limit_down = dictionary.get('perClientBandwidthLimitDown')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(name,
                   enabled,
                   auth_mode,
                   encryption_mode,
                   psk,
                   wpa_encryption_mode,
                   splash_page,
                   radius_servers,
                   radius_coa_enabled,
                   radius_failover_policy,
                   radius_load_balancing_policy,
                   radius_accounting_enabled,
                   radius_accounting_servers,
                   ip_assignment_mode,
                   use_vlan_tagging,
                   concentrator_network_id,
                   vlan_id,
                   default_vlan_id,
                   ap_tags_and_vlan_ids,
                   walled_garden_enabled,
                   walled_garden_ranges,
                   min_bitrate,
                   band_selection,
                   per_client_bandwidth_limit_up,
                   per_client_bandwidth_limit_down,
                   dictionary)


