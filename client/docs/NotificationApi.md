# swagger_client.NotificationApi

All URIs are relative to *http://localhost/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_acknowledge**](NotificationApi.md#notification_acknowledge) | **PUT** /notification/{notificationId} | 
[**notification_get**](NotificationApi.md#notification_get) | **GET** /notification/{notificationId} | 
[**notification_list**](NotificationApi.md#notification_list) | **GET** /notification | 


# **notification_acknowledge**
> DefaultMessage notification_acknowledge(notification_id, body)



Acknowledge the notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
notification_id = 'notification_id_example' # str | 
body = swagger_client.NotificationUpdate() # NotificationUpdate | 

try:
    api_response = api_instance.notification_acknowledge(notification_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_acknowledge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 
 **body** | [**NotificationUpdate**](NotificationUpdate.md)|  | 

### Return type

[**DefaultMessage**](DefaultMessage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_get**
> Notification notification_get(notification_id)



Get specific content for a notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
notification_id = 'notification_id_example' # str | 

try:
    api_response = api_instance.notification_get(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 

### Return type

[**Notification**](Notification.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_list**
> NotificationList notification_list(next_id=next_id)



Get all your certificate update notifications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['bearer'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NotificationApi(swagger_client.ApiClient(configuration))
next_id = 56 # int |  (optional)

try:
    api_response = api_instance.notification_list(next_id=next_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_id** | **int**|  | [optional] 

### Return type

[**NotificationList**](NotificationList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

