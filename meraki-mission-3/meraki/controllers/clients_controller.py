# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class ClientsController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_network_client(self,
                           options=dict()):
        """Does a GET request to /networks/{networkId}/clients/{idOrMacOrIp}.

        Return the client associated with the given identifier. This endpoint
        will lookup by client ID or either the MAC or IP depending on whether
        the network uses Track-by-IP.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    id_or_mac_or_ip -- string -- TODO: type description here.
                        Example: 

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
                                 id_or_mac_or_ip=options.get("id_or_mac_or_ip"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/clients/{idOrMacOrIp}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'idOrMacOrIp': options.get('id_or_mac_or_ip', None)
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

    def provision_network_clients(self,
                                  options=dict()):
        """Does a POST request to /networks/{networkId}/clients/provision.

        Provisions a client with a name and policy. Clients can be provisioned
        before they associate to the network.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    provision_network_clients -- ProvisionNetworkClientsModel
                        -- TODO: type description here. Example: 

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
        _url_path = '/networks/{networkId}/clients/provision'
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('provision_network_clients')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_client_usage_history(self,
                                         options=dict()):
        """Does a GET request to /networks/{networkId}/clients/{idOrMacOrIp}/usageHistory.

        Return the client's daily usage history. Usage data is in kilobytes.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    id_or_mac_or_ip -- string -- TODO: type description here.
                        Example: 

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
                                 id_or_mac_or_ip=options.get("id_or_mac_or_ip"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/clients/{idOrMacOrIp}/usageHistory'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'idOrMacOrIp': options.get('id_or_mac_or_ip', None)
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

    def get_network_client_policy(self,
                                  options=dict()):
        """Does a GET request to /networks/{networkId}/clients/{mac}/policy.

        Return the policy assigned to a client on the network.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    mac -- string -- TODO: type description here. Example: 
                    timespan -- string -- The timespan for which clients will
                        be fetched. Must be in seconds and less than or equal
                        to a month (2592000 seconds).

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
                                 mac=options.get("mac"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/clients/{mac}/policy'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'mac': options.get('mac', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'timespan': options.get('timespan', None)
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

    def update_network_client_policy(self,
                                     options=dict()):
        """Does a PUT request to /networks/{networkId}/clients/{mac}/policy.

        Update the policy assigned to a client on the network.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    mac -- string -- TODO: type description here. Example: 
                    update_network_client_policy --
                        UpdateNetworkClientPolicyModel -- TODO: type
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
        self.validate_parameters(network_id=options.get("network_id"),
                                 mac=options.get("mac"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/clients/{mac}/policy'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'mac': options.get('mac', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_client_policy')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_client_splash_authorization_status(self,
                                                       options=dict()):
        """Does a GET request to /networks/{id}/clients/{mac}/splashAuthorizationStatus.

        Return the splash authorization for a client, for each SSID they've
        associated with through splash.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- string -- TODO: type description here. Example: 
                    mac -- string -- TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=options.get("id"),
                                 mac=options.get("mac"))

        # Prepare query URL
        _url_path = '/networks/{id}/clients/{mac}/splashAuthorizationStatus'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'id': options.get('id', None),
            'mac': options.get('mac', None)
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

    def update_network_client_splash_authorization_status(self,
                                                          options=dict()):
        """Does a PUT request to /networks/{id}/clients/{mac}/splashAuthorizationStatus.

        Update a client's splash authorization.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- string -- TODO: type description here. Example: 
                    mac -- string -- TODO: type description here. Example: 
                    update_network_client_splash_authorization_status --
                        UpdateNetworkClientSplashAuthorizationStatusModel --
                        TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=options.get("id"),
                                 mac=options.get("mac"))

        # Prepare query URL
        _url_path = '/networks/{id}/clients/{mac}/splashAuthorizationStatus'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'id': options.get('id', None),
            'mac': options.get('mac', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_client_splash_authorization_status')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_device_clients(self,
                           options=dict()):
        """Does a GET request to /devices/{serial}/clients.

        List the clients of a device, up to a maximum of a month ago. The
        usage of each client is returned in kilobytes. If the device is a
        switch, the switchport is returned; otherwise the switchport field is
        null.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    serial -- string -- TODO: type description here. Example:
                                            t_0 -- string -- The beginning of the timespan for the
                        data. The maximum lookback period is 31 days from
                        today.
                    timespan -- int -- The timespan for which the information
                        will be fetched. If specifying timespan, do not
                        specify parameter t0. The value must be in seconds and
                        be less than or equal to 31 days. The default is 1
                        day.

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(serial=options.get("serial"))

        # Prepare query URL
        _url_path = '/devices/{serial}/clients'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'serial': options.get('serial', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            'timespan': options.get('timespan', None)
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

    def get_network_client_traffic_history(self,
                                           options=dict()):
        """Does a GET request to /networks/{networkId}/clients/{idOrMacOrIp}/trafficHistory.

        Return the client's network traffic data over time. Usage data is in
        kilobytes. This endpoint requires detailed traffic analysis to be
        enabled on the Network-wide > General page.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    id_or_mac_or_ip -- string -- TODO: type description here.
                        Example: 
                    per_page -- int -- The number of entries per page
                        returned. Acceptable range is 3 - 1000.
                    starting_after -- string -- A token used by the server to
                        indicate the start of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, prev, or
                        next page in the HTTP Link header should define it.
                    ending_before -- string -- A token used by the server to
                        indicate the end of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, prev, or
                        next page in the HTTP Link header should define it.

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
                                 id_or_mac_or_ip=options.get("id_or_mac_or_ip"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/clients/{idOrMacOrIp}/trafficHistory'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'idOrMacOrIp': options.get('id_or_mac_or_ip', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'perPage': options.get('per_page', None),
            'startingAfter': options.get('starting_after', None),
            'endingBefore': options.get('ending_before', None)
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

    def get_network_client_events(self,
                                  options=dict()):
        """Does a GET request to /networks/{networkId}/clients/{idOrMacOrIp}/events.

        Return the events associated with this client

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    id_or_mac_or_ip -- string -- TODO: type description here.
                        Example: 
                    per_page -- int -- The number of entries per page
                        returned. Acceptable range is 3 - 100. Default is
                        100.
                    starting_after -- string -- A token used by the server to
                        indicate the start of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, prev, or
                        next page in the HTTP Link header should define it.
                    ending_before -- string -- A token used by the server to
                        indicate the end of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, prev, or
                        next page in the HTTP Link header should define it.

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
                                 id_or_mac_or_ip=options.get("id_or_mac_or_ip"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/clients/{idOrMacOrIp}/events'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'idOrMacOrIp': options.get('id_or_mac_or_ip', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'perPage': options.get('per_page', None),
            'startingAfter': options.get('starting_after', None),
            'endingBefore': options.get('ending_before', None)
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

    def get_network_client_latency_history(self,
                                           options=dict()):
        """Does a GET request to /networks/{networkId}/clients/{idOrMacOrIp}/latencyHistory.

        Return the latency history for a client. The latency data is from a
        sample of 2% of packets and is grouped into 4 traffic categories:
        background, best effort, video, voice. Within these categories the
        sampled packet counters are bucketed by latency in milliseconds.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    id_or_mac_or_ip -- string -- TODO: type description here.
                        Example: 
                    t_0 -- string -- The beginning of the timespan for the
                        data. The maximum lookback period is 791 days from
                        today.
                    t_1 -- string -- The end of the timespan for the data. t1
                        can be a maximum of 791 days after t0.
                    timespan -- int -- The timespan for which the information
                        will be fetched. If specifying timespan, do not
                        specify parameters t0 and t1. The value must be in
                        seconds and be less than or equal to 791 days. The
                        default is 1 day.
                    resolution -- int -- The time resolution in seconds for
                        returned data. The valid resolutions are: 86400. The
                        default is 86400.

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
                                 id_or_mac_or_ip=options.get("id_or_mac_or_ip"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/clients/{idOrMacOrIp}/latencyHistory'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'idOrMacOrIp': options.get('id_or_mac_or_ip', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'timespan': options.get('timespan', None),
            'resolution': options.get('resolution', None)
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
