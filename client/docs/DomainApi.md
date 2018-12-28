# swagger_client.DomainApi

All URIs are relative to *http://localhost/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificate_create**](DomainApi.md#certificate_create) | **POST** /domain/{domainName}/certificate/ | 
[**certificate_delete**](DomainApi.md#certificate_delete) | **DELETE** /domain/{domainName}/certificate/{certificateId} | 
[**certificate_get**](DomainApi.md#certificate_get) | **GET** /domain/{domainName}/certificate/{certificateId} | 
[**certificate_list**](DomainApi.md#certificate_list) | **GET** /domain/{domainName}/certificate/ | 
[**domain_create**](DomainApi.md#domain_create) | **POST** /domain | 
[**domain_delete**](DomainApi.md#domain_delete) | **DELETE** /domain/{domainName} | 
[**domain_get**](DomainApi.md#domain_get) | **GET** /domain/{domainName} | 
[**domain_list**](DomainApi.md#domain_list) | **GET** /domain | 


# **certificate_create**
> DefaultMessage certificate_create(domain_name, body)



Post an externally generated certificate

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
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
body = swagger_client.CertificatePayload() # CertificatePayload | 

try:
    api_response = api_instance.certificate_create(domain_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->certificate_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 
 **body** | [**CertificatePayload**](CertificatePayload.md)|  | 

### Return type

[**DefaultMessage**](DefaultMessage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificate_delete**
> DefaultMessage certificate_delete(domain_name, certificate_id)



Remove the certificate

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
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
certificate_id = 'certificate_id_example' # str | 

try:
    api_response = api_instance.certificate_delete(domain_name, certificate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->certificate_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 
 **certificate_id** | **str**|  | 

### Return type

[**DefaultMessage**](DefaultMessage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificate_get**
> Certificate certificate_get(domain_name, certificate_id)



Get a specific certificate and the associated key and CA

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
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
certificate_id = 'certificate_id_example' # str | 

try:
    api_response = api_instance.certificate_get(domain_name, certificate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->certificate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 
 **certificate_id** | **str**|  | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificate_list**
> CertificateList certificate_list(domain_name, next_id=next_id)



Get the list of certificate for a specific domain

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
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
next_id = 56 # int |  (optional)

try:
    api_response = api_instance.certificate_list(domain_name, next_id=next_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->certificate_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 
 **next_id** | **int**|  | [optional] 

### Return type

[**CertificateList**](CertificateList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_create**
> Domain domain_create(body)



Register a new domain

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
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
body = swagger_client.DomainCreateUpdate() # DomainCreateUpdate | 

try:
    api_response = api_instance.domain_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainCreateUpdate**](DomainCreateUpdate.md)|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_delete**
> DefaultMessage domain_delete(domain_name)



Remove the domain

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
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 

try:
    api_response = api_instance.domain_delete(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 

### Return type

[**DefaultMessage**](DefaultMessage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_get**
> Domain domain_get(domain_name)



Get the details of a specific domain

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
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 

try:
    api_response = api_instance.domain_get(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_list**
> DomainList domain_list(next_id=next_id)



Get the list of your domains

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
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
next_id = 56 # int |  (optional)

try:
    api_response = api_instance.domain_list(next_id=next_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_id** | **int**|  | [optional] 

### Return type

[**DomainList**](DomainList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

