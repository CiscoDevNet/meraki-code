# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class PIIController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_network_pii_pii_keys(self,
                                 options=dict()):
        """Does a GET request to /networks/{networkId}/pii/piiKeys.

        List the keys required to access Personally Identifiable Information
        (PII) for a given identifier. Exactly one identifier will be accepted.
        If the organization contains org-wide Systems Manager users matching
        the key provided then there will be an entry with the key "0"
        containing the applicable keys.
        ## ALTERNATE PATH
        ```
        /organizations/{organizationId}/pii/piiKeys
        ```

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    username -- string -- The username of a Systems Manager
                        user
                    email -- string -- The email of a network user account or
                        a Systems Manager device
                    mac -- string -- The MAC of a network client device or a
                        Systems Manager device
                    serial -- string -- The serial of a Systems Manager
                        device
                    imei -- string -- The IMEI of a Systems Manager device
                    bluetooth_mac -- string -- The MAC of a Bluetooth client

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=options.get("network_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/pii/piiKeys'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'username': options.get('username', None),
            'email': options.get('email', None),
            'mac': options.get('mac', None),
            'serial': options.get('serial', None),
            'imei': options.get('imei', None),
            'bluetoothMac': options.get('bluetooth_mac', None)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_pii_sm_devices_for_key(self,
                                           options=dict()):
        """Does a GET request to /networks/{networkId}/pii/smDevicesForKey.

        Given a piece of Personally Identifiable Information (PII), return the
        Systems Manager device ID(s) associated with that identifier. These
        device IDs can be used with the Systems Manager API endpoints to
        retrieve device details. Exactly one identifier will be accepted.
        ## ALTERNATE PATH
        ```
        /organizations/{organizationId}/pii/smDevicesForKey
        ```

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    username -- string -- The username of a Systems Manager
                        user
                    email -- string -- The email of a network user account or
                        a Systems Manager device
                    mac -- string -- The MAC of a network client device or a
                        Systems Manager device
                    serial -- string -- The serial of a Systems Manager
                        device
                    imei -- string -- The IMEI of a Systems Manager device
                    bluetooth_mac -- string -- The MAC of a Bluetooth client

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=options.get("network_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/pii/smDevicesForKey'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'username': options.get('username', None),
            'email': options.get('email', None),
            'mac': options.get('mac', None),
            'serial': options.get('serial', None),
            'imei': options.get('imei', None),
            'bluetoothMac': options.get('bluetooth_mac', None)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_pii_sm_owners_for_key(self,
                                          options=dict()):
        """Does a GET request to /networks/{networkId}/pii/smOwnersForKey.

        Given a piece of Personally Identifiable Information (PII), return the
        Systems Manager owner ID(s) associated with that identifier. These
        owner IDs can be used with the Systems Manager API endpoints to
        retrieve owner details. Exactly one identifier will be accepted.
        ## ALTERNATE PATH
        ```
        /organizations/{organizationId}/pii/smOwnersForKey
        ```

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    username -- string -- The username of a Systems Manager
                        user
                    email -- string -- The email of a network user account or
                        a Systems Manager device
                    mac -- string -- The MAC of a network client device or a
                        Systems Manager device
                    serial -- string -- The serial of a Systems Manager
                        device
                    imei -- string -- The IMEI of a Systems Manager device
                    bluetooth_mac -- string -- The MAC of a Bluetooth client

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=options.get("network_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/pii/smOwnersForKey'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'username': options.get('username', None),
            'email': options.get('email', None),
            'mac': options.get('mac', None),
            'serial': options.get('serial', None),
            'imei': options.get('imei', None),
            'bluetoothMac': options.get('bluetooth_mac', None)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_pii_requests(self,
                                 network_id):
        """Does a GET request to /networks/{networkId}/pii/requests.

        List the PII requests for this network or organization
        ## ALTERNATE PATH
        ```
        /organizations/{organizationId}/pii/requests
        ```

        Args:
            network_id (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=network_id)

        # Prepare query URL
        _url_path = '/networks/{networkId}/pii/requests'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': network_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def create_network_pii_requests(self,
                                    options=dict()):
        """Does a POST request to /networks/{networkId}/pii/requests.

        Submit a new delete or restrict processing PII request
        ## ALTERNATE PATH
        ```
        /organizations/{organizationId}/pii/requests
        ```

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    create_network_pii_requests --
                        CreateNetworkPiiRequestsModel -- TODO: type
                        description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=options.get("network_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/pii/requests'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('create_network_pii_requests')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_pii_request(self,
                                options=dict()):
        """Does a GET request to /networks/{networkId}/pii/requests/{id}.

        Return a PII request
        ## ALTERNATE PATH
        ```
        /organizations/{organizationId}/pii/requests/{id}
        ```

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    id -- string -- TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=options.get("network_id"),
                                 id=options.get("id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/pii/requests/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'id': options.get('id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def delete_network_pii_request(self,
                                   options=dict()):
        """Does a DELETE request to /networks/{networkId}/pii/requests/{id}.

        Delete a restrict processing PII request
        ## ALTERNATE PATH
        ```
        /organizations/{organizationId}/pii/requests/{id}
        ```

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    id -- string -- TODO: type description here. Example: 

        Returns:
            void: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(network_id=options.get("network_id"),
                                 id=options.get("id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/pii/requests/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'id': options.get('id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)
