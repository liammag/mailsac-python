# client.AccountApi

All URIs are relative to *https://mailsac.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_stats**](AccountApi.md#account_stats) | **GET** /me/stats | Get account stats
[**user**](AccountApi.md#user) | **GET** /me | Get current account

# **account_stats**
> CurrentUserStats account_stats()

Get account stats

Get summary information about email addresses, domains, and usage.

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
api_instance = client.AccountApi(client.ApiClient(configuration))

try:
    # Get account stats
    api_response = api_instance.account_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentUserStats**](CurrentUserStats.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user**
> CurrentUserInfo user()

Get current account

Get information about the account for this API key.

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
api_instance = client.AccountApi(client.ApiClient(configuration))

try:
    # Get current account
    api_response = api_instance.user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentUserInfo**](CurrentUserInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

