# coding: utf-8

"""
    certascale API

    Certascale API documentation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AccountApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def account_create(self, body, **kwargs):  # noqa: E501
        """account_create  # noqa: E501

        Create a new account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.account_create(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param AccountCreateUpdate body: Data structure to create the account (required)
        :return: AccountDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.account_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.account_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def account_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """account_create  # noqa: E501

        Create a new account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.account_create_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param AccountCreateUpdate body: Data structure to create the account (required)
        :return: AccountDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `account_create`")  # noqa: E501

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
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_delete(self, account_id, **kwargs):  # noqa: E501
        """account_delete  # noqa: E501

        Remove the account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.account_delete(account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :return: DefaultMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.account_delete_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.account_delete_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def account_delete_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """account_delete  # noqa: E501

        Remove the account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.account_delete_with_http_info(account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :return: DefaultMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `account_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account/{accountId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DefaultMessage',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_get(self, account_id, **kwargs):  # noqa: E501
        """account_get  # noqa: E501

        Get the details of a specific account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.account_get(account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :return: AccountDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.account_get_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.account_get_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def account_get_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """account_get  # noqa: E501

        Get the details of a specific account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.account_get_with_http_info(account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :return: AccountDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `account_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account/{accountId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_list(self, **kwargs):  # noqa: E501
        """account_list  # noqa: E501

        Get the list of accounts (paginated)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.account_list(async=True)
        >>> result = thread.get()

        :param async bool
        :param int next_id:
        :return: AccountDefinitionList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.account_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.account_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def account_list_with_http_info(self, **kwargs):  # noqa: E501
        """account_list  # noqa: E501

        Get the list of accounts (paginated)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.account_list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int next_id:
        :return: AccountDefinitionList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['next_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'next_id' in params:
            query_params.append(('next_id', params['next_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountDefinitionList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_update(self, account_id, body, **kwargs):  # noqa: E501
        """account_update  # noqa: E501

        Update an existing account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.account_update(account_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :param AccountCreateUpdate body: (required)
        :return: DefaultMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.account_update_with_http_info(account_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.account_update_with_http_info(account_id, body, **kwargs)  # noqa: E501
            return data

    def account_update_with_http_info(self, account_id, body, **kwargs):  # noqa: E501
        """account_update  # noqa: E501

        Update an existing account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.account_update_with_http_info(account_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :param AccountCreateUpdate body: (required)
        :return: DefaultMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `account_update`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `account_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

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
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account/{accountId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DefaultMessage',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apikey_create(self, account_id, **kwargs):  # noqa: E501
        """apikey_create  # noqa: E501

        Create a new API key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.apikey_create(account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :return: ApiKey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.apikey_create_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.apikey_create_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def apikey_create_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """apikey_create  # noqa: E501

        Create a new API key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.apikey_create_with_http_info(account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :return: ApiKey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apikey_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `apikey_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account/{accountId}/apikey/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKey',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apikey_delete(self, account_id, key_id, **kwargs):  # noqa: E501
        """apikey_delete  # noqa: E501

        Delete a given key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.apikey_delete(account_id, key_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :param str key_id: (required)
        :return: DefaultMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.apikey_delete_with_http_info(account_id, key_id, **kwargs)  # noqa: E501
        else:
            (data) = self.apikey_delete_with_http_info(account_id, key_id, **kwargs)  # noqa: E501
            return data

    def apikey_delete_with_http_info(self, account_id, key_id, **kwargs):  # noqa: E501
        """apikey_delete  # noqa: E501

        Delete a given key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.apikey_delete_with_http_info(account_id, key_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :param str key_id: (required)
        :return: DefaultMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'key_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apikey_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `apikey_delete`")  # noqa: E501
        # verify the required parameter 'key_id' is set
        if ('key_id' not in params or
                params['key_id'] is None):
            raise ValueError("Missing the required parameter `key_id` when calling `apikey_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501
        if 'key_id' in params:
            path_params['keyId'] = params['key_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account/{accountId}/apikey/{keyId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DefaultMessage',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apikey_get(self, account_id, key_id, **kwargs):  # noqa: E501
        """apikey_get  # noqa: E501

        Get a given API key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.apikey_get(account_id, key_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :param str key_id: (required)
        :return: ApiKey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.apikey_get_with_http_info(account_id, key_id, **kwargs)  # noqa: E501
        else:
            (data) = self.apikey_get_with_http_info(account_id, key_id, **kwargs)  # noqa: E501
            return data

    def apikey_get_with_http_info(self, account_id, key_id, **kwargs):  # noqa: E501
        """apikey_get  # noqa: E501

        Get a given API key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.apikey_get_with_http_info(account_id, key_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :param str key_id: (required)
        :return: ApiKey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'key_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apikey_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `apikey_get`")  # noqa: E501
        # verify the required parameter 'key_id' is set
        if ('key_id' not in params or
                params['key_id'] is None):
            raise ValueError("Missing the required parameter `key_id` when calling `apikey_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501
        if 'key_id' in params:
            path_params['keyId'] = params['key_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account/{accountId}/apikey/{keyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKey',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apikey_list(self, account_id, **kwargs):  # noqa: E501
        """apikey_list  # noqa: E501

        Get the list of API keys for a given account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.apikey_list(account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :param int next_id:
        :return: ApiKeyList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.apikey_list_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.apikey_list_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def apikey_list_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """apikey_list  # noqa: E501

        Get the list of API keys for a given account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.apikey_list_with_http_info(account_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str account_id: (required)
        :param int next_id:
        :return: ApiKeyList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'next_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apikey_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `apikey_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []
        if 'next_id' in params:
            query_params.append(('next_id', params['next_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account/{accountId}/apikey/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiKeyList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
