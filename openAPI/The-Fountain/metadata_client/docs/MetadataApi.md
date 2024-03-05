# swagger_client.MetadataApi

All URIs are relative to *https://api-metadata.fountain.coach*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_metadata**](MetadataApi.md#delete_metadata) | **DELETE** /metadata | 
[**get_metadata**](MetadataApi.md#get_metadata) | **GET** /metadata | 
[**post_metadata**](MetadataApi.md#post_metadata) | **POST** /metadata | 
[**update_metadata**](MetadataApi.md#update_metadata) | **PATCH** /metadata | 

# **delete_metadata**
> delete_metadata(metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
metadata_id = 'metadata_id_example' # str |  (optional)
creation_date = '2013-10-20' # date |  (optional)
last_modified_date = '2013-10-20' # date |  (optional)
version_number = 'version_number_example' # str |  (optional)
additional_information = 'additional_information_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.delete_metadata(metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information, prefer=prefer)
except ApiException as e:
    print("Exception when calling MetadataApi->delete_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_id** | **str**|  | [optional] 
 **creation_date** | **date**|  | [optional] 
 **last_modified_date** | **date**|  | [optional] 
 **version_number** | **str**|  | [optional] 
 **additional_information** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> list[Metadata] get_metadata(metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
metadata_id = 'metadata_id_example' # str |  (optional)
creation_date = '2013-10-20' # date |  (optional)
last_modified_date = '2013-10-20' # date |  (optional)
version_number = 'version_number_example' # str |  (optional)
additional_information = 'additional_information_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.get_metadata(metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_id** | **str**|  | [optional] 
 **creation_date** | **date**|  | [optional] 
 **last_modified_date** | **date**|  | [optional] 
 **version_number** | **str**|  | [optional] 
 **additional_information** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_metadata**
> post_metadata(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = swagger_client.Metadata() # Metadata | metadata (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.post_metadata(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling MetadataApi->post_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| metadata | [optional] 
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

# **update_metadata**
> update_metadata(body=body, prefer=prefer, metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
body = swagger_client.Metadata() # Metadata | metadata (optional)
prefer = 'prefer_example' # str | Preference (optional)
metadata_id = 'metadata_id_example' # str |  (optional)
creation_date = '2013-10-20' # date |  (optional)
last_modified_date = '2013-10-20' # date |  (optional)
version_number = 'version_number_example' # str |  (optional)
additional_information = 'additional_information_example' # str |  (optional)

try:
    api_instance.update_metadata(body=body, prefer=prefer, metadata_id=metadata_id, creation_date=creation_date, last_modified_date=last_modified_date, version_number=version_number, additional_information=additional_information)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Metadata**](Metadata.md)| metadata | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **metadata_id** | **str**|  | [optional] 
 **creation_date** | **date**|  | [optional] 
 **last_modified_date** | **date**|  | [optional] 
 **version_number** | **str**|  | [optional] 
 **additional_information** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

