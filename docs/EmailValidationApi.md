# client.EmailValidationApi

All URIs are relative to *https://mailsac.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_address**](EmailValidationApi.md#validate_address) | **GET** /validations/addresses/{email} | Validate an email address and if it is disposable
[**validate_addresses_bulk**](EmailValidationApi.md#validate_addresses_bulk) | **POST** /validations/addresses | Validate up to 50 email addresses

# **validate_address**
> EmailAddressIntegrity validate_address(email)

Validate an email address and if it is disposable

Determine whether an email address is a valid format, whether it is a disposable address, and the domains or IP addresses it is associated with. 

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = client.Configuration()
configuration.api_key['Mailsac-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Mailsac-Key'] = 'Bearer'
# Configure API key authorization: APIKeyQueryParam
configuration = client.Configuration()
configuration.api_key['_mailsacKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_mailsacKey'] = 'Bearer'

# create an instance of the API class
api_instance = client.EmailValidationApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address

try:
    # Validate an email address and if it is disposable
    api_response = api_instance.validate_address(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailValidationApi->validate_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 

### Return type

[**EmailAddressIntegrity**](EmailAddressIntegrity.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_addresses_bulk**
> EmailAddressIntegrityList validate_addresses_bulk(body)

Validate up to 50 email addresses

Determine whether an email address is a valid format, whether it is a disposable address, and the domains or IP addresses it is associated with. 

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = client.Configuration()
configuration.api_key['Mailsac-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Mailsac-Key'] = 'Bearer'
# Configure API key authorization: APIKeyQueryParam
configuration = client.Configuration()
configuration.api_key['_mailsacKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['_mailsacKey'] = 'Bearer'

# create an instance of the API class
api_instance = client.EmailValidationApi(client.ApiClient(configuration))
body = client.ValidationsAddressesBody() # ValidationsAddressesBody | 

try:
    # Validate up to 50 email addresses
    api_response = api_instance.validate_addresses_bulk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailValidationApi->validate_addresses_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ValidationsAddressesBody**](ValidationsAddressesBody.md)|  | 

### Return type

[**EmailAddressIntegrityList**](EmailAddressIntegrityList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

