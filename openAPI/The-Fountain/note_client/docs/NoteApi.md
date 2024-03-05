# swagger_client.NoteApi

All URIs are relative to *https://api-note.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_note**](NoteApi.md#delete_note) | **DELETE** /note | 
[**get_note**](NoteApi.md#get_note) | **GET** /note | 
[**post_note**](NoteApi.md#post_note) | **POST** /note | 
[**update_note**](NoteApi.md#update_note) | **PATCH** /note | 

# **delete_note**
> delete_note(note_id=note_id, script_id=script_id, type=type, text=text, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NoteApi()
note_id = 'note_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
type = 'type_example' # str |  (optional)
text = 'text_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_note(note_id=note_id, script_id=script_id, type=type, text=text, prefer=prefer)
except ApiException as e:
    print("Exception when calling NoteApi->delete_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
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

# **get_note**
> list[Note] get_note(note_id=note_id, script_id=script_id, type=type, text=text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NoteApi()
note_id = 'note_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
type = 'type_example' # str |  (optional)
text = 'text_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_note(note_id=note_id, script_id=script_id, type=type, text=text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteApi->get_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Note]**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_note**
> post_note(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NoteApi()
body = swagger_client.Note() # Note | note (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_note(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling NoteApi->post_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Note**](Note.md)| note | [optional] 
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

# **update_note**
> update_note(body=body, prefer=prefer, note_id=note_id, script_id=script_id, type=type, text=text)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NoteApi()
body = swagger_client.Note() # Note | note (optional)
prefer = 'prefer_example' # str | Preference (optional)
note_id = 'note_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
type = 'type_example' # str |  (optional)
text = 'text_example' # str |  (optional)

try:
    api_instance.update_note(body=body, prefer=prefer, note_id=note_id, script_id=script_id, type=type, text=text)
except ApiException as e:
    print("Exception when calling NoteApi->update_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Note**](Note.md)| note | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **note_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

