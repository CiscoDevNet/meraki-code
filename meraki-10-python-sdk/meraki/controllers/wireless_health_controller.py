# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class WirelessHealthController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_network_connection_stats(self,
                                     options=dict()):
        """Does a GET request to /networks/{networkId}/connectionStats.

        Aggregated connectivity info for this network

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    t_0 -- string -- Start of the requested time range in
                        seconds since epoch (Required)
                    t_1 -- string -- End of the requested time range in
                        seconds since epoch (Required)
                    ssid -- string -- Filter results by SSID
                    vlan -- string -- Filter results by VLAN
                    ap_tag -- string -- Filter results by AP Tag

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
        _url_path = '/networks/{networkId}/connectionStats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'ssid': options.get('ssid', None),
            'vlan': options.get('vlan', None),
            'apTag': options.get('ap_tag', None)
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

    def get_network_devices_connection_stats(self,
                                             options=dict()):
        """Does a GET request to /networks/{networkId}/devices/connectionStats.

        Aggregated connectivity info for this network, grouped by node

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    t_0 -- string -- Start of the requested time range in
                        seconds since epoch (Required)
                    t_1 -- string -- End of the requested time range in
                        seconds since epoch (Required)
                    ssid -- string -- Filter results by SSID
                    vlan -- string -- Filter results by VLAN
                    ap_tag -- string -- Filter results by AP Tag

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
        _url_path = '/networks/{networkId}/devices/connectionStats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'ssid': options.get('ssid', None),
            'vlan': options.get('vlan', None),
            'apTag': options.get('ap_tag', None)
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

    def get_network_device_connection_stats(self,
                                            options=dict()):
        """Does a GET request to /networks/{networkId}/devices/{serial}/connectionStats.

        Aggregated connectivity info for a given AP on this network

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    serial -- string -- TODO: type description here. Example:
                                            t_0 -- string -- Start of the requested time range in
                        seconds since epoch (Required)
                    t_1 -- string -- End of the requested time range in
                        seconds since epoch (Required)
                    ssid -- string -- Filter results by SSID
                    vlan -- string -- Filter results by VLAN
                    ap_tag -- string -- Filter results by AP Tag

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
                                 serial=options.get("serial"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/devices/{serial}/connectionStats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'serial': options.get('serial', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'ssid': options.get('ssid', None),
            'vlan': options.get('vlan', None),
            'apTag': options.get('ap_tag', None)
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

    def get_network_clients_connection_stats(self,
                                             options=dict()):
        """Does a GET request to /networks/{networkId}/clients/connectionStats.

        Aggregated connectivity info for this network, grouped by clients

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    t_0 -- string -- Start of the requested time range in
                        seconds since epoch (Required)
                    t_1 -- string -- End of the requested time range in
                        seconds since epoch (Required)
                    ssid -- string -- Filter results by SSID
                    vlan -- string -- Filter results by VLAN
                    ap_tag -- string -- Filter results by AP Tag

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
        _url_path = '/networks/{networkId}/clients/connectionStats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'ssid': options.get('ssid', None),
            'vlan': options.get('vlan', None),
            'apTag': options.get('ap_tag', None)
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

    def get_network_client_connection_stats(self,
                                            options=dict()):
        """Does a GET request to /networks/{networkId}/clients/{clientId}/connectionStats.

        Aggregated connectivity info for a given client on this network

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    client_id -- string -- TODO: type description here.
                        Example: 
                    t_0 -- string -- Start of the requested time range in
                        seconds since epoch (Required)
                    t_1 -- string -- End of the requested time range in
                        seconds since epoch (Required)
                    ssid -- string -- Filter results by SSID
                    vlan -- string -- Filter results by VLAN
                    ap_tag -- string -- Filter results by AP Tag

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
                                 client_id=options.get("client_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/clients/{clientId}/connectionStats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'clientId': options.get('client_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'ssid': options.get('ssid', None),
            'vlan': options.get('vlan', None),
            'apTag': options.get('ap_tag', None)
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

    def get_network_latency_stats(self,
                                  options=dict()):
        """Does a GET request to /networks/{networkId}/latencyStats.

        Aggregated latency info for this network

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    t_0 -- string -- Start of the requested time range in
                        seconds since epoch (Required)
                    t_1 -- string -- End of the requested time range in
                        seconds since epoch (Required)
                    ssid -- string -- Filter results by SSID
                    vlan -- string -- Filter results by VLAN
                    ap_tag -- string -- Filter results by AP Tag
                    fields -- string -- Partial selection: If present, this
                        call will return only the selected fields of
                        ["rawDistribution", "avg"]. All fields will be
                        returned by default. Selected fields must be entered
                        as a comma separated string.

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
        _url_path = '/networks/{networkId}/latencyStats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'ssid': options.get('ssid', None),
            'vlan': options.get('vlan', None),
            'apTag': options.get('ap_tag', None),
            'fields': options.get('fields', None)
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

    def get_network_devices_latency_stats(self,
                                          options=dict()):
        """Does a GET request to /networks/{networkId}/devices/latencyStats.

        Aggregated latency info for this network, grouped by node

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    t_0 -- string -- Start of the requested time range in
                        seconds since epoch (Required)
                    t_1 -- string -- End of the requested time range in
                        seconds since epoch (Required)
                    ssid -- string -- Filter results by SSID
                    vlan -- string -- Filter results by VLAN
                    ap_tag -- string -- Filter results by AP Tag
                    fields -- string -- Partial selection: If present, this
                        call will return only the selected fields of
                        ["rawDistribution", "avg"]. All fields will be
                        returned by default. Selected fields must be entered
                        as a comma separated string.

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
        _url_path = '/networks/{networkId}/devices/latencyStats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'ssid': options.get('ssid', None),
            'vlan': options.get('vlan', None),
            'apTag': options.get('ap_tag', None),
            'fields': options.get('fields', None)
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

    def get_network_device_latency_stats(self,
                                         options=dict()):
        """Does a GET request to /networks/{networkId}/devices/{serial}/latencyStats.

        Aggregated latency info for a given AP on this network

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    serial -- string -- TODO: type description here. Example:
                                            t_0 -- string -- Start of the requested time range in
                        seconds since epoch (Required)
                    t_1 -- string -- End of the requested time range in
                        seconds since epoch (Required)
                    ssid -- string -- Filter results by SSID
                    vlan -- string -- Filter results by VLAN
                    ap_tag -- string -- Filter results by AP Tag
                    fields -- string -- Partial selection: If present, this
                        call will return only the selected fields of
                        ["rawDistribution", "avg"]. All fields will be
                        returned by default. Selected fields must be entered
                        as a comma separated string.

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
                                 serial=options.get("serial"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/devices/{serial}/latencyStats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'serial': options.get('serial', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'ssid': options.get('ssid', None),
            'vlan': options.get('vlan', None),
            'apTag': options.get('ap_tag', None),
            'fields': options.get('fields', None)
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

    def get_network_clients_latency_stats(self,
                                          options=dict()):
        """Does a GET request to /networks/{networkId}/clients/latencyStats.

        Aggregated latency info for this network, grouped by clients

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    t_0 -- string -- Start of the requested time range in
                        seconds since epoch (Required)
                    t_1 -- string -- End of the requested time range in
                        seconds since epoch (Required)
                    ssid -- string -- Filter results by SSID
                    vlan -- string -- Filter results by VLAN
                    ap_tag -- string -- Filter results by AP Tag
                    fields -- string -- Partial selection: If present, this
                        call will return only the selected fields of
                        ["rawDistribution", "avg"]. All fields will be
                        returned by default. Selected fields must be entered
                        as a comma separated string.

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
        _url_path = '/networks/{networkId}/clients/latencyStats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'ssid': options.get('ssid', None),
            'vlan': options.get('vlan', None),
            'apTag': options.get('ap_tag', None),
            'fields': options.get('fields', None)
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

    def get_network_client_latency_stats(self,
                                         options=dict()):
        """Does a GET request to /networks/{networkId}/clients/{clientId}/latencyStats.

        Aggregated latency info for a given client on this network

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    client_id -- string -- TODO: type description here.
                        Example: 
                    t_0 -- string -- Start of the requested time range in
                        seconds since epoch (Required)
                    t_1 -- string -- End of the requested time range in
                        seconds since epoch (Required)
                    ssid -- string -- Filter results by SSID
                    vlan -- string -- Filter results by VLAN
                    ap_tag -- string -- Filter results by AP Tag
                    fields -- string -- Partial selection: If present, this
                        call will return only the selected fields of
                        ["rawDistribution", "avg"]. All fields will be
                        returned by default. Selected fields must be entered
                        as a comma separated string.

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
                                 client_id=options.get("client_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/clients/{clientId}/latencyStats'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'clientId': options.get('client_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'ssid': options.get('ssid', None),
            'vlan': options.get('vlan', None),
            'apTag': options.get('ap_tag', None),
            'fields': options.get('fields', None)
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

    def get_network_failed_connections(self,
                                       options=dict()):
        """Does a GET request to /networks/{networkId}/failedConnections.

        List of all failed client connection events on this network in a given
        time range

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    t_0 -- string -- Start of the requested time range in
                        seconds since epoch (Required)
                    t_1 -- string -- End of the requested time range in
                        seconds since epoch (Required)
                    ssid -- string -- Filter results by SSID
                    vlan -- string -- Filter results by VLAN
                    ap_tag -- string -- Filter results by AP Tag
                    serial -- string -- Filter by AP
                    client_id -- string -- Filter by client

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
        _url_path = '/networks/{networkId}/failedConnections'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'ssid': options.get('ssid', None),
            'vlan': options.get('vlan', None),
            'apTag': options.get('ap_tag', None),
            'serial': options.get('serial', None),
            'clientId': options.get('client_id', None)
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
