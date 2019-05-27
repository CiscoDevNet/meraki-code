# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class IpsecPoliciesModel(object):

    """Implementation of the 'IpsecPolicies' model.

    Custom IPSec policies for the VPN peer. If not included and a preset has
    not been chosen, the default preset for IPSec policies will be used.

    Attributes:
        ike_cipher_algo (list of string): This is the cipher algorithm to be
            used in Phase 1. The value should be an array with one of the
            following algorithms: 'aes256', 'aes192', 'aes128', 'tripledes',
            'des'
        ike_auth_algo (list of string): This is the authentication algorithm
            to be used in Phase 1. The value should be an array with one of
            the following algorithms: 'sha1', 'md5'
        ike_diffie_hellman_group (list of string): This is the Diffie-Hellman
            group to be used in Phase 1. The value should be an array with one
            of the following algorithms: 'group5', 'group2', 'group1'
        ike_lifetime (int): The lifetime of the Phase 1 SA in seconds.
        child_cipher_algo (list of string): This is the cipher algorithms to
            be used in Phase 2. The value should be an array with one or more
            of the following algorithms: 'aes256', 'aes192', 'aes128',
            'tripledes', 'des', 'null'
        child_auth_algo (list of string): This is the authentication
            algorithms to be used in Phase 2. The value should be an array
            with one of the following algorithms: 'sha1', 'md5'
        child_pfs_group (list of string): This is the Diffie-Hellman group to
            be used for Perfect Forward Secrecy in Phase 2. The value should
            be an array with one of the following values: 'disabled',
            'group5', 'group2', 'group1'
        child_lifetime (int): The lifetime of the Phase 2 SA in seconds.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ike_cipher_algo":'ikeCipherAlgo',
        "ike_auth_algo":'ikeAuthAlgo',
        "ike_diffie_hellman_group":'ikeDiffieHellmanGroup',
        "ike_lifetime":'ikeLifetime',
        "child_cipher_algo":'childCipherAlgo',
        "child_auth_algo":'childAuthAlgo',
        "child_pfs_group":'childPfsGroup',
        "child_lifetime":'childLifetime'
    }

    def __init__(self,
                 ike_cipher_algo=None,
                 ike_auth_algo=None,
                 ike_diffie_hellman_group=None,
                 ike_lifetime=None,
                 child_cipher_algo=None,
                 child_auth_algo=None,
                 child_pfs_group=None,
                 child_lifetime=None,
                 additional_properties = {}):
        """Constructor for the IpsecPoliciesModel class"""

        # Initialize members of the class
        self.ike_cipher_algo = ike_cipher_algo
        self.ike_auth_algo = ike_auth_algo
        self.ike_diffie_hellman_group = ike_diffie_hellman_group
        self.ike_lifetime = ike_lifetime
        self.child_cipher_algo = child_cipher_algo
        self.child_auth_algo = child_auth_algo
        self.child_pfs_group = child_pfs_group
        self.child_lifetime = child_lifetime

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
        ike_cipher_algo = dictionary.get('ikeCipherAlgo')
        ike_auth_algo = dictionary.get('ikeAuthAlgo')
        ike_diffie_hellman_group = dictionary.get('ikeDiffieHellmanGroup')
        ike_lifetime = dictionary.get('ikeLifetime')
        child_cipher_algo = dictionary.get('childCipherAlgo')
        child_auth_algo = dictionary.get('childAuthAlgo')
        child_pfs_group = dictionary.get('childPfsGroup')
        child_lifetime = dictionary.get('childLifetime')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(ike_cipher_algo,
                   ike_auth_algo,
                   ike_diffie_hellman_group,
                   ike_lifetime,
                   child_cipher_algo,
                   child_auth_algo,
                   child_pfs_group,
                   child_lifetime,
                   dictionary)


