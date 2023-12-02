# client.AddressesApi

All URIs are relative to *https://mailsac.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_availability**](AddressesApi.md#check_availability) | **GET** /addresses/{email}/availability | Check address ownership
[**create_address**](AddressesApi.md#create_address) | **POST** /addresses/{email} | Reserve (create/own) a private email address
[**create_addresses**](AddressesApi.md#create_addresses) | **POST** /private-addresses-bulk | Reserve multiple private addresses
[**delete_address**](AddressesApi.md#delete_address) | **DELETE** /addresses/{email} | Release a private email address
[**get_address**](AddressesApi.md#get_address) | **GET** /addresses/{email} | Fetch an address or check if it is reserved
[**list_addresses**](AddressesApi.md#list_addresses) | **GET** /addresses | List all private email addresses
[**update_address**](AddressesApi.md#update_address) | **PUT** /addresses/{email} | Update private email address forwarding and metadata

# **check_availability**
> EmailAddressAvailability check_availability(email)

Check address ownership

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
api_instance = client.AddressesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address

try:
    # Check address ownership
    api_response = api_instance.check_availability(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->check_availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 

### Return type

[**EmailAddressAvailability**](EmailAddressAvailability.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_address**
> EmailAddress create_address(email, body=body)

Reserve (create/own) a private email address

Sets the email address private and \"owned\" by the account. All messages which already exist, and any future messages which are received, will be private to this account only.  An email address must be reserved to be able to forward messages to another email address, Slack, web sockets, or webhooks. Public email addresses, and private email addresses under a custom domain, are not routeable. 

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
api_instance = client.AddressesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
body = client.UpdatePrivateAddressForwarding() # UpdatePrivateAddressForwarding |  (optional)

try:
    # Reserve (create/own) a private email address
    api_response = api_instance.create_address(email, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->create_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **body** | [**UpdatePrivateAddressForwarding**](UpdatePrivateAddressForwarding.md)|  | [optional] 

### Return type

[**EmailAddress**](EmailAddress.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_addresses**
> EmailAddressList create_addresses(body)

Reserve multiple private addresses

Reserves multiple private addresses. The max addresses per request is 100. 

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
api_instance = client.AddressesApi(client.ApiClient(configuration))
body = client.PrivateaddressesbulkBody() # PrivateaddressesbulkBody | 

try:
    # Reserve multiple private addresses
    api_response = api_instance.create_addresses(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->create_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrivateaddressesbulkBody**](PrivateaddressesbulkBody.md)|  | 

### Return type

[**EmailAddressList**](EmailAddressList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_address**
> delete_address(email, delete_address_messages=delete_address_messages)

Release a private email address

Removes this private address from ownership by the account. Any email received to the address's inbox will be public in the future, unless the address was under a custom domain which is set private. 

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
api_instance = client.AddressesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
delete_address_messages = true # bool |  (optional)

try:
    # Release a private email address
    api_instance.delete_address(email, delete_address_messages=delete_address_messages)
except ApiException as e:
    print("Exception when calling AddressesApi->delete_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **delete_address_messages** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address**
> EmailAddress get_address(email)

Fetch an address or check if it is reserved

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
api_instance = client.AddressesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address

try:
    # Fetch an address or check if it is reserved
    api_response = api_instance.get_address(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 

### Return type

[**EmailAddress**](EmailAddress.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_addresses**
> EmailAddressList list_addresses()

List all private email addresses

Get an array of private inbox address objects for the account.  These addresses must be setup (\"reserved\") using `POST /api/addresses/:email`, or [on the Add Email Address page](https://mailsac.com/private-address). 

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
api_instance = client.AddressesApi(client.ApiClient(configuration))

try:
    # List all private email addresses
    api_response = api_instance.list_addresses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->list_addresses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EmailAddressList**](EmailAddressList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address**
> update_address(email, body=body)

Update private email address forwarding and metadata

For a private email address, set it to forward to another place.  It can be forwarded to another email (with `via mailsac` indicator), to a websocket, to a webhook, or to a Slack channel. 

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
api_instance = client.AddressesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
body = client.UpdatePrivateAddressForwarding() # UpdatePrivateAddressForwarding |  (optional)

try:
    # Update private email address forwarding and metadata
    api_instance.update_address(email, body=body)
except ApiException as e:
    print("Exception when calling AddressesApi->update_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **body** | [**UpdatePrivateAddressForwarding**](UpdatePrivateAddressForwarding.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

