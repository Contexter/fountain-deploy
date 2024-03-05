# swagger_client.PagebreakApi

All URIs are relative to *https://api-pagebreak.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pagebreak**](PagebreakApi.md#delete_pagebreak) | **DELETE** /pagebreak | 
[**get_pagebreak**](PagebreakApi.md#get_pagebreak) | **GET** /pagebreak | 
[**post_pagebreak**](PagebreakApi.md#post_pagebreak) | **POST** /pagebreak | 
[**update_pagebreak**](PagebreakApi.md#update_pagebreak) | **PATCH** /pagebreak | 

# **delete_pagebreak**
> delete_pagebreak(page_break_id=page_break_id, script_id=script_id, page_number=page_number, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PagebreakApi()
page_break_id = 'page_break_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
page_number = 'page_number_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_pagebreak(page_break_id=page_break_id, script_id=script_id, page_number=page_number, prefer=prefer)
except ApiException as e:
    print("Exception when calling PagebreakApi->delete_pagebreak: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_break_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **page_number** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pagebreak**
> list[Pagebreak] get_pagebreak(page_break_id=page_break_id, script_id=script_id, page_number=page_number, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PagebreakApi()
page_break_id = 'page_break_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
page_number = 'page_number_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_pagebreak(page_break_id=page_break_id, script_id=script_id, page_number=page_number, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PagebreakApi->get_pagebreak: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_break_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **page_number** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Pagebreak]**](Pagebreak.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pagebreak**
> post_pagebreak(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PagebreakApi()
body = swagger_client.Pagebreak() # Pagebreak | pagebreak (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_pagebreak(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling PagebreakApi->post_pagebreak: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pagebreak**](Pagebreak.md)| pagebreak | [optional] 
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

# **update_pagebreak**
> update_pagebreak(body=body, prefer=prefer, page_break_id=page_break_id, script_id=script_id, page_number=page_number)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PagebreakApi()
body = swagger_client.Pagebreak() # Pagebreak | pagebreak (optional)
prefer = 'prefer_example' # str | Preference (optional)
page_break_id = 'page_break_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
page_number = 'page_number_example' # str |  (optional)

try:
    api_instance.update_pagebreak(body=body, prefer=prefer, page_break_id=page_break_id, script_id=script_id, page_number=page_number)
except ApiException as e:
    print("Exception when calling PagebreakApi->update_pagebreak: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pagebreak**](Pagebreak.md)| pagebreak | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **page_break_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **page_number** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

