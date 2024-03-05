# swagger_client.CastingApi

All URIs are relative to *https://api-casting.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_casting**](CastingApi.md#delete_casting) | **DELETE** /casting | 
[**get_casting**](CastingApi.md#get_casting) | **GET** /casting | 
[**post_casting**](CastingApi.md#post_casting) | **POST** /casting | 
[**update_casting**](CastingApi.md#update_casting) | **PATCH** /casting | 

# **delete_casting**
> delete_casting(casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CastingApi()
casting_id = 'casting_id_example' # str |  (optional)
character_id = 'character_id_example' # str |  (optional)
actor_characteristics_choices = 'actor_characteristics_choices_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_casting(casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices, prefer=prefer)
except ApiException as e:
    print("Exception when calling CastingApi->delete_casting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **casting_id** | **str**|  | [optional] 
 **character_id** | **str**|  | [optional] 
 **actor_characteristics_choices** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_casting**
> list[Casting] get_casting(casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CastingApi()
casting_id = 'casting_id_example' # str |  (optional)
character_id = 'character_id_example' # str |  (optional)
actor_characteristics_choices = 'actor_characteristics_choices_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_casting(casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CastingApi->get_casting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **casting_id** | **str**|  | [optional] 
 **character_id** | **str**|  | [optional] 
 **actor_characteristics_choices** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Casting]**](Casting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_casting**
> post_casting(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CastingApi()
body = swagger_client.Casting() # Casting | casting (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_casting(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling CastingApi->post_casting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Casting**](Casting.md)| casting | [optional] 
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

# **update_casting**
> update_casting(body=body, prefer=prefer, casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CastingApi()
body = swagger_client.Casting() # Casting | casting (optional)
prefer = 'prefer_example' # str | Preference (optional)
casting_id = 'casting_id_example' # str |  (optional)
character_id = 'character_id_example' # str |  (optional)
actor_characteristics_choices = 'actor_characteristics_choices_example' # str |  (optional)

try:
    api_instance.update_casting(body=body, prefer=prefer, casting_id=casting_id, character_id=character_id, actor_characteristics_choices=actor_characteristics_choices)
except ApiException as e:
    print("Exception when calling CastingApi->update_casting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Casting**](Casting.md)| casting | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **casting_id** | **str**|  | [optional] 
 **character_id** | **str**|  | [optional] 
 **actor_characteristics_choices** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

