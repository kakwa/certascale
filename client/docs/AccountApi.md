# swagger_client.AccountApi

All URIs are relative to *http://localhost/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_create**](AccountApi.md#account_create) | **POST** /account | 
[**account_delete**](AccountApi.md#account_delete) | **DELETE** /account/{accountId} | 
[**account_get**](AccountApi.md#account_get) | **GET** /account/{accountId} | 
[**account_list**](AccountApi.md#account_list) | **GET** /account | 
[**account_update**](AccountApi.md#account_update) | **PUT** /account/{accountId} | 
[**apikey_create**](AccountApi.md#apikey_create) | **POST** /account/{accountId}/apikey/ | 
[**apikey_delete**](AccountApi.md#apikey_delete) | **DELETE** /account/{accountId}/apikey/{keyId} | 
[**apikey_get**](AccountApi.md#apikey_get) | **GET** /account/{accountId}/apikey/{keyId} | 
[**apikey_list**](AccountApi.md#apikey_list) | **GET** /account/{accountId}/apikey/ | 


# **account_create**
> AccountDefinition account_create(body)



Create a new account

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountCreateUpdate() # AccountCreateUpdate | Data structure to create the account

try:
    api_response = api_instance.account_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCreateUpdate**](AccountCreateUpdate.md)| Data structure to create the account | 

### Return type

[**AccountDefinition**](AccountDefinition.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_delete**
> DefaultMessage account_delete(account_id)



Remove the account

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 

try:
    api_response = api_instance.account_delete(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**DefaultMessage**](DefaultMessage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get**
> AccountDefinition account_get(account_id)



Get the details of a specific account

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 

try:
    api_response = api_instance.account_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**AccountDefinition**](AccountDefinition.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_list**
> AccountDefinitionList account_list(next_id=next_id)



Get the list of accounts (paginated)

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
next_id = 56 # int |  (optional)

try:
    api_response = api_instance.account_list(next_id=next_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_id** | **int**|  | [optional] 

### Return type

[**AccountDefinitionList**](AccountDefinitionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_update**
> DefaultMessage account_update(account_id, body)



Update an existing account

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 
body = swagger_client.AccountCreateUpdate() # AccountCreateUpdate | 

try:
    api_response = api_instance.account_update(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **body** | [**AccountCreateUpdate**](AccountCreateUpdate.md)|  | 

### Return type

[**DefaultMessage**](DefaultMessage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apikey_create**
> ApiKey apikey_create(account_id)



Create a new API key

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 

try:
    api_response = api_instance.apikey_create(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->apikey_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apikey_delete**
> DefaultMessage apikey_delete(account_id, key_id)



Delete a given key

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    api_response = api_instance.apikey_delete(account_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->apikey_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**DefaultMessage**](DefaultMessage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apikey_get**
> ApiKey apikey_get(account_id, key_id)



Get a given API key

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    api_response = api_instance.apikey_get(account_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->apikey_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apikey_list**
> ApiKeyList apikey_list(account_id, next_id=next_id)



Get the list of API keys for a given account

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 
next_id = 56 # int |  (optional)

try:
    api_response = api_instance.apikey_list(account_id, next_id=next_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->apikey_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **next_id** | **int**|  | [optional] 

### Return type

[**ApiKeyList**](ApiKeyList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

