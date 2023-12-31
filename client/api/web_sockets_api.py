# coding: utf-8

"""
    mailsac API Specification

    ## About the API  The Mailsac API allows for interacting with Mailsac services, including checking email, email validations, setting up forwarding addresses, receiving web socket email messages, and sending outbound mail.  [**Get a free API key**](https://mailsac.com/api-keys)  Test the Mailsac API online:  * [**Swagger UI Explorer** &rarr;](https://mailsac.com/docs/swagger)  **Base API Endpoint**:  * `https://mailsac.com/api/` * _All API documentation is relative to this endpoint._  **OpenAPI Spec**:  * [Download JSON](https://mailsac.com/openapi.json) * [Download YAML](https://mailsac.com/openapi.yml)   ### Support and Resources  * [npm Node.js and Browser library - @mailsac/api](https://www.npmjs.com/package/@mailsac/api) * [Full Documentation and Guides](https://docs.mailsac.com) * [Community Support and Discussion Forums](https://forum.mailsac.com/forums/) * [Web socket example in Node.js - ruffrey](https://github.com/ruffrey/mailsac-node-websocket-example)  Paid Email Support, Pre-Sales    > support@team.mailsac.com  [Terms of Service](https://docs.mailsac.com/en/latest/about/terms_of_service.html)  [Privacy Policy](https://docs.mailsac.com/en/latest/about/privacy_policy.html)   # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from client.api_client import ApiClient


class WebSocketsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def do_not_use_web_socket_docs_only(self, **kwargs):  # noqa: E501
        """Connect a web socket to wss://sock.mailsac.com/incoming-messages  # noqa: E501

        *Note: this does not work in Swagger UI. Visit https://sock.mailsac.com to test.*  You can receive email via web socket for private email addresses and custom domains.  To enable web socket forwarding:  * Addresses: Select *Edit* for the email address you want to forward. Then check the checkbox for web socket forwarding, and save. * Custom Domains: Select *Manage* for the domain and click the *Forwarding* tab. Toggle the *Enable Web Sockets* option.  Note: Web socket forwarding is **not enabled by default.**  ### Web Socket Examples  #### Web Socket Test Page  https://sock.mailsac.com  Receive emails in your web browser.  Experiment with the web socket gateway in realtime.  #### Web Socket Node.js  Listen for Mailsac emails via websocket in this tiny Node.js example app.  https://github.com/ruffrey/mailsac-node-websocket-example  ### Web Socket Connection Endpoint  The web socket endpoint is `wss://sock.mailsac.com/incoming-messages`  Example:  > wss://sock.mailsac.com/incoming-messages?key=k_e9bPnd2adexample&addresses=jeff@mailsac.com,asdf-outbound.mailsac.com  > First frame:  ``` {   \"status\": 200,   \"msg\": \"Listening\",   \"addresses\": [     \"jeff@mailsac.com\"   ],   \"domains\": [     \"asdf-outbound.mailsac.com\"   ] } ```  All web socket messages are JSON. After parsing the JSON, there will be a status field with an HTTP status code (usually 200).  An email coming over the web socket will also have an email property, and its value will be the same as the messages REST API, plus some additional fields.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.do_not_use_web_socket_docs_only(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: Mailsac-Key in the `?key=` querystring
        :param str addresses: Private addresses or domains which are enabled for web socket messages
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.do_not_use_web_socket_docs_only_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.do_not_use_web_socket_docs_only_with_http_info(**kwargs)  # noqa: E501
            return data

    def do_not_use_web_socket_docs_only_with_http_info(self, **kwargs):  # noqa: E501
        """Connect a web socket to wss://sock.mailsac.com/incoming-messages  # noqa: E501

        *Note: this does not work in Swagger UI. Visit https://sock.mailsac.com to test.*  You can receive email via web socket for private email addresses and custom domains.  To enable web socket forwarding:  * Addresses: Select *Edit* for the email address you want to forward. Then check the checkbox for web socket forwarding, and save. * Custom Domains: Select *Manage* for the domain and click the *Forwarding* tab. Toggle the *Enable Web Sockets* option.  Note: Web socket forwarding is **not enabled by default.**  ### Web Socket Examples  #### Web Socket Test Page  https://sock.mailsac.com  Receive emails in your web browser.  Experiment with the web socket gateway in realtime.  #### Web Socket Node.js  Listen for Mailsac emails via websocket in this tiny Node.js example app.  https://github.com/ruffrey/mailsac-node-websocket-example  ### Web Socket Connection Endpoint  The web socket endpoint is `wss://sock.mailsac.com/incoming-messages`  Example:  > wss://sock.mailsac.com/incoming-messages?key=k_e9bPnd2adexample&addresses=jeff@mailsac.com,asdf-outbound.mailsac.com  > First frame:  ``` {   \"status\": 200,   \"msg\": \"Listening\",   \"addresses\": [     \"jeff@mailsac.com\"   ],   \"domains\": [     \"asdf-outbound.mailsac.com\"   ] } ```  All web socket messages are JSON. After parsing the JSON, there will be a status field with an HTTP status code (usually 200).  An email coming over the web socket will also have an email property, and its value will be the same as the messages REST API, plus some additional fields.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.do_not_use_web_socket_docs_only_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: Mailsac-Key in the `?key=` querystring
        :param str addresses: Private addresses or domains which are enabled for web socket messages
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'addresses']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method do_not_use_web_socket_docs_only" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
        if 'addresses' in params:
            query_params.append(('addresses', params['addresses']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/custom_web_sockets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
