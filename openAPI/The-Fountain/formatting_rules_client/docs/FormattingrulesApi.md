# swagger_client.FormattingrulesApi

All URIs are relative to *https://api-formattingrules.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_formattingrules**](FormattingrulesApi.md#delete_formattingrules) | **DELETE** /formattingrules | 
[**get_formattingrules**](FormattingrulesApi.md#get_formattingrules) | **GET** /formattingrules | 
[**post_formattingrules**](FormattingrulesApi.md#post_formattingrules) | **POST** /formattingrules | 
[**update_forattingrules**](FormattingrulesApi.md#update_forattingrules) | **PATCH** /formattingrules | 

# **delete_formattingrules**
> delete_formattingrules(rule_id=rule_id, script_id=script_id, rule_description=rule_description, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FormattingrulesApi()
rule_id = 'rule_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
rule_description = 'rule_description_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_formattingrules(rule_id=rule_id, script_id=script_id, rule_description=rule_description, prefer=prefer)
except ApiException as e:
    print("Exception when calling FormattingrulesApi->delete_formattingrules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **rule_description** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_formattingrules**
> list[Formattingrules] get_formattingrules(rule_id=rule_id, script_id=script_id, rule_description=rule_description, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FormattingrulesApi()
rule_id = 'rule_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
rule_description = 'rule_description_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_formattingrules(rule_id=rule_id, script_id=script_id, rule_description=rule_description, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormattingrulesApi->get_formattingrules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **rule_description** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Formattingrules]**](Formattingrules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_formattingrules**
> post_formattingrules(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FormattingrulesApi()
body = swagger_client.Formattingrules() # Formattingrules | formattingrules (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_formattingrules(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling FormattingrulesApi->post_formattingrules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Formattingrules**](Formattingrules.md)| formattingrules | [optional] 
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

# **update_forattingrules**
> update_forattingrules(body=body, prefer=prefer, rule_id=rule_id, script_id=script_id, rule_description=rule_description)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FormattingrulesApi()
body = swagger_client.Formattingrules() # Formattingrules | formattingrules (optional)
prefer = 'prefer_example' # str | Preference (optional)
rule_id = 'rule_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
rule_description = 'rule_description_example' # str |  (optional)

try:
    api_instance.update_forattingrules(body=body, prefer=prefer, rule_id=rule_id, script_id=script_id, rule_description=rule_description)
except ApiException as e:
    print("Exception when calling FormattingrulesApi->update_forattingrules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Formattingrules**](Formattingrules.md)| formattingrules | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **rule_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **rule_description** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

