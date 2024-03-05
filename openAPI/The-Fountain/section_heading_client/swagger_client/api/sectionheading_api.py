# coding: utf-8

"""
    PostgREST API

    This is a dynamic API generated by PostgREST  # noqa: E501

    OpenAPI spec version: 12.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SectionheadingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_sectionheading(self, **kwargs):  # noqa: E501
        """delete_sectionheading  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sectionheading(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str section_id:
        :param str script_id:
        :param str text:
        :param str prefer: Preference
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_sectionheading_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_sectionheading_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_sectionheading_with_http_info(self, **kwargs):  # noqa: E501
        """delete_sectionheading  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sectionheading_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str section_id:
        :param str script_id:
        :param str text:
        :param str prefer: Preference
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['section_id', 'script_id', 'text', 'prefer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_sectionheading" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'section_id' in params:
            query_params.append(('section_id', params['section_id']))  # noqa: E501
        if 'script_id' in params:
            query_params.append(('script_id', params['script_id']))  # noqa: E501
        if 'text' in params:
            query_params.append(('text', params['text']))  # noqa: E501

        header_params = {}
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sectionheading', 'DELETE',
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

    def get_sectionheading(self, **kwargs):  # noqa: E501
        """get_sectionheading  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sectionheading(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str section_id:
        :param str script_id:
        :param str text:
        :param str select: Filtering Columns
        :param str order: Ordering
        :param str range: Limiting and Pagination
        :param str range_unit: Limiting and Pagination
        :param str offset: Limiting and Pagination
        :param str limit: Limiting and Pagination
        :param str prefer: Preference
        :return: list[Sectionheading]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sectionheading_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sectionheading_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sectionheading_with_http_info(self, **kwargs):  # noqa: E501
        """get_sectionheading  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sectionheading_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str section_id:
        :param str script_id:
        :param str text:
        :param str select: Filtering Columns
        :param str order: Ordering
        :param str range: Limiting and Pagination
        :param str range_unit: Limiting and Pagination
        :param str offset: Limiting and Pagination
        :param str limit: Limiting and Pagination
        :param str prefer: Preference
        :return: list[Sectionheading]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['section_id', 'script_id', 'text', 'select', 'order', 'range', 'range_unit', 'offset', 'limit', 'prefer']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sectionheading" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'section_id' in params:
            query_params.append(('section_id', params['section_id']))  # noqa: E501
        if 'script_id' in params:
            query_params.append(('script_id', params['script_id']))  # noqa: E501
        if 'text' in params:
            query_params.append(('text', params['text']))  # noqa: E501
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'range' in params:
            header_params['Range'] = params['range']  # noqa: E501
        if 'range_unit' in params:
            header_params['Range-Unit'] = params['range_unit']  # noqa: E501
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/vnd.pgrst.object+json;nulls=stripped', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sectionheading', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Sectionheading]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_sectionheading(self, **kwargs):  # noqa: E501
        """post_sectionheading  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_sectionheading(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Sectionheading body: sectionheading
        :param str prefer: Preference
        :param str select: Filtering Columns
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_sectionheading_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_sectionheading_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_sectionheading_with_http_info(self, **kwargs):  # noqa: E501
        """post_sectionheading  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_sectionheading_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Sectionheading body: sectionheading
        :param str prefer: Preference
        :param str select: Filtering Columns
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'prefer', 'select']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_sectionheading" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501

        header_params = {}
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/vnd.pgrst.object+json;nulls=stripped', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sectionheading', 'POST',
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

    def update_sectionheading(self, **kwargs):  # noqa: E501
        """update_sectionheading  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_sectionheading(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Sectionheading body: sectionheading
        :param str prefer: Preference
        :param str section_id:
        :param str script_id:
        :param str text:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_sectionheading_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_sectionheading_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_sectionheading_with_http_info(self, **kwargs):  # noqa: E501
        """update_sectionheading  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_sectionheading_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Sectionheading body: sectionheading
        :param str prefer: Preference
        :param str section_id:
        :param str script_id:
        :param str text:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'prefer', 'section_id', 'script_id', 'text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_sectionheading" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'section_id' in params:
            query_params.append(('section_id', params['section_id']))  # noqa: E501
        if 'script_id' in params:
            query_params.append(('script_id', params['script_id']))  # noqa: E501
        if 'text' in params:
            query_params.append(('text', params['text']))  # noqa: E501

        header_params = {}
        if 'prefer' in params:
            header_params['Prefer'] = params['prefer']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/vnd.pgrst.object+json;nulls=stripped', 'application/vnd.pgrst.object+json', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sectionheading', 'PATCH',
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
