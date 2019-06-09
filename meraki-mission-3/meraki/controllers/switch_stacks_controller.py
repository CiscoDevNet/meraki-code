# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class SwitchStacksController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_network_switch_stacks(self,
                                  network_id):
        """Does a GET request to /networks/{networkId}/switchStacks.

        List the switch stacks in a network

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
        _url_path = '/networks/{networkId}/switchStacks'
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

    def create_network_switch_stacks(self,
                                     options=dict()):
        """Does a POST request to /networks/{networkId}/switchStacks.

        Create a stack

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    create_network_switch_stacks --
                        CreateNetworkSwitchStacksModel -- TODO: type
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
                                 create_network_switch_stacks=options.get("create_network_switch_stacks"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switchStacks'
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('create_network_switch_stacks')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_network_switch_stack(self,
                                 options=dict()):
        """Does a GET request to /networks/{networkId}/switchStacks/{switchStackId}.

        Show a switch stack

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    switch_stack_id -- string -- TODO: type description here.
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
                                 switch_stack_id=options.get("switch_stack_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switchStacks/{switchStackId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'switchStackId': options.get('switch_stack_id', None)
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

    def delete_network_switch_stack(self,
                                    options=dict()):
        """Does a DELETE request to /networks/{networkId}/switchStacks/{switchStackId}.

        Delete a stack

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    switch_stack_id -- string -- TODO: type description here.
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
                                 switch_stack_id=options.get("switch_stack_id"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switchStacks/{switchStackId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'switchStackId': options.get('switch_stack_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def add_network_switch_stack(self,
                                 options=dict()):
        """Does a POST request to /networks/{networkId}/switchStacks/{switchStackId}/add.

        Add a switch to a stack

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    switch_stack_id -- string -- TODO: type description here.
                        Example: 
                    add_network_switch_stack -- AddNetworkSwitchStackModel --
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
        self.validate_parameters(network_id=options.get("network_id"),
                                 switch_stack_id=options.get("switch_stack_id"),
                                 add_network_switch_stack=options.get("add_network_switch_stack"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/switchStacks/{switchStackId}/add'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'switchStackId': options.get('switch_stack_id', None)
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('add_network_switch_stack')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def remove_network_switch_stack(self,
                                    options=dict()):
        """Does a POST request to /networks/{networkID}/switchStacks/{switchStackId}/remove.

        Remove a switch from a stack

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    switch_stack_id -- string -- TODO: type description here.
                        Example: 
                    remove_network_switch_stack --
                        RemoveNetworkSwitchStackModel -- TODO: type
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
                                 switch_stack_id=options.get("switch_stack_id"),
                                 remove_network_switch_stack=options.get("remove_network_switch_stack"))

        # Prepare query URL
        _url_path = '/networks/{networkID}/switchStacks/{switchStackId}/remove'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkID': options.get('network_id', None),
            'switchStackId': options.get('switch_stack_id', None)
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('remove_network_switch_stack')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)
