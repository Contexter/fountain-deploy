# swagger_client.TitlepageApi

All URIs are relative to *https://api-titlepage.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_titlepage**](TitlepageApi.md#delete_titlepage) | **DELETE** /titlepage | 
[**get_titlepage**](TitlepageApi.md#get_titlepage) | **GET** /titlepage | 
[**post_titlepage**](TitlepageApi.md#post_titlepage) | **POST** /titlepage | 
[**update_titlepage**](TitlepageApi.md#update_titlepage) | **PATCH** /titlepage | 

# **delete_titlepage**
> delete_titlepage(title_page_id=title_page_id, script_id=script_id, text=text, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TitlepageApi()
title_page_id = 'title_page_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
text = 'text_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_titlepage(title_page_id=title_page_id, script_id=script_id, text=text, prefer=prefer)
except ApiException as e:
    print("Exception when calling TitlepageApi->delete_titlepage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_page_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_titlepage**
> list[Titlepage] get_titlepage(title_page_id=title_page_id, script_id=script_id, text=text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TitlepageApi()
title_page_id = 'title_page_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
text = 'text_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_titlepage(title_page_id=title_page_id, script_id=script_id, text=text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TitlepageApi->get_titlepage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title_page_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Titlepage]**](Titlepage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_titlepage**
> post_titlepage(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TitlepageApi()
body = swagger_client.Titlepage() # Titlepage | titlepage (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_titlepage(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling TitlepageApi->post_titlepage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Titlepage**](Titlepage.md)| titlepage | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **select** | **str**| Filtering Columns | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_titlepage**
> update_titlepage(body=body, prefer=prefer, title_page_id=title_page_id, script_id=script_id, text=text)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TitlepageApi()
body = swagger_client.Titlepage() # Titlepage | titlepage (optional)
prefer = 'prefer_example' # str | Preference (optional)
title_page_id = 'title_page_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
text = 'text_example' # str |  (optional)

try:
    api_instance.update_titlepage(body=body, prefer=prefer, title_page_id=title_page_id, script_id=script_id, text=text)
except ApiException as e:
    print("Exception when calling TitlepageApi->update_titlepage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Titlepage**](Titlepage.md)| titlepage | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **title_page_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

