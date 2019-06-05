# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class ClientSecurityEventsController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_network_client_security_events(self,
                                           options=dict()):
        """Does a GET request to /networks/{networkId}/clients/{clientId}/securityEvents.

        List the security events

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
                    per_page -- int -- The number of entries per page
                        returned. Acceptable range is 3 - 1000.
                    t_0 -- string -- The beginning of the timespan for the
                        data. The maximum lookback period is 791 days from
                        today.
                    t_1 -- string -- The end of the timespan for the data. t1
                        can be a maximum of 791 days after t0.
                    timespan -- int -- The timespan for which the information
                        will be fetched. If specifying timespan, do not
                        specify parameters t0 and t1. The value must be in
                        seconds and be less than or equal to 791 days. The
                        default is 31 days.
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
                                 client_id=options.get("client_id"),
                                 per_page=options.get("per_page"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/clients/{clientId}/securityEvents'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'clientId': options.get('client_id', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'perPage': options.get('per_page', None),
            't0': options.get('t0', None),
            't1': options.get('t1', None),
            'timespan': options.get('timespan', None),
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
