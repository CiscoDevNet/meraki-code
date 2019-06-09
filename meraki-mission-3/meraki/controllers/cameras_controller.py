# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class CamerasController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_network_camera_video_link(self,
                                      options=dict()):
        """Does a GET request to /networks/{networkId}/cameras/{serial}/videoLink.

        Returns video link for the specified camera. If a timestamp supplied,
        it links to that time.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    serial -- string -- TODO: type description here. Example:
                                            timestamp -- string -- The video link will start at this
                        timestamp. The timestamp is in UNIX Epoch time
                        (milliseconds).

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
        _url_path = '/networks/{networkId}/cameras/{serial}/videoLink'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'serial': options.get('serial', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'timestamp': options.get('timestamp', None)
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

    def snapshot_network_camera(self,
                                options=dict()):
        """Does a POST request to /networks/{networkId}/cameras/{serial}/snapshot.

        Generate a snapshot of what the camera sees at the specified time and
        return a link to that image.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    network_id -- string -- TODO: type description here.
                        Example: 
                    serial -- string -- TODO: type description here. Example:
                                            snapshot_network_camera -- SnapshotNetworkCameraModel --
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
                                 serial=options.get("serial"))

        # Prepare query URL
        _url_path = '/networks/{networkId}/cameras/{serial}/snapshot'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'networkId': options.get('network_id', None),
            'serial': options.get('serial', None)
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
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('snapshot_network_camera')))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)
