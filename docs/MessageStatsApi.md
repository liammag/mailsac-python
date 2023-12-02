# client.MessageStatsApi

All URIs are relative to *https://mailsac.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_denylist**](MessageStatsApi.md#check_denylist) | **GET** /mailstats/blacklist/{domainOrIP} | Check IP or domain on deny-list
[**denylist**](MessageStatsApi.md#denylist) | **GET** /mailstats/blacklist | List the current deny-list
[**list_top_public_addresses**](MessageStatsApi.md#list_top_public_addresses) | **GET** /mailstats/top-addresses | List top public disposable email addresses receiving messages
[**list_top_public_domains**](MessageStatsApi.md#list_top_public_domains) | **GET** /mailstats/top-domains | List top public domains receiving disposable messages
[**list_top_public_senders**](MessageStatsApi.md#list_top_public_senders) | **GET** /mailstats/top-senders | List top sender email addresses for disposable public messages

# **check_denylist**
> InlineResponse20011 check_denylist(domain_or_ip)

Check IP or domain on deny-list

Check whether an IP or domain is currently on the deny-list.

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
api_instance = client.MessageStatsApi(client.ApiClient(configuration))
domain_or_ip = 'domain_or_ip_example' # str | 

try:
    # Check IP or domain on deny-list
    api_response = api_instance.check_denylist(domain_or_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageStatsApi->check_denylist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_or_ip** | **str**|  | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **denylist**
> list[str] denylist()

List the current deny-list

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
api_instance = client.MessageStatsApi(client.ApiClient(configuration))

try:
    # List the current deny-list
    api_response = api_instance.denylist()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageStatsApi->denylist: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_top_public_addresses**
> InlineResponse2009 list_top_public_addresses(start_date=start_date, end_date=end_date, skip=skip, limit=limit)

List top public disposable email addresses receiving messages

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
api_instance = client.MessageStatsApi(client.ApiClient(configuration))
start_date = client.ModelDate() # ModelDate |  (optional)
end_date = client.ModelDate() # ModelDate |  (optional)
skip = client.Skip() # Skip |  (optional)
limit = client.Limit() # Limit |  (optional)

try:
    # List top public disposable email addresses receiving messages
    api_response = api_instance.list_top_public_addresses(start_date=start_date, end_date=end_date, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageStatsApi->list_top_public_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | [**ModelDate**](.md)|  | [optional] 
 **end_date** | [**ModelDate**](.md)|  | [optional] 
 **skip** | [**Skip**](.md)|  | [optional] 
 **limit** | [**Limit**](.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_top_public_domains**
> InlineResponse20010 list_top_public_domains(start_date=start_date, end_date=end_date, skip=skip, limit=limit)

List top public domains receiving disposable messages

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
api_instance = client.MessageStatsApi(client.ApiClient(configuration))
start_date = client.ModelDate() # ModelDate |  (optional)
end_date = client.ModelDate() # ModelDate |  (optional)
skip = client.Skip() # Skip |  (optional)
limit = client.Limit() # Limit |  (optional)

try:
    # List top public domains receiving disposable messages
    api_response = api_instance.list_top_public_domains(start_date=start_date, end_date=end_date, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageStatsApi->list_top_public_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | [**ModelDate**](.md)|  | [optional] 
 **end_date** | [**ModelDate**](.md)|  | [optional] 
 **skip** | [**Skip**](.md)|  | [optional] 
 **limit** | [**Limit**](.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_top_public_senders**
> InlineResponse2009 list_top_public_senders(start_date=start_date, end_date=end_date, skip=skip, limit=limit)

List top sender email addresses for disposable public messages

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
api_instance = client.MessageStatsApi(client.ApiClient(configuration))
start_date = client.ModelDate() # ModelDate |  (optional)
end_date = client.ModelDate() # ModelDate |  (optional)
skip = client.Skip() # Skip |  (optional)
limit = client.Limit() # Limit |  (optional)

try:
    # List top sender email addresses for disposable public messages
    api_response = api_instance.list_top_public_senders(start_date=start_date, end_date=end_date, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageStatsApi->list_top_public_senders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | [**ModelDate**](.md)|  | [optional] 
 **end_date** | [**ModelDate**](.md)|  | [optional] 
 **skip** | [**Skip**](.md)|  | [optional] 
 **limit** | [**Limit**](.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

