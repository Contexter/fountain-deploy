# swagger_client.CharacterrelationshipApi

All URIs are relative to *https://api-characterrelationship.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_charcterrelationship**](CharacterrelationshipApi.md#delete_charcterrelationship) | **DELETE** /characterrelationship | 
[**get_characterrelationship**](CharacterrelationshipApi.md#get_characterrelationship) | **GET** /characterrelationship | 
[**post_characterrelationship**](CharacterrelationshipApi.md#post_characterrelationship) | **POST** /characterrelationship | 
[**update_characterrelationship**](CharacterrelationshipApi.md#update_characterrelationship) | **PATCH** /characterrelationship | 

# **delete_charcterrelationship**
> delete_charcterrelationship(relationship_id=relationship_id, character1_id=character1_id, character2_id=character2_id, relationship_type=relationship_type, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CharacterrelationshipApi()
relationship_id = 'relationship_id_example' # str |  (optional)
character1_id = 'character1_id_example' # str |  (optional)
character2_id = 'character2_id_example' # str |  (optional)
relationship_type = 'relationship_type_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_charcterrelationship(relationship_id=relationship_id, character1_id=character1_id, character2_id=character2_id, relationship_type=relationship_type, prefer=prefer)
except ApiException as e:
    print("Exception when calling CharacterrelationshipApi->delete_charcterrelationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relationship_id** | **str**|  | [optional] 
 **character1_id** | **str**|  | [optional] 
 **character2_id** | **str**|  | [optional] 
 **relationship_type** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characterrelationship**
> list[Characterrelationship] get_characterrelationship(relationship_id=relationship_id, character1_id=character1_id, character2_id=character2_id, relationship_type=relationship_type, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CharacterrelationshipApi()
relationship_id = 'relationship_id_example' # str |  (optional)
character1_id = 'character1_id_example' # str |  (optional)
character2_id = 'character2_id_example' # str |  (optional)
relationship_type = 'relationship_type_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_characterrelationship(relationship_id=relationship_id, character1_id=character1_id, character2_id=character2_id, relationship_type=relationship_type, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CharacterrelationshipApi->get_characterrelationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relationship_id** | **str**|  | [optional] 
 **character1_id** | **str**|  | [optional] 
 **character2_id** | **str**|  | [optional] 
 **relationship_type** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Characterrelationship]**](Characterrelationship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_characterrelationship**
> post_characterrelationship(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CharacterrelationshipApi()
body = swagger_client.Characterrelationship() # Characterrelationship | characterrelationship (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_characterrelationship(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling CharacterrelationshipApi->post_characterrelationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Characterrelationship**](Characterrelationship.md)| characterrelationship | [optional] 
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

# **update_characterrelationship**
> update_characterrelationship(body=body, prefer=prefer, relationship_id=relationship_id, character1_id=character1_id, character2_id=character2_id, relationship_type=relationship_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CharacterrelationshipApi()
body = swagger_client.Characterrelationship() # Characterrelationship | characterrelationship (optional)
prefer = 'prefer_example' # str | Preference (optional)
relationship_id = 'relationship_id_example' # str |  (optional)
character1_id = 'character1_id_example' # str |  (optional)
character2_id = 'character2_id_example' # str |  (optional)
relationship_type = 'relationship_type_example' # str |  (optional)

try:
    api_instance.update_characterrelationship(body=body, prefer=prefer, relationship_id=relationship_id, character1_id=character1_id, character2_id=character2_id, relationship_type=relationship_type)
except ApiException as e:
    print("Exception when calling CharacterrelationshipApi->update_characterrelationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Characterrelationship**](Characterrelationship.md)| characterrelationship | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **relationship_id** | **str**|  | [optional] 
 **character1_id** | **str**|  | [optional] 
 **character2_id** | **str**|  | [optional] 
 **relationship_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

