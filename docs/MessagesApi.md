# client.MessagesApi

All URIs are relative to *https://mailsac.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_message_label**](MessagesApi.md#add_message_label) | **PUT** /addresses/{email}/messages/{messageId}/labels/{label} | Add a label to a message
[**count_messages**](MessagesApi.md#count_messages) | **GET** /addresses/{email}/message-count | Count messages for an email inbox
[**delete_all_domain_messages**](MessagesApi.md#delete_all_domain_messages) | **POST** /domains/{domain}/delete-all-domain-mail | Delete all messages in a domain
[**delete_all_messages**](MessagesApi.md#delete_all_messages) | **DELETE** /addresses/{email}/messages | Delete all messages for an email inbox
[**delete_message**](MessagesApi.md#delete_message) | **DELETE** /addresses/{email}/messages/{messageId} | Delete an email message
[**delete_message_label**](MessagesApi.md#delete_message_label) | **DELETE** /addresses/{email}/messages/{messageId}/labels/{label} | Remove a label from a message
[**filter_inbox_messages**](MessagesApi.md#filter_inbox_messages) | **GET** /inbox-filter | Filter messages in account by to, from, and/or subject
[**get_body_dirty**](MessagesApi.md#get_body_dirty) | **GET** /dirty/{email}/{messageId} | Get message HTML body (dirty)
[**get_body_plain_text**](MessagesApi.md#get_body_plain_text) | **GET** /text/{email}/{messageId} | Get message plaintext
[**get_body_sanitized**](MessagesApi.md#get_body_sanitized) | **GET** /body/{email}/{messageId} | Get the message HTML body (sanitized)
[**get_full_raw_message**](MessagesApi.md#get_full_raw_message) | **GET** /raw/{email}/{messageId} | Get original SMTP message
[**get_headers**](MessagesApi.md#get_headers) | **GET** /addresses/{email}/messages/{messageId}/headers | Get parsed message headers
[**get_message_metadata**](MessagesApi.md#get_message_metadata) | **GET** /addresses/{email}/messages/{messageId} | Get email message metadata
[**list_domain_messages**](MessagesApi.md#list_domain_messages) | **GET** /domains/{domain}/messages | List messages for an domain
[**list_inbox_messages**](MessagesApi.md#list_inbox_messages) | **GET** /inbox | Get all account messages paginated
[**list_messages**](MessagesApi.md#list_messages) | **GET** /addresses/{email}/messages | List messages for an email inbox
[**list_starred_messages**](MessagesApi.md#list_starred_messages) | **GET** /addresses/starred/messages | List starred (saved) messages on the account
[**search_inbox_messages**](MessagesApi.md#search_inbox_messages) | **GET** /inbox-search | Search messages by to, from, and subject
[**set_message_folder**](MessagesApi.md#set_message_folder) | **PUT** /addresses/{email}/messages/{messageId}/folder/{folder} | Move a message into a folder
[**set_message_read_status**](MessagesApi.md#set_message_read_status) | **PUT** /addresses/{email}/messages/{messageId}/read/{readBoolean} | Set message read/unread status
[**toggle_message_star**](MessagesApi.md#toggle_message_star) | **PUT** /addresses/{email}/messages/{messageId}/star | Star (save) a message

# **add_message_label**
> InlineResponse2002 add_message_label(email, message_id, label)

Add a label to a message

To help organize messages and group messages together, add a label to a message. Labels are used in the Inbox UI to group messages.  When successful, returns 200 with a subset of the message object.  When the label already exists on the message, the message is not modified and the API endpoint returns 200.  No PUT body is needed. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier
label = client.MessageLabel() # MessageLabel | Label for email message - must be url encoded

try:
    # Add a label to a message
    api_response = api_instance.add_message_label(email, message_id, label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->add_message_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 
 **label** | [**MessageLabel**](.md)| Label for email message - must be url encoded | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_messages**
> InlineResponse200 count_messages(email)

Count messages for an email inbox

Get the number of messages for an email inbox address. **It is NOT necessary to reserve the address** before using this route. Whether it is an address on a custom domain, or a public domain, or mailsac.com, the mail can be counted as long as nobody else owns it.

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address

try:
    # Count messages for an email inbox
    api_response = api_instance.count_messages(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->count_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_domain_messages**
> delete_all_domain_messages(domain)

Delete all messages in a domain

Delete all messages for a specifc domain. Starred messages will be deleted.  The domain must be owned domain. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
domain = client.DomainString() # DomainString | Domain

try:
    # Delete all messages in a domain
    api_instance.delete_all_domain_messages(domain)
except ApiException as e:
    print("Exception when calling MessagesApi->delete_all_domain_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**DomainString**](.md)| Domain | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_messages**
> delete_all_messages(email, until=until, limit=limit)

Delete all messages for an email inbox

This deletes all messages for a specific email address.  The address must be an owned address or an address in a owned domain. Starred messages will not be deleted. Use `DELETE /addresses/{email}/messages/{messageId}` to remove starred messages or unstar the messages before calling this route. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
until = client.ModelDate() # ModelDate | Return messages returned up to this UTC date (optional)
limit = client.Limit() # Limit |  (optional)

try:
    # Delete all messages for an email inbox
    api_instance.delete_all_messages(email, until=until, limit=limit)
except ApiException as e:
    print("Exception when calling MessagesApi->delete_all_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **until** | [**ModelDate**](.md)| Return messages returned up to this UTC date | [optional] 
 **limit** | [**Limit**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message**
> InlineResponse2001 delete_message(email, message_id)

Delete an email message

Deletes an individual email message. There is no trash or undo.

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier

try:
    # Delete an email message
    api_response = api_instance.delete_message(email, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->delete_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message_label**
> InlineResponse2002 delete_message_label(email, message_id, label)

Remove a label from a message

Removes a label from a message. Returns 200 with a subset of the message object when successful.  When the label did not exists on the message, the message is not modified and the API endpoint returns 200. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier
label = client.MessageLabel() # MessageLabel | Label for email message - must be url encoded

try:
    # Remove a label from a message
    api_response = api_instance.delete_message_label(email, message_id, label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->delete_message_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 
 **label** | [**MessageLabel**](.md)| Label for email message - must be url encoded | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_inbox_messages**
> InlineResponse2006 filter_inbox_messages(and_subject_includes=and_subject_includes, and_from=and_from, and_to=and_to)

Filter messages in account by to, from, and/or subject

Filter account messages within the the `to` and `from` `.address` fields, and the `subject` line. This differs from `/api/inbox-search` by using logical AND, rather than OR in `/api/inbox-search`.  At least one query condition is required, otherwise a 400 will be returned.  A maximum of 100 results will ever be returned. Refine the query or reduce the number of messages in the account to find specific items. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
and_subject_includes = 'and_subject_includes_example' # str | Messages must include this text in the subject line (optional)
and_from = 'and_from_example' # str | Messages must include this text in FROM envelope (optional)
and_to = 'and_to_example' # str | Messages must include this text in TO envelope or the `message.inbox` is equal to this value (optional)

try:
    # Filter messages in account by to, from, and/or subject
    api_response = api_instance.filter_inbox_messages(and_subject_includes=and_subject_includes, and_from=and_from, and_to=and_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->filter_inbox_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **and_subject_includes** | **str**| Messages must include this text in the subject line | [optional] 
 **and_from** | **str**| Messages must include this text in FROM envelope | [optional] 
 **and_to** | **str**| Messages must include this text in TO envelope or the &#x60;message.inbox&#x60; is equal to this value | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_body_dirty**
> str get_body_dirty(email, message_id, download=download)

Get message HTML body (dirty)

Get a message's HTML content.  Attached images are inlined and nothing has been stripped.  When no HTML body was sent in the original message, a simple HTML body will be created.  Use the querystring param ?download=1 to trigger file download in browser. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier
download = 56 # int | Download to browser (optional)

try:
    # Get message HTML body (dirty)
    api_response = api_instance.get_body_dirty(email, message_id, download=download)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_body_dirty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 
 **download** | **int**| Download to browser | [optional] 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_body_plain_text**
> str get_body_plain_text(email, message_id, download=download)

Get message plaintext

Get a message's text content. If the original message only contained HTML, a simple plain text body will be generated.  HTTP links in the plain text email will be available when fetching the message's metadata at the `message.links[]` property.  Use the querystring param ?download=1 to trigger file download in browser. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier
download = 56 # int | Download to browser (optional)

try:
    # Get message plaintext
    api_response = api_instance.get_body_plain_text(email, message_id, download=download)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_body_plain_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 
 **download** | **int**| Download to browser | [optional] 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_body_sanitized**
> str get_body_sanitized(email, message_id, download=download)

Get the message HTML body (sanitized)

Get safe HTML from an email message. Scripts, images and links are stripped out. This HTML is safer to render than the potentially \"dirty\" original HTML.  When no HTML body was sent in the original message, a simple HTML body will be created.  Use the querystring param ?download=1 to trigger file download in browser. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier
download = 56 # int | Download to browser (optional)

try:
    # Get the message HTML body (sanitized)
    api_response = api_instance.get_body_sanitized(email, message_id, download=download)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_body_sanitized: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 
 **download** | **int**| Download to browser | [optional] 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_full_raw_message**
> str get_full_raw_message(email, message_id, download=download)

Get original SMTP message

Gets the entire original SMTP message transport - everything that was sent over the network to Mailsac's inbound servers, plus any Mailsac-generated `Received` headers, and special `x-mailsac-*` headers. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier
download = 56 # int | Download to browser (optional)

try:
    # Get original SMTP message
    api_response = api_instance.get_full_raw_message(email, message_id, download=download)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_full_raw_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 
 **download** | **int**| Download to browser | [optional] 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_headers**
> MessageHeaders get_headers(email, message_id, download=download, message_headers_format=message_headers_format)

Get parsed message headers

Returns pre-parsed message headers in one of 3 formats - `json`, `json-ordered`, or `plain`.  If no querystring parameter is provided, the default format will be `json`.  Every email is different; fields in the below examples are not guaranteed to exist. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier
download = 56 # int | Download to browser (optional)
message_headers_format = 'message_headers_format_example' # str |  (optional)

try:
    # Get parsed message headers
    api_response = api_instance.get_headers(email, message_id, download=download, message_headers_format=message_headers_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_headers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 
 **download** | **int**| Download to browser | [optional] 
 **message_headers_format** | **str**|  | [optional] 

### Return type

[**MessageHeaders**](MessageHeaders.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_metadata**
> EmailMessage get_message_metadata(email, message_id)

Get email message metadata

Retrieves metadata about a single email message. This route includes additional metadata not available when listing messages, such as parsed links from the text or HTML body, and attachment md5sums.  To get even more information about message attachments, like filenames, see the Attachments API.  To get the entire original SMTP message, see the \"raw\" message route. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier

try:
    # Get email message metadata
    api_response = api_instance.get_message_metadata(email, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_message_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 

### Return type

[**EmailMessage**](EmailMessage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domain_messages**
> EmailMessageShort list_domain_messages(domain, until=until, limit=limit)

List messages for an domain

Get a list of messages across any inboxes of a domain. Messages are always **sorted in decending order by when they were received**, with the newest message always in the first position of the array.  The email message objects are abbreviated to provide basic meta data. To get more information about a specific message, use `GET /api/addresses/{email}/messages/{messageId}`.  The domain must be owned by the account making the request, and have DNS validated. Paginate with `until?=<Date>` and `limit=<uint>`.

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
domain = client.DomainString() # DomainString | Domain
until = client.ModelDate() # ModelDate | Return messages returned up to this UTC date (optional)
limit = client.Limit() # Limit |  (optional)

try:
    # List messages for an domain
    api_response = api_instance.list_domain_messages(domain, until=until, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->list_domain_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**DomainString**](.md)| Domain | 
 **until** | [**ModelDate**](.md)| Return messages returned up to this UTC date | [optional] 
 **limit** | [**Limit**](.md)|  | [optional] 

### Return type

[**EmailMessageShort**](EmailMessageShort.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbox_messages**
> InlineResponse2005 list_inbox_messages(limit=limit, since=since, skip=skip)

Get all account messages paginated

Used by the Inbox UI to display all messages for the account, across all domains and private addresses.  Returns email message short metadata, paginated, with the global account unread message count. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
limit = client.Limit() # Limit |  (optional)
since = client.ModelDate() # ModelDate | Only fetch messages since this date (optional)
skip = client.Skip() # Skip |  (optional)

try:
    # Get all account messages paginated
    api_response = api_instance.list_inbox_messages(limit=limit, since=since, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->list_inbox_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**Limit**](.md)|  | [optional] 
 **since** | [**ModelDate**](.md)| Only fetch messages since this date | [optional] 
 **skip** | [**Skip**](.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_messages**
> EmailMessageShort list_messages(email, until=until, limit=limit)

List messages for an email inbox

Get a list of messages for the email address. Messages are always **sorted in decending order by when they were received**, with the newest message always in the first position of the array.  The email message objects are abbreviated to provide basic meta data. To get more information about a specific message, use `GET /api/addresses/{email}/messages/{messageId}`.  **It is NOT necessary to reserve the address** before checking mail! Whether it is an address on a custom domain, or a public domain, or mailsac.com, the mail can be checked with this route.

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
until = client.ModelDate() # ModelDate | Return messages returned up to this UTC date (optional)
limit = client.Limit() # Limit |  (optional)

try:
    # List messages for an email inbox
    api_response = api_instance.list_messages(email, until=until, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->list_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **until** | [**ModelDate**](.md)| Return messages returned up to this UTC date | [optional] 
 **limit** | [**Limit**](.md)|  | [optional] 

### Return type

[**EmailMessageShort**](EmailMessageShort.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_starred_messages**
> EmailMessageList list_starred_messages()

List starred (saved) messages on the account

Get a list of messages that have been saved and made private for the entire account using the \"star message\" feature.  Messages recieved via the Capture Service will also show up as starred IF the `capturePrivate` flag on the account is enabled.

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
api_instance = client.MessagesApi(client.ApiClient(configuration))

try:
    # List starred (saved) messages on the account
    api_response = api_instance.list_starred_messages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->list_starred_messages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EmailMessageList**](EmailMessageList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_inbox_messages**
> InlineResponse2007 search_inbox_messages(query=query)

Search messages by to, from, and subject

Search all account messages within the the `to` and `from` `.address` fields, and the `subject` line. This differs from `/api/inbox-filter` by using logical OR, rather than AND in `/api/inbox-filter`.  A maximum of 100 results will ever be returned. Refine the query or reduce the number of messages in the account to find specific items. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
query = 'query_example' # str | Searches to, from, and subject for all messages on this account, limited to 100 results. (optional)

try:
    # Search messages by to, from, and subject
    api_response = api_instance.search_inbox_messages(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->search_inbox_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Searches to, from, and subject for all messages on this account, limited to 100 results. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_message_folder**
> InlineResponse2003 set_message_folder(email, message_id, folder)

Move a message into a folder

Move the message to a different mail folder.  No new folders can be added. To organize mail, use labels.  No PUT body is needed. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier
folder = client.MessageFolder() # MessageFolder | Folder for email organization

try:
    # Move a message into a folder
    api_response = api_instance.set_message_folder(email, message_id, folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->set_message_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 
 **folder** | [**MessageFolder**](.md)| Folder for email organization | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_message_read_status**
> InlineResponse2004 set_message_read_status(email, message_id, read_boolean)

Set message read/unread status

Change the read state of a message.  Pass `readBoolean` as `true` to mark the message as read, and `false` to mark it as unread. The default for any new message `false` (unread).  No PUT body is needed. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier
read_boolean = client.ReadBoolean() # ReadBoolean | Set message read/unread

try:
    # Set message read/unread status
    api_response = api_instance.set_message_read_status(email, message_id, read_boolean)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->set_message_read_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 
 **read_boolean** | [**ReadBoolean**](.md)| Set message read/unread | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_message_star**
> EmailMessageShort toggle_message_star(email, message_id)

Star (save) a message

Toggle a message's *starred* status so it will not be automatically recycled when the account's message storage limit is reached.  There is no PUT body.  It returns only the message metadata. 

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
api_instance = client.MessagesApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier

try:
    # Star (save) a message
    api_response = api_instance.toggle_message_star(email, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->toggle_message_star: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 

### Return type

[**EmailMessageShort**](EmailMessageShort.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

