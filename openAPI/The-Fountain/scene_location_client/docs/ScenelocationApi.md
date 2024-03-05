# swagger_client.ScenelocationApi

All URIs are relative to *https://api-scenelocation.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scenelocation**](ScenelocationApi.md#delete_scenelocation) | **DELETE** /scenelocation | 
[**get_scenelocation**](ScenelocationApi.md#get_scenelocation) | **GET** /scenelocation | 
[**post_scenelocation**](ScenelocationApi.md#post_scenelocation) | **POST** /scenelocation | 
[**update_scenelocation**](ScenelocationApi.md#update_scenelocation) | **PATCH** /scenelocation | 

# **delete_scenelocation**
> delete_scenelocation(location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScenelocationApi()
location_id = 'location_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
historical_cultural_significance = 'historical_cultural_significance_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_scenelocation(location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance, prefer=prefer)
except ApiException as e:
    print("Exception when calling ScenelocationApi->delete_scenelocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **historical_cultural_significance** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenelocation**
> list[Scenelocation] get_scenelocation(location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScenelocationApi()
location_id = 'location_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
historical_cultural_significance = 'historical_cultural_significance_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_scenelocation(location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenelocationApi->get_scenelocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **historical_cultural_significance** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Scenelocation]**](Scenelocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_scenelocation**
> post_scenelocation(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScenelocationApi()
body = swagger_client.Scenelocation() # Scenelocation | scenelocation (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_scenelocation(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling ScenelocationApi->post_scenelocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scenelocation**](Scenelocation.md)| scenelocation | [optional] 
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

# **update_scenelocation**
> update_scenelocation(body=body, prefer=prefer, location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScenelocationApi()
body = swagger_client.Scenelocation() # Scenelocation | scenelocation (optional)
prefer = 'prefer_example' # str | Preference (optional)
location_id = 'location_id_example' # str |  (optional)
description = 'description_example' # str |  (optional)
historical_cultural_significance = 'historical_cultural_significance_example' # str |  (optional)

try:
    api_instance.update_scenelocation(body=body, prefer=prefer, location_id=location_id, description=description, historical_cultural_significance=historical_cultural_significance)
except ApiException as e:
    print("Exception when calling ScenelocationApi->update_scenelocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scenelocation**](Scenelocation.md)| scenelocation | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **location_id** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **historical_cultural_significance** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

