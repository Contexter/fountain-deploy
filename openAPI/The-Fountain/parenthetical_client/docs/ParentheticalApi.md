# swagger_client.ParentheticalApi

All URIs are relative to *https://api-parenthetical.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_parenthetical**](ParentheticalApi.md#delete_parenthetical) | **DELETE** /parenthetical | 
[**get_parenthetical**](ParentheticalApi.md#get_parenthetical) | **GET** /parenthetical | 
[**post_parenthetical**](ParentheticalApi.md#post_parenthetical) | **POST** /parenthetical | 
[**update_parenthetical**](ParentheticalApi.md#update_parenthetical) | **PATCH** /parenthetical | 

# **delete_parenthetical**
> delete_parenthetical(parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParentheticalApi()
parenthetical_id = 'parenthetical_id_example' # str |  (optional)
dialogue_id = 'dialogue_id_example' # str |  (optional)
original_text = 'original_text_example' # str |  (optional)
modernized_text = 'modernized_text_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_parenthetical(parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text, prefer=prefer)
except ApiException as e:
    print("Exception when calling ParentheticalApi->delete_parenthetical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parenthetical_id** | **str**|  | [optional] 
 **dialogue_id** | **str**|  | [optional] 
 **original_text** | **str**|  | [optional] 
 **modernized_text** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parenthetical**
> list[Parenthetical] get_parenthetical(parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParentheticalApi()
parenthetical_id = 'parenthetical_id_example' # str |  (optional)
dialogue_id = 'dialogue_id_example' # str |  (optional)
original_text = 'original_text_example' # str |  (optional)
modernized_text = 'modernized_text_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_parenthetical(parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParentheticalApi->get_parenthetical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parenthetical_id** | **str**|  | [optional] 
 **dialogue_id** | **str**|  | [optional] 
 **original_text** | **str**|  | [optional] 
 **modernized_text** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Parenthetical]**](Parenthetical.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_parenthetical**
> post_parenthetical(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParentheticalApi()
body = swagger_client.Parenthetical() # Parenthetical | parenthetical (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_parenthetical(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling ParentheticalApi->post_parenthetical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Parenthetical**](Parenthetical.md)| parenthetical | [optional] 
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

# **update_parenthetical**
> update_parenthetical(body=body, prefer=prefer, parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParentheticalApi()
body = swagger_client.Parenthetical() # Parenthetical | parenthetical (optional)
prefer = 'prefer_example' # str | Preference (optional)
parenthetical_id = 'parenthetical_id_example' # str |  (optional)
dialogue_id = 'dialogue_id_example' # str |  (optional)
original_text = 'original_text_example' # str |  (optional)
modernized_text = 'modernized_text_example' # str |  (optional)

try:
    api_instance.update_parenthetical(body=body, prefer=prefer, parenthetical_id=parenthetical_id, dialogue_id=dialogue_id, original_text=original_text, modernized_text=modernized_text)
except ApiException as e:
    print("Exception when calling ParentheticalApi->update_parenthetical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Parenthetical**](Parenthetical.md)| parenthetical | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **parenthetical_id** | **str**|  | [optional] 
 **dialogue_id** | **str**|  | [optional] 
 **original_text** | **str**|  | [optional] 
 **modernized_text** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

