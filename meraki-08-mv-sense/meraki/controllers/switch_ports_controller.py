# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class SwitchPortsController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_device_switch_ports(self,
                                serial):
        """Does a GET request to /devices/{serial}/switchPorts.

        List the switch ports for a switch

        Args:
            serial (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(serial=serial)

        # Prepare query URL
        _url_path = '/devices/{serial}/switchPorts'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'serial': serial
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

    def get_device_switch_port(self,
                               options=dict()):
        """Does a GET request to /devices/{serial}/switchPorts/{number}.

        Return a switch port

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    serial -- string -- TODO: type description here. Example:
                                            number -- string -- TODO: type description here. Example:
                        
        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(serial=options.get("serial"),
                                 number=options.get("number"))

        # Prepare query URL
        _url_path = '/devices/{serial}/switchPorts/{number}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'serial': options.get('serial', None),
            'number': options.get('number', None)
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

    def update_device_switch_port(self,
                                  options=dict()):
        """Does a PUT request to /devices/{serial}/switchPorts/{number}.

        Update a switch port

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    serial -- string -- TODO: type description here. Example:
                                            number -- string -- TODO: type description here. Example:
                                            update_device_switch_port -- UpdateDeviceSwitchPortModel
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
        self.validate_parameters(serial=options.get("serial"),
                                 number=options.get("number"))

        # Prepare query URL
        _url_path = '/devices/{serial}/switchPorts/{number}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'serial': options.get('serial', None),
            'number': options.get('number', None)
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('update_device_switch_port')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)
