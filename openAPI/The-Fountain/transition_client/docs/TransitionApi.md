# swagger_client.TransitionApi

All URIs are relative to *https://api-transition.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_transition**](TransitionApi.md#delete_transition) | **DELETE** /transition | 
[**get_transition**](TransitionApi.md#get_transition) | **GET** /transition | 
[**post_transition**](TransitionApi.md#post_transition) | **POST** /transition | 
[**update_transition**](TransitionApi.md#update_transition) | **PATCH** /transition | 

# **delete_transition**
> delete_transition(transition_id=transition_id, scene_id=scene_id, transition_text=transition_text, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransitionApi()
transition_id = 'transition_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
transition_text = 'transition_text_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_transition(transition_id=transition_id, scene_id=scene_id, transition_text=transition_text, prefer=prefer)
except ApiException as e:
    print("Exception when calling TransitionApi->delete_transition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transition_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **transition_text** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transition**
> list[Transition] get_transition(transition_id=transition_id, scene_id=scene_id, transition_text=transition_text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransitionApi()
transition_id = 'transition_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
transition_text = 'transition_text_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_transition(transition_id=transition_id, scene_id=scene_id, transition_text=transition_text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransitionApi->get_transition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transition_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **transition_text** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Transition]**](Transition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_transition**
> post_transition(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransitionApi()
body = swagger_client.Transition() # Transition | transition (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_transition(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling TransitionApi->post_transition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Transition**](Transition.md)| transition | [optional] 
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

# **update_transition**
> update_transition(body=body, prefer=prefer, transition_id=transition_id, scene_id=scene_id, transition_text=transition_text)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransitionApi()
body = swagger_client.Transition() # Transition | transition (optional)
prefer = 'prefer_example' # str | Preference (optional)
transition_id = 'transition_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
transition_text = 'transition_text_example' # str |  (optional)

try:
    api_instance.update_transition(body=body, prefer=prefer, transition_id=transition_id, scene_id=scene_id, transition_text=transition_text)
except ApiException as e:
    print("Exception when calling TransitionApi->update_transition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Transition**](Transition.md)| transition | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **transition_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **transition_text** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

