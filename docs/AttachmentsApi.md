# client.AttachmentsApi

All URIs are relative to *https://mailsac.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_public_attachments**](AttachmentsApi.md#count_public_attachments) | **GET** /mailstats/common-attachments/{md5sum}/count | Count public attachments
[**download_attachment**](AttachmentsApi.md#download_attachment) | **GET** /addresses/{email}/messages/{messageId}/attachments/{attachmentIdentifier} | Download email attachment
[**download_public_attachment**](AttachmentsApi.md#download_public_attachment) | **GET** /mailstats/common-attachments/{md5sum}/download | Download public attachment
[**list_message_attachments**](AttachmentsApi.md#list_message_attachments) | **GET** /addresses/{email}/messages/{messageId}/attachments | List attachments for an email message
[**list_messages_for_attachment**](AttachmentsApi.md#list_messages_for_attachment) | **GET** /mailstats/common-attachments/{md5sum} | List public messages with an attachment
[**list_public_attachments**](AttachmentsApi.md#list_public_attachments) | **GET** /mailstats/common-attachments | Search for attachments

# **count_public_attachments**
> InlineResponse2008 count_public_attachments(md5sum)

Count public attachments

Provides count of attachments by md5 sum  Responds with 'Failed to fetch' in swagger editor, works in curl with generated example 

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
api_instance = client.AttachmentsApi(client.ApiClient(configuration))
md5sum = client.Md5sum() # Md5sum | md5 sum of an attachment

try:
    # Count public attachments
    api_response = api_instance.count_public_attachments(md5sum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->count_public_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **md5sum** | [**Md5sum**](.md)| md5 sum of an attachment | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_attachment**
> str download_attachment(email, message_id, attachment_identifier)

Download email attachment

Download an email message attachment as a file.

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
api_instance = client.AttachmentsApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier
attachment_identifier = client.AttachmentIdentifier() # AttachmentIdentifier | Unique identifier of email attachment

try:
    # Download email attachment
    api_response = api_instance.download_attachment(email, message_id, attachment_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->download_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 
 **attachment_identifier** | [**AttachmentIdentifier**](.md)| Unique identifier of email attachment | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_public_attachment**
> download_public_attachment(md5sum)

Download public attachment

Download an attachment with the MD5 sum requested.

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
api_instance = client.AttachmentsApi(client.ApiClient(configuration))
md5sum = client.Md5sum() # Md5sum | md5 sum of an attachment

try:
    # Download public attachment
    api_instance.download_public_attachment(md5sum)
except ApiException as e:
    print("Exception when calling AttachmentsApi->download_public_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **md5sum** | [**Md5sum**](.md)| md5 sum of an attachment | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_message_attachments**
> AttachmentMeta list_message_attachments(email, message_id)

List attachments for an email message

Get attachment metadata on email message.

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
api_instance = client.AttachmentsApi(client.ApiClient(configuration))
email = client.EmailString() # EmailString | Email address
message_id = client.MessageId() # MessageId | Mailsac-generated globally unique message identifier

try:
    # List attachments for an email message
    api_response = api_instance.list_message_attachments(email, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->list_message_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**EmailString**](.md)| Email address | 
 **message_id** | [**MessageId**](.md)| Mailsac-generated globally unique message identifier | 

### Return type

[**AttachmentMeta**](AttachmentMeta.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_messages_for_attachment**
> EmailMessage list_messages_for_attachment(md5sum)

List public messages with an attachment

List the email messages that have attachments with the requested MD5 sum. Limited to non-private inboxes.

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
api_instance = client.AttachmentsApi(client.ApiClient(configuration))
md5sum = client.Md5sum() # Md5sum | md5 sum of an attachment

try:
    # List public messages with an attachment
    api_response = api_instance.list_messages_for_attachment(md5sum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->list_messages_for_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **md5sum** | [**Md5sum**](.md)| md5 sum of an attachment | 

### Return type

[**EmailMessage**](EmailMessage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_attachments**
> list[CommonAttachments] list_public_attachments(start_date, end_date, skip=skip, limit=limit)

Search for attachments

Search for attachments that were received during the requested time period. Limited to non-private inboxes.  Responds with 'Failed to fetch' in swagger editor. Works in curl with generated example. 

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
api_instance = client.AttachmentsApi(client.ApiClient(configuration))
start_date = client.ModelDate() # ModelDate | 
end_date = client.ModelDate() # ModelDate | 
skip = client.Skip() # Skip |  (optional)
limit = client.Limit() # Limit |  (optional)

try:
    # Search for attachments
    api_response = api_instance.list_public_attachments(start_date, end_date, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->list_public_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | [**ModelDate**](.md)|  | 
 **end_date** | [**ModelDate**](.md)|  | 
 **skip** | [**Skip**](.md)|  | [optional] 
 **limit** | [**Limit**](.md)|  | [optional] 

### Return type

[**list[CommonAttachments]**](CommonAttachments.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

