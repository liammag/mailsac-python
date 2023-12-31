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


class AddressesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def check_availability(self, email, **kwargs):  # noqa: E501
        """Check address ownership  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_availability(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailString email: Email address (required)
        :return: EmailAddressAvailability
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_availability_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.check_availability_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def check_availability_with_http_info(self, email, **kwargs):  # noqa: E501
        """Check address ownership  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_availability_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailString email: Email address (required)
        :return: EmailAddressAvailability
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_availability" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `check_availability`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{email}/availability', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailAddressAvailability',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_address(self, email, **kwargs):  # noqa: E501
        """Reserve (create/own) a private email address  # noqa: E501

        Sets the email address private and \"owned\" by the account. All messages which already exist, and any future messages which are received, will be private to this account only.  An email address must be reserved to be able to forward messages to another email address, Slack, web sockets, or webhooks. Public email addresses, and private email addresses under a custom domain, are not routeable.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_address(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailString email: Email address (required)
        :param UpdatePrivateAddressForwarding body:
        :return: EmailAddress
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_address_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.create_address_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def create_address_with_http_info(self, email, **kwargs):  # noqa: E501
        """Reserve (create/own) a private email address  # noqa: E501

        Sets the email address private and \"owned\" by the account. All messages which already exist, and any future messages which are received, will be private to this account only.  An email address must be reserved to be able to forward messages to another email address, Slack, web sockets, or webhooks. Public email addresses, and private email addresses under a custom domain, are not routeable.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_address_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailString email: Email address (required)
        :param UpdatePrivateAddressForwarding body:
        :return: EmailAddress
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `create_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{email}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailAddress',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_addresses(self, body, **kwargs):  # noqa: E501
        """Reserve multiple private addresses  # noqa: E501

        Reserves multiple private addresses. The max addresses per request is 100.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_addresses(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PrivateaddressesbulkBody body: (required)
        :return: EmailAddressList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_addresses_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_addresses_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_addresses_with_http_info(self, body, **kwargs):  # noqa: E501
        """Reserve multiple private addresses  # noqa: E501

        Reserves multiple private addresses. The max addresses per request is 100.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_addresses_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PrivateaddressesbulkBody body: (required)
        :return: EmailAddressList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_addresses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_addresses`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/private-addresses-bulk', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailAddressList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_address(self, email, **kwargs):  # noqa: E501
        """Release a private email address  # noqa: E501

        Removes this private address from ownership by the account. Any email received to the address's inbox will be public in the future, unless the address was under a custom domain which is set private.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_address(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailString email: Email address (required)
        :param bool delete_address_messages:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_address_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_address_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def delete_address_with_http_info(self, email, **kwargs):  # noqa: E501
        """Release a private email address  # noqa: E501

        Removes this private address from ownership by the account. Any email received to the address's inbox will be public in the future, unless the address was under a custom domain which is set private.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_address_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailString email: Email address (required)
        :param bool delete_address_messages:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email', 'delete_address_messages']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `delete_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []
        if 'delete_address_messages' in params:
            query_params.append(('deleteAddressMessages', params['delete_address_messages']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{email}', 'DELETE',
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

    def get_address(self, email, **kwargs):  # noqa: E501
        """Fetch an address or check if it is reserved  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailString email: Email address (required)
        :return: EmailAddress
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def get_address_with_http_info(self, email, **kwargs):  # noqa: E501
        """Fetch an address or check if it is reserved  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailString email: Email address (required)
        :return: EmailAddress
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `get_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{email}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailAddress',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_addresses(self, **kwargs):  # noqa: E501
        """List all private email addresses  # noqa: E501

        Get an array of private inbox address objects for the account.  These addresses must be setup (\"reserved\") using `POST /api/addresses/:email`, or [on the Add Email Address page](https://mailsac.com/private-address).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_addresses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: EmailAddressList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_addresses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_addresses_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_addresses_with_http_info(self, **kwargs):  # noqa: E501
        """List all private email addresses  # noqa: E501

        Get an array of private inbox address objects for the account.  These addresses must be setup (\"reserved\") using `POST /api/addresses/:email`, or [on the Add Email Address page](https://mailsac.com/private-address).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_addresses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: EmailAddressList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_addresses" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/addresses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailAddressList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_address(self, email, **kwargs):  # noqa: E501
        """Update private email address forwarding and metadata  # noqa: E501

        For a private email address, set it to forward to another place.  It can be forwarded to another email (with `via mailsac` indicator), to a websocket, to a webhook, or to a Slack channel.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_address(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailString email: Email address (required)
        :param UpdatePrivateAddressForwarding body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_address_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.update_address_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def update_address_with_http_info(self, email, **kwargs):  # noqa: E501
        """Update private email address forwarding and metadata  # noqa: E501

        For a private email address, set it to forward to another place.  It can be forwarded to another email (with `via mailsac` indicator), to a websocket, to a webhook, or to a Slack channel.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_address_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmailString email: Email address (required)
        :param UpdatePrivateAddressForwarding body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `update_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{email}', 'PUT',
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
