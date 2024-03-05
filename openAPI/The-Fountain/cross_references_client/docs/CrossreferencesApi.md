# swagger_client.CrossreferencesApi

All URIs are relative to *https://api-crossreferences.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_crossreferences**](CrossreferencesApi.md#delete_crossreferences) | **DELETE** /crossreferences | 
[**get_crossreferences**](CrossreferencesApi.md#get_crossreferences) | **GET** /crossreferences | 
[**post_crossreferences**](CrossreferencesApi.md#post_crossreferences) | **POST** /crossreferences | 
[**update_crossreferences**](CrossreferencesApi.md#update_crossreferences) | **PATCH** /crossreferences | 

# **delete_crossreferences**
> delete_crossreferences(cross_reference_id=cross_reference_id, scene_id=scene_id, referenced_scene_id=referenced_scene_id, description=description, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CrossreferencesApi()
cross_reference_id = 'cross_reference_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
referenced_scene_id = 'referenced_scene_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_crossreferences(cross_reference_id=cross_reference_id, scene_id=scene_id, referenced_scene_id=referenced_scene_id, description=description, prefer=prefer)
except ApiException as e:
    print("Exception when calling CrossreferencesApi->delete_crossreferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_reference_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **referenced_scene_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crossreferences**
> list[Crossreferences] get_crossreferences(cross_reference_id=cross_reference_id, scene_id=scene_id, referenced_scene_id=referenced_scene_id, description=description, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CrossreferencesApi()
cross_reference_id = 'cross_reference_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
referenced_scene_id = 'referenced_scene_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_crossreferences(cross_reference_id=cross_reference_id, scene_id=scene_id, referenced_scene_id=referenced_scene_id, description=description, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrossreferencesApi->get_crossreferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_reference_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **referenced_scene_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Crossreferences]**](Crossreferences.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_crossreferences**
> post_crossreferences(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CrossreferencesApi()
body = swagger_client.Crossreferences() # Crossreferences | crossreferences (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_crossreferences(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling CrossreferencesApi->post_crossreferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Crossreferences**](Crossreferences.md)| crossreferences | [optional] 
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

# **update_crossreferences**
> update_crossreferences(body=body, prefer=prefer, cross_reference_id=cross_reference_id, scene_id=scene_id, referenced_scene_id=referenced_scene_id, description=description)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CrossreferencesApi()
body = swagger_client.Crossreferences() # Crossreferences | crossreferences (optional)
prefer = 'prefer_example' # str | Preference (optional)
cross_reference_id = 'cross_reference_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
referenced_scene_id = 'referenced_scene_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)

try:
    api_instance.update_crossreferences(body=body, prefer=prefer, cross_reference_id=cross_reference_id, scene_id=scene_id, referenced_scene_id=referenced_scene_id, description=description)
except ApiException as e:
    print("Exception when calling CrossreferencesApi->update_crossreferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Crossreferences**](Crossreferences.md)| crossreferences | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **cross_reference_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **referenced_scene_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

