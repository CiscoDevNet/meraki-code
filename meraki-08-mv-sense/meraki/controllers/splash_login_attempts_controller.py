# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class SplashLoginAttemptsController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_network_splash_login_attempts(self,
                                          options=dict()):
        """Does a GET request to /networks/{id}/splashLoginAttempts.

        List the splash login attempts for a network

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- string -- TODO: type description here. Example: 
                    ssid_number -- string -- Only return the login attempts
                        for the specified SSID
                    login_identifier -- string -- The username, email, or
                        phone number used during login
                    timespan -- string -- The timespan, in seconds, for the
                        login attempts. The period will be from [timespan]
                        seconds ago until now. The maximum timespan is 3
                        months

        Returns:
            mixed: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(id=options.get("id"))

        # Prepare query URL
        _url_path = '/networks/{id}/splashLoginAttempts'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'id': options.get('id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'ssidNumber': options.get('ssid_number', None),
            'loginIdentifier': options.get('login_identifier', None),
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
