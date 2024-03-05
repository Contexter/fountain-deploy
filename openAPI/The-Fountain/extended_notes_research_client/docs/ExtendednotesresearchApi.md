# swagger_client.ExtendednotesresearchApi

All URIs are relative to *https://api-extendednotesresearch.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_extendednotesresearch**](ExtendednotesresearchApi.md#delete_extendednotesresearch) | **DELETE** /extendednotesresearch | 
[**get_extentednotesresearch**](ExtendednotesresearchApi.md#get_extentednotesresearch) | **GET** /extendednotesresearch | 
[**post_extendednotesresearch**](ExtendednotesresearchApi.md#post_extendednotesresearch) | **POST** /extendednotesresearch | 
[**update_extedednotesresearch**](ExtendednotesresearchApi.md#update_extedednotesresearch) | **PATCH** /extendednotesresearch | 

# **delete_extendednotesresearch**
> delete_extendednotesresearch(research_id=research_id, script_id=script_id, notes=notes, research_details=research_details, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtendednotesresearchApi()
research_id = 'research_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
research_details = 'research_details_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_extendednotesresearch(research_id=research_id, script_id=script_id, notes=notes, research_details=research_details, prefer=prefer)
except ApiException as e:
    print("Exception when calling ExtendednotesresearchApi->delete_extendednotesresearch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **research_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **research_details** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extentednotesresearch**
> list[Extendednotesresearch] get_extentednotesresearch(research_id=research_id, script_id=script_id, notes=notes, research_details=research_details, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtendednotesresearchApi()
research_id = 'research_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
research_details = 'research_details_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_extentednotesresearch(research_id=research_id, script_id=script_id, notes=notes, research_details=research_details, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtendednotesresearchApi->get_extentednotesresearch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **research_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **research_details** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Extendednotesresearch]**](Extendednotesresearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_extendednotesresearch**
> post_extendednotesresearch(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtendednotesresearchApi()
body = swagger_client.Extendednotesresearch() # Extendednotesresearch | extendednotesresearch (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_extendednotesresearch(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling ExtendednotesresearchApi->post_extendednotesresearch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Extendednotesresearch**](Extendednotesresearch.md)| extendednotesresearch | [optional] 
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

# **update_extedednotesresearch**
> update_extedednotesresearch(body=body, prefer=prefer, research_id=research_id, script_id=script_id, notes=notes, research_details=research_details)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtendednotesresearchApi()
body = swagger_client.Extendednotesresearch() # Extendednotesresearch | extendednotesresearch (optional)
prefer = 'prefer_example' # str | Preference (optional)
research_id = 'research_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
research_details = 'research_details_example' # str |  (optional)

try:
    api_instance.update_extedednotesresearch(body=body, prefer=prefer, research_id=research_id, script_id=script_id, notes=notes, research_details=research_details)
except ApiException as e:
    print("Exception when calling ExtendednotesresearchApi->update_extedednotesresearch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Extendednotesresearch**](Extendednotesresearch.md)| extendednotesresearch | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **research_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **research_details** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

