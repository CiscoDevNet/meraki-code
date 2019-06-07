# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class SMController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def create_network_sm_profile_clarity(self,
                                          options=dict()):
        """Does a POST request to /networks/{network_id}/sm/profile/clarity.

        Create a new profile containing a Cisco Clarity payload

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    create_network_sm_profile_clarity --
                        CreateNetworkSmProfileClarityModel -- TODO: type
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
        _url_path = '/networks/{network_id}/sm/profile/clarity'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('create_network_sm_profile_clarity')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def update_network_sm_profile_clarity(self,
                                          options=dict()):
        """Does a PUT request to /networks/{network_id}/sm/profile/clarity/{profileId}.

        Update an existing profile containing a Cisco Clarity payload

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    profile_id -- string -- TODO: type description here.
                        Example: 
                    update_network_sm_profile_clarity --
                        UpdateNetworkSmProfileClarityModel -- TODO: type
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
                                 profile_id=options.get("profile_id"))

        # Prepare query URL
        _url_path = '/networks/{network_id}/sm/profile/clarity/{profileId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'profileId': options.get('profile_id', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_sm_profile_clarity')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def add_network_sm_profile_clarity(self,
                                       options=dict()):
        """Does a POST request to /networks/{network_id}/sm/profile/clarity/{profileId}.

        Add a Cisco Clarity payload to an existing profile

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    profile_id -- string -- TODO: type description here.
                        Example: 
                    add_network_sm_profile_clarity --
                        AddNetworkSmProfileClarityModel -- TODO: type
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
                                 profile_id=options.get("profile_id"))

        # Prepare query URL
        _url_path = '/networks/{network_id}/sm/profile/clarity/{profileId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'profileId': options.get('profile_id', None)
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('add_network_sm_profile_clarity')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_sm_profile_clarity(self,
                                       options=dict()):
        """Does a GET request to /networks/{network_id}/sm/profile/clarity/{profileId}.

        Get details for a Cisco Clarity payload

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    profile_id -- string -- TODO: type description here.
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
                                 profile_id=options.get("profile_id"))

        # Prepare query URL
        _url_path = '/networks/{network_id}/sm/profile/clarity/{profileId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'profileId': options.get('profile_id', None)
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

    def delete_network_sm_profile_clarity(self,
                                          options=dict()):
        """Does a DELETE request to /networks/{network_id}/sm/profile/clarity/{profileId}.

        Delete a Cisco Clarity payload. Deletes the entire profile if it's
        empty after removing the payload.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    profile_id -- string -- TODO: type description here.
                        Example: 

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
                                 profile_id=options.get("profile_id"))

        # Prepare query URL
        _url_path = '/networks/{network_id}/sm/profile/clarity/{profileId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'profileId': options.get('profile_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def create_network_sm_profile_umbrella(self,
                                           options=dict()):
        """Does a POST request to /networks/{network_id}/sm/profile/umbrella.

        Create a new profile containing a Cisco Umbrella payload

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    create_network_sm_profile_umbrella --
                        CreateNetworkSmProfileUmbrellaModel -- TODO: type
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
        _url_path = '/networks/{network_id}/sm/profile/umbrella'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('create_network_sm_profile_umbrella')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def update_network_sm_profile_umbrella(self,
                                           options=dict()):
        """Does a PUT request to /networks/{network_id}/sm/profile/umbrella/{profileId}.

        Update an existing profile containing a Cisco Umbrella payload

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    profile_id -- string -- TODO: type description here.
                        Example: 
                    update_network_sm_profile_umbrella --
                        UpdateNetworkSmProfileUmbrellaModel -- TODO: type
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
                                 profile_id=options.get("profile_id"))

        # Prepare query URL
        _url_path = '/networks/{network_id}/sm/profile/umbrella/{profileId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'profileId': options.get('profile_id', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_sm_profile_umbrella')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def add_network_sm_profile_umbrella(self,
                                        options=dict()):
        """Does a POST request to /networks/{network_id}/sm/profile/umbrella/{profileId}.

        Add a Cisco Umbrella payload to an existing profile

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    profile_id -- string -- TODO: type description here.
                        Example: 
                    add_network_sm_profile_umbrella --
                        AddNetworkSmProfileUmbrellaModel -- TODO: type
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
                                 profile_id=options.get("profile_id"))

        # Prepare query URL
        _url_path = '/networks/{network_id}/sm/profile/umbrella/{profileId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'profileId': options.get('profile_id', None)
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('add_network_sm_profile_umbrella')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_sm_profile_umbrella(self,
                                        options=dict()):
        """Does a GET request to /networks/{network_id}/sm/profile/umbrella/{profileId}.

        Get details for a Cisco Umbrella payload

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    profile_id -- string -- TODO: type description here.
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
                                 profile_id=options.get("profile_id"))

        # Prepare query URL
        _url_path = '/networks/{network_id}/sm/profile/umbrella/{profileId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'profileId': options.get('profile_id', None)
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

    def delete_network_sm_profile_umbrella(self,
                                           options=dict()):
        """Does a DELETE request to /networks/{network_id}/sm/profile/umbrella/{profileId}.

        Delete a Cisco Umbrella payload. Deletes the entire profile if it's
        empty after removing the payload

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    profile_id -- string -- TODO: type description here.
                        Example: 

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
                                 profile_id=options.get("profile_id"))

        # Prepare query URL
        _url_path = '/networks/{network_id}/sm/profile/umbrella/{profileId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'profileId': options.get('profile_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def create_network_sm_app_polaris(self,
                                      options=dict()):
        """Does a POST request to /networks/{network_id}/sm/app/polaris.

        Create a new Polaris app

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    create_network_sm_app_polaris --
                        CreateNetworkSmAppPolarisModel -- TODO: type
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
        _url_path = '/networks/{network_id}/sm/app/polaris'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('create_network_sm_app_polaris')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_sm_app_polaris(self,
                                   options=dict()):
        """Does a GET request to /networks/{network_id}/sm/app/polaris.

        Get details for a Cisco Polaris app if it exists

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    bundle_id -- string -- The bundle ID of the app to be
                        found, defaults to com.cisco.ciscosecurity.app

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
        _url_path = '/networks/{network_id}/sm/app/polaris'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'bundleId': options.get('bundle_id', None)
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

    def update_network_sm_app_polari(self,
                                     options=dict()):
        """Does a PUT request to /networks/{network_id}/sm/app/polaris/{appId}.

        Update an existing Polaris app

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    app_id -- string -- TODO: type description here. Example:
                                            update_network_sm_app_polari --
                        UpdateNetworkSmAppPolariModel -- TODO: type
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
                                 app_id=options.get("app_id"))

        # Prepare query URL
        _url_path = '/networks/{network_id}/sm/app/polaris/{appId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'appId': options.get('app_id', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_sm_app_polari')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def delete_network_sm_app_polari(self,
                                     options=dict()):
        """Does a DELETE request to /networks/{network_id}/sm/app/polaris/{appId}.

        Delete a Cisco Polaris app

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    app_id -- string -- TODO: type description here. Example:
                        
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
                                 app_id=options.get("app_id"))

        # Prepare query URL
        _url_path = '/networks/{network_id}/sm/app/polaris/{appId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'appId': options.get('app_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def get_network_sm_devices(self,
                               options=dict()):
        """Does a GET request to /networks/{network_id}/sm/devices.

        List the devices enrolled in an SM network with various specified
        fields and filters

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    fields -- string -- Additional fields that will be
                        displayed for each device. Multiple fields can be
                        passed in as comma separated values.       The default
                        fields are: id, name, tags, ssid, wifiMac, osName,
                        systemModel, uuid, and serialNumber. The additional
                        fields are: ip,       systemType,
                        availableDeviceCapacity, kioskAppName, biosVersion,
                        lastConnected, missingAppsCount, userSuppliedAddress,
                        location, lastUser,       ownerEmail, ownerUsername,
                        publicIp, phoneNumber, diskInfoJson, deviceCapacity,
                        isManaged, hadMdm, isSupervised, meid, imei, iccid,   
                        simCarrierNetwork, cellularDataUsed, isHotspotEnabled,
                        createdAt, batteryEstCharge, quarantined, avName,
                        avRunning, asName, fwName,       isRooted,
                        loginRequired, screenLockEnabled, screenLockDelay,
                        autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent,
                        diskEncryptionEnabled,       hardwareEncryptionCaps,
                        passCodeLock, usesHardwareKeystore, and
                        androidSecurityPatchVersion.
                    wifi_macs -- string -- Filter devices by wifi mac(s).
                        Multiple wifi macs can be passed in as comma separated
                        values.
                    serials -- string -- Filter devices by serial(s). Multiple
                        serials can be passed in as comma separated values.
                    ids -- string -- Filter devices by id(s). Multiple ids can
                        be passed in as comma separated values.
                    scope -- string -- Specify a scope (one of all, none,
                        withAny, withAll, withoutAny, or withoutAll) and a set
                        of tags as comma separated values.
                    batch_token -- string -- On networks with more than 1000
                        devices, the device list will be limited to 1000
                        devices per query.       If there are more devices to
                        be seen, a batch token will be returned as a part of
                        the device list. To see the remainder of       the
                        devices, pass in the batchToken as a parameter in the
                        next request. Requests made with the batchToken do not
                        require       additional parameters as the batchToken
                        includes the parameters passed in with the original
                        request. Additional parameters       passed in with
                        the batchToken will be ignored.

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
        _url_path = '/networks/{network_id}/sm/devices'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'fields': options.get('fields', None),
            'wifiMacs': options.get('wifi_macs', None),
            'serials': options.get('serials', None),
            'ids': options.get('ids', None),
            'scope': options.get('scope', None),
            'batchToken': options.get('batch_token', None)
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

    def get_network_sm_users(self,
                             options=dict()):
        """Does a GET request to /networks/{network_id}/sm/users.

        List the owners in an SM network with various specified fields and
        filters

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    usernames -- string -- Filter users by username(s).
                        Multiple usernames can be passed in as comma separated
                        values.
                    emails -- string -- Filter users by email(s). Multiple
                        emails can be passed in as comma separated values.
                    ids -- string -- Filter users by id(s). Multiple ids can
                        be passed in as comma separated values.
                    scope -- string -- Specify a scope (one of all, none,
                        withAny, withAll, withoutAny, or withoutAll) and a set
                        of tags as comma separated values.

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
        _url_path = '/networks/{network_id}/sm/users'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'usernames': options.get('usernames', None),
            'emails': options.get('emails', None),
            'ids': options.get('ids', None),
            'scope': options.get('scope', None)
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

    def get_network_sm_user_device_profiles(self,
                                            options=dict()):
        """Does a GET request to /networks/{network_id}/sm/user/{id}/deviceProfiles.

        Get the profiles associated with a user

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
        _url_path = '/networks/{network_id}/sm/user/{id}/deviceProfiles'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
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

    def get_network_sm_device_profiles(self,
                                       options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/deviceProfiles.

        Get the profiles associated with a device

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
        _url_path = '/networks/{network_id}/sm/{id}/deviceProfiles'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
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

    def get_network_sm_user_softwares(self,
                                      options=dict()):
        """Does a GET request to /networks/{network_id}/sm/user/{id}/softwares.

        Get a list of softwares associated with a user

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
        _url_path = '/networks/{network_id}/sm/user/{id}/softwares'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
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

    def get_network_sm_softwares(self,
                                 options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/softwares.

        Get a list of softwares associated with a device

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
        _url_path = '/networks/{network_id}/sm/{id}/softwares'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
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

    def get_network_sm_network_adapters(self,
                                        options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/networkAdapters.

        List the network adapters of a device

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
        _url_path = '/networks/{network_id}/sm/{id}/networkAdapters'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
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

    def get_network_sm_wlan_lists(self,
                                  options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/wlanLists.

        List the saved SSID names on a device

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
        _url_path = '/networks/{network_id}/sm/{id}/wlanLists'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
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

    def get_network_sm_security_centers(self,
                                        options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/securityCenters.

        List the security centers on a device

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
        _url_path = '/networks/{network_id}/sm/{id}/securityCenters'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
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

    def get_network_sm_restrictions(self,
                                    options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/restrictions.

        List the restrictions on a device

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
        _url_path = '/networks/{network_id}/sm/{id}/restrictions'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
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

    def get_network_sm_certs(self,
                             options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/certs.

        List the certs on a device

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
        _url_path = '/networks/{network_id}/sm/{id}/certs'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
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

    def update_network_sm_devices_tags(self,
                                       options=dict()):
        """Does a PUT request to /networks/{network_id}/sm/devices/tags.

        Add, delete, or update the tags of a set of devices

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_sm_devices_tags --
                        UpdateNetworkSmDevicesTagsModel -- TODO: type
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
        _url_path = '/networks/{network_id}/sm/devices/tags'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_sm_devices_tags')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def update_network_sm_device_fields(self,
                                        options=dict()):
        """Does a PUT request to /networks/{network_id}/sm/device/fields.

        Modify the fields of a device

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_sm_device_fields --
                        UpdateNetworkSmDeviceFieldsModel -- TODO: type
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
        _url_path = '/networks/{network_id}/sm/device/fields'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_sm_device_fields')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def update_network_sm_devices_lock(self,
                                       options=dict()):
        """Does a PUT request to /networks/{network_id}/sm/devices/lock.

        Lock a set of devices

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_sm_devices_lock --
                        UpdateNetworkSmDevicesLockModel -- TODO: type
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
        _url_path = '/networks/{network_id}/sm/devices/lock'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_sm_devices_lock')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def update_network_sm_device_wipe(self,
                                      options=dict()):
        """Does a PUT request to /networks/{network_id}/sm/device/wipe.

        Wipe a device

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_sm_device_wipe --
                        UpdateNetworkSmDeviceWipeModel -- TODO: type
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
        _url_path = '/networks/{network_id}/sm/device/wipe'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_sm_device_wipe')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def update_network_sm_devices_checkin(self,
                                          options=dict()):
        """Does a PUT request to /networks/{network_id}/sm/devices/checkin.

        Force check-in a set of devices

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_sm_devices_checkin --
                        UpdateNetworkSmDevicesCheckinModel -- TODO: type
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
        _url_path = '/networks/{network_id}/sm/devices/checkin'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_sm_devices_checkin')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def update_network_sm_devices_move(self,
                                       options=dict()):
        """Does a PUT request to /networks/{network_id}/sm/devices/move.

        Move a set of devices to a new network

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    update_network_sm_devices_move --
                        UpdateNetworkSmDevicesMoveModel -- TODO: type
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
        _url_path = '/networks/{network_id}/sm/devices/move'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_network_sm_devices_move')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def unenroll_network_sm_device(self,
                                   options=dict()):
        """Does a POST request to /networks/{network_id}/sm/devices/{deviceId}/unenroll.

        Unenroll a device

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    device_id -- string -- TODO: type description here.
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
                                 device_id=options.get("device_id"))

        # Prepare query URL
        _url_path = '/networks/{network_id}/sm/devices/{deviceId}/unenroll'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'deviceId': options.get('device_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_sm_profiles(self,
                                network_id):
        """Does a GET request to /networks/{network_id}/sm/profiles.

        List all the profiles in the network

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
        _url_path = '/networks/{network_id}/sm/profiles'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': network_id
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

    def get_network_sm_cellular_usage_history(self,
                                              options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/cellularUsageHistory.

        Return the client's daily cellular data usage history. Usage data is
        in kilobytes.

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
        _url_path = '/networks/{network_id}/sm/{id}/cellularUsageHistory'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
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

    def get_network_sm_performance_history(self,
                                           options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/performanceHistory.

        Return historical records of various Systems Manager client metrics
        for desktop devices.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    id -- string -- TODO: type description here. Example: 
                    per_page -- string -- The number of entries per page
                        returned
                    starting_after -- string -- A token used by the server to
                        indicate the start of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, next or
                        prev page in the HTTP Link header should define it.
                    ending_before -- string -- A token used by the server to
                        indicate the end of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, next or
                        prev page in the HTTP Link header should define it.

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
        _url_path = '/networks/{network_id}/sm/{id}/performanceHistory'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'id': options.get('id', None)
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

    def get_network_sm_desktop_logs(self,
                                    options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/desktopLogs.

        Return historical records of various Systems Manager network
        connection details for desktop devices.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    id -- string -- TODO: type description here. Example: 
                    per_page -- string -- The number of entries per page
                        returned
                    starting_after -- string -- A token used by the server to
                        indicate the start of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, next or
                        prev page in the HTTP Link header should define it.
                    ending_before -- string -- A token used by the server to
                        indicate the end of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, next or
                        prev page in the HTTP Link header should define it.

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
        _url_path = '/networks/{network_id}/sm/{id}/desktopLogs'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'id': options.get('id', None)
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

    def get_network_sm_device_command_logs(self,
                                           options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/deviceCommandLogs.

            Return historical records of commands sent to Systems Manager
            devices.
            <p>Note that this will include the name of the Dashboard user who
            initiated the command if it was generated
            by a Dashboard admin rather than the automatic behavior of the
            system; you may wish to filter this out
            of any reports.</p>

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    id -- string -- TODO: type description here. Example: 
                    per_page -- string -- The number of entries per page
                        returned
                    starting_after -- string -- A token used by the server to
                        indicate the start of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, next or
                        prev page in the HTTP Link header should define it.
                    ending_before -- string -- A token used by the server to
                        indicate the end of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, next or
                        prev page in the HTTP Link header should define it.

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
        _url_path = '/networks/{network_id}/sm/{id}/deviceCommandLogs'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'id': options.get('id', None)
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

    def get_network_sm_connectivity(self,
                                    options=dict()):
        """Does a GET request to /networks/{network_id}/sm/{id}/connectivity.

        Returns historical connectivity data (whether a device is regularly
        checking in to Dashboard).

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    id -- string -- TODO: type description here. Example: 
                    per_page -- string -- The number of entries per page
                        returned
                    starting_after -- string -- A token used by the server to
                        indicate the start of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, next or
                        prev page in the HTTP Link header should define it.
                    ending_before -- string -- A token used by the server to
                        indicate the end of the page. Often this is a
                        timestamp or an ID but it is not limited to those.
                        This parameter should not be defined by client
                        applications. The link for the first, last, next or
                        prev page in the HTTP Link header should define it.

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
        _url_path = '/networks/{network_id}/sm/{id}/connectivity'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'network_id': options.get('network_id', None),
            'id': options.get('id', None)
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
