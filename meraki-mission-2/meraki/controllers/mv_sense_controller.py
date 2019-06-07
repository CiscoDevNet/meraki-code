# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

from meraki.api_helper import APIHelper
from meraki.configuration import Configuration
from meraki.controllers.base_controller import BaseController
from meraki.http.auth.custom_header_auth import CustomHeaderAuth

class MVSenseController(BaseController):

    """A Controller to access Endpoints in the meraki API."""


    def get_device_camera_analytics_zones(self,
                                          serial):
        """Does a GET request to /devices/{serial}/camera/analytics/zones.

        Returns all configured analytic zones for this camera

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
        _url_path = '/devices/{serial}/camera/analytics/zones'
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

    def get_device_camera_analytics_recent(self,
                                           serial):
        """Does a GET request to /devices/{serial}/camera/analytics/recent.

        Returns most recent record for analytics zones

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
        _url_path = '/devices/{serial}/camera/analytics/recent'
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

    def get_device_camera_analytics_live(self,
                                         serial):
        """Does a GET request to /devices/{serial}/camera/analytics/live.

        Returns live state from camera of analytics zones

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
        _url_path = '/devices/{serial}/camera/analytics/live'
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

    def get_device_camera_analytics_overview(self,
                                             options=dict()):
        """Does a GET request to /devices/{serial}/camera/analytics/overview.

        Returns an overview of aggregate analytics data for a timespan

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    serial -- string -- TODO: type description here. Example:
                                            t_0 -- string -- The beginning of the timespan for the
                        data. The maximum lookback period is 365 days from
                        today.
                    t_1 -- string -- The end of the timespan for the data. t1
                        can be a maximum of 7 days after t0.
                    timespan -- int -- The timespan for which the information
                        will be fetched. If specifying timespan, do not
                        specify parameters t0 and t1. The value must be in
                        seconds and be less than or equal to 7 days. The
                        default is 1 hour.

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
        _url_path = '/devices/{serial}/camera/analytics/overview'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'serial': options.get('serial', None)
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            't0': options.get('t0', None),
            't1': options.get('t1', None),
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

    def get_device_camera_analytics_zone_history(self,
                                                 options=dict()):
        """Does a GET request to /devices/{serial}/camera/analytics/zones/{zoneId}/history.

        Return historical records for analytic zones

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    serial -- string -- TODO: type description here. Example:
                                            zone_id -- string -- TODO: type description here. Example:
                                            t_0 -- string -- The beginning of the timespan for the
                        data. The maximum lookback period is 365 days from
                        today.
                    t_1 -- string -- The end of the timespan for the data. t1
                        can be a maximum of 14 hours after t0.
                    timespan -- int -- The timespan for which the information
                        will be fetched. If specifying timespan, do not
                        specify parameters t0 and t1. The value must be in
                        seconds and be less than or equal to 14 hours. The
                        default is 1 hour.
                    resolution -- int -- The time resolution in seconds for
                        returned data. The valid resolutions are: 60. The
                        default is 60.

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
                                 zone_id=options.get("zone_id"))

        # Prepare query URL
        _url_path = '/devices/{serial}/camera/analytics/zones/{zoneId}/history'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'serial': options.get('serial', None),
            'zoneId': options.get('zone_id', None)
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
