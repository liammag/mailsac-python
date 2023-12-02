# Mailsac Client

## About
The Mailsac API allows interaction with Mailsac services, including email checking, validation, forwarding setup, web socket email messages reception, and outbound mail sending.

Test the Mailsac API online: [Swagger UI Explorer](https://mailsac.com/docs/swagger)

**Base API Endpoint**: `https://mailsac.com/api/`  
_All API documentation is relative to this endpoint._  

## Resources
- [API Documentation](https://docs.mailsac.com/api-docs/index.html)
- [Full Documentation and Guides](https://docs.mailsac.com)
- [Community Support and Discussion Forums](https://forum.mailsac.com/forums/)
- [Web socket example in Node.js - ruffrey](https://github.com/ruffrey/mailsac-node-websocket-example)
- [Terms of Service](https://docs.mailsac.com/en/latest/about/terms_of_service.html)
- [Privacy Policy](https://docs.mailsac.com/en/latest/about/privacy_policy.html)

## Contact
For paid email support and pre-sales, contact us at support@team.mailsac.com.

## Requirements
This package requires Python 2.7 or 3.4 and above.

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://mailsac.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**account_stats**](docs/AccountApi.md#account_stats) | **GET** /me/stats | Get account stats
*AccountApi* | [**user**](docs/AccountApi.md#user) | **GET** /me | Get current account
*AddressesApi* | [**check_availability**](docs/AddressesApi.md#check_availability) | **GET** /addresses/{email}/availability | Check address ownership
*AddressesApi* | [**create_address**](docs/AddressesApi.md#create_address) | **POST** /addresses/{email} | Reserve (create/own) a private email address
*AddressesApi* | [**create_addresses**](docs/AddressesApi.md#create_addresses) | **POST** /private-addresses-bulk | Reserve multiple private addresses
*AddressesApi* | [**delete_address**](docs/AddressesApi.md#delete_address) | **DELETE** /addresses/{email} | Release a private email address
*AddressesApi* | [**get_address**](docs/AddressesApi.md#get_address) | **GET** /addresses/{email} | Fetch an address or check if it is reserved
*AddressesApi* | [**list_addresses**](docs/AddressesApi.md#list_addresses) | **GET** /addresses | List all private email addresses
*AddressesApi* | [**update_address**](docs/AddressesApi.md#update_address) | **PUT** /addresses/{email} | Update private email address forwarding and metadata
*AttachmentsApi* | [**count_public_attachments**](docs/AttachmentsApi.md#count_public_attachments) | **GET** /mailstats/common-attachments/{md5sum}/count | Count public attachments
*AttachmentsApi* | [**download_attachment**](docs/AttachmentsApi.md#download_attachment) | **GET** /addresses/{email}/messages/{messageId}/attachments/{attachmentIdentifier} | Download email attachment
*AttachmentsApi* | [**download_public_attachment**](docs/AttachmentsApi.md#download_public_attachment) | **GET** /mailstats/common-attachments/{md5sum}/download | Download public attachment
*AttachmentsApi* | [**list_message_attachments**](docs/AttachmentsApi.md#list_message_attachments) | **GET** /addresses/{email}/messages/{messageId}/attachments | List attachments for an email message
*AttachmentsApi* | [**list_messages_for_attachment**](docs/AttachmentsApi.md#list_messages_for_attachment) | **GET** /mailstats/common-attachments/{md5sum} | List public messages with an attachment
*AttachmentsApi* | [**list_public_attachments**](docs/AttachmentsApi.md#list_public_attachments) | **GET** /mailstats/common-attachments | Search for attachments
*DomainsApi* | [**list_domains**](docs/DomainsApi.md#list_domains) | **GET** /domains | List domains
*MessagesApi* | [**add_message_label**](docs/MessagesApi.md#add_message_label) | **PUT** /addresses/{email}/messages/{messageId}/labels/{label} | Add a label to a message
*MessagesApi* | [**count_messages**](docs/MessagesApi.md#count_messages) | **GET** /addresses/{email}/message-count | Count messages for an email inbox
*MessagesApi* | [**delete_all_domain_messages**](docs/MessagesApi.md#delete_all_domain_messages) | **POST** /domains/{domain}/delete-all-domain-mail | Delete all messages in a domain
*MessagesApi* | [**delete_all_messages**](docs/MessagesApi.md#delete_all_messages) | **DELETE** /addresses/{email}/messages | Delete all messages for an email inbox
*MessagesApi* | [**delete_message**](docs/MessagesApi.md#delete_message) | **DELETE** /addresses/{email}/messages/{messageId} | Delete an email message
*MessagesApi* | [**delete_message_label**](docs/MessagesApi.md#delete_message_label) | **DELETE** /addresses/{email}/messages/{messageId}/labels/{label} | Remove a label from a message
*MessagesApi* | [**filter_inbox_messages**](docs/MessagesApi.md#filter_inbox_messages) | **GET** /inbox-filter | Filter messages in account by to, from, and/or subject
*MessagesApi* | [**get_body_dirty**](docs/MessagesApi.md#get_body_dirty) | **GET** /dirty/{email}/{messageId} | Get message HTML body (dirty)
*MessagesApi* | [**get_body_plain_text**](docs/MessagesApi.md#get_body_plain_text) | **GET** /text/{email}/{messageId} | Get message plaintext
*MessagesApi* | [**get_body_sanitized**](docs/MessagesApi.md#get_body_sanitized) | **GET** /body/{email}/{messageId} | Get the message HTML body (sanitized)
*MessagesApi* | [**get_full_raw_message**](docs/MessagesApi.md#get_full_raw_message) | **GET** /raw/{email}/{messageId} | Get original SMTP message
*MessagesApi* | [**get_headers**](docs/MessagesApi.md#get_headers) | **GET** /addresses/{email}/messages/{messageId}/headers | Get parsed message headers
*MessagesApi* | [**get_message_metadata**](docs/MessagesApi.md#get_message_metadata) | **GET** /addresses/{email}/messages/{messageId} | Get email message metadata
*MessagesApi* | [**list_domain_messages**](docs/MessagesApi.md#list_domain_messages) | **GET** /domains/{domain}/messages | List messages for an domain
*MessagesApi* | [**list_inbox_messages**](docs/MessagesApi.md#list_inbox_messages) | **GET** /inbox | Get all account messages paginated
*MessagesApi* | [**list_messages**](docs/MessagesApi.md#list_messages) | **GET** /addresses/{email}/messages | List messages for an email inbox
*MessagesApi* | [**list_starred_messages**](docs/MessagesApi.md#list_starred_messages) | **GET** /addresses/starred/messages | List starred (saved) messages on the account
*MessagesApi* | [**search_inbox_messages**](docs/MessagesApi.md#search_inbox_messages) | **GET** /inbox-search | Search messages by to, from, and subject
*MessagesApi* | [**set_message_folder**](docs/MessagesApi.md#set_message_folder) | **PUT** /addresses/{email}/messages/{messageId}/folder/{folder} | Move a message into a folder
*MessagesApi* | [**set_message_read_status**](docs/MessagesApi.md#set_message_read_status) | **PUT** /addresses/{email}/messages/{messageId}/read/{readBoolean} | Set message read/unread status
*MessagesApi* | [**toggle_message_star**](docs/MessagesApi.md#toggle_message_star) | **PUT** /addresses/{email}/messages/{messageId}/star | Star (save) a message
*WebSocketsApi* | [**do_not_use_web_socket_docs_only**](docs/WebSocketsApi.md#do_not_use_web_socket_docs_only) | **POST** /custom_web_sockets | Connect a web socket to wss://sock.mailsac.com/incoming-messages
*WebhooksApi* | [**do_not_use_webhook_docs_only**](docs/WebhooksApi.md#do_not_use_webhook_docs_only) | **POST** /custom_webhooks | Receive a webhook email message on your server
*EmailValidationApi* | [**validate_address**](docs/EmailValidationApi.md#validate_address) | **GET** /validations/addresses/{email} | Validate an email address and if it is disposable
*EmailValidationApi* | [**validate_addresses_bulk**](docs/EmailValidationApi.md#validate_addresses_bulk) | **POST** /validations/addresses | Validate up to 50 email addresses
*MessageStatsApi* | [**check_denylist**](docs/MessageStatsApi.md#check_denylist) | **GET** /mailstats/blacklist/{domainOrIP} | Check IP or domain on deny-list
*MessageStatsApi* | [**denylist**](docs/MessageStatsApi.md#denylist) | **GET** /mailstats/blacklist | List the current deny-list
*MessageStatsApi* | [**list_top_public_addresses**](docs/MessageStatsApi.md#list_top_public_addresses) | **GET** /mailstats/top-addresses | List top public disposable email addresses receiving messages
*MessageStatsApi* | [**list_top_public_domains**](docs/MessageStatsApi.md#list_top_public_domains) | **GET** /mailstats/top-domains | List top public domains receiving disposable messages
*MessageStatsApi* | [**list_top_public_senders**](docs/MessageStatsApi.md#list_top_public_senders) | **GET** /mailstats/top-senders | List top sender email addresses for disposable public messages

## Documentation For Models

 - [AllOfEmailMessageWebSocketFrameEmail](docs/AllOfEmailMessageWebSocketFrameEmail.md)
 - [AttachmentIdentifier](docs/AttachmentIdentifier.md)
 - [AttachmentMeta](docs/AttachmentMeta.md)
 - [ByteEncoding](docs/ByteEncoding.md)
 - [CommonAttachments](docs/CommonAttachments.md)
 - [CurrentUserInfo](docs/CurrentUserInfo.md)
 - [CurrentUserStats](docs/CurrentUserStats.md)
 - [Domain](docs/Domain.md)
 - [DomainString](docs/DomainString.md)
 - [DomainsList](docs/DomainsList.md)
 - [EmailAddress](docs/EmailAddress.md)
 - [EmailAddressAvailability](docs/EmailAddressAvailability.md)
 - [EmailAddressIntegrity](docs/EmailAddressIntegrity.md)
 - [EmailAddressIntegrityList](docs/EmailAddressIntegrityList.md)
 - [EmailAddressList](docs/EmailAddressList.md)
 - [EmailAttachment](docs/EmailAttachment.md)
 - [EmailAttachmentList](docs/EmailAttachmentList.md)
 - [EmailMessage](docs/EmailMessage.md)
 - [EmailMessageBodyProps](docs/EmailMessageBodyProps.md)
 - [EmailMessageList](docs/EmailMessageList.md)
 - [EmailMessageShort](docs/EmailMessageShort.md)
 - [EmailMessageWebSocketFrame](docs/EmailMessageWebSocketFrame.md)
 - [EmailMessageWebhook](docs/EmailMessageWebhook.md)
 - [EmailRecipient](docs/EmailRecipient.md)
 - [EmailString](docs/EmailString.md)
 - [EmailStringList](docs/EmailStringList.md)
 - [EmailSubject](docs/EmailSubject.md)
 - [ErrorResponseBody](docs/ErrorResponseBody.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [Limit](docs/Limit.md)
 - [Md5sum](docs/Md5sum.md)
 - [MessageFolder](docs/MessageFolder.md)
 - [MessageHeaders](docs/MessageHeaders.md)
 - [MessageId](docs/MessageId.md)
 - [MessageLabel](docs/MessageLabel.md)
 - [MessageLabels](docs/MessageLabels.md)
 - [ModelDate](docs/ModelDate.md)
 - [NotEnoughCreditsResponse](docs/NotEnoughCreditsResponse.md)
 - [PrivateaddressesbulkBody](docs/PrivateaddressesbulkBody.md)
 - [ReadBoolean](docs/ReadBoolean.md)
 - [ReceivedHeaders](docs/ReceivedHeaders.md)
 - [ReceivedHeadersList](docs/ReceivedHeadersList.md)
 - [SendMessage](docs/SendMessage.md)
 - [SendMessageFrom](docs/SendMessageFrom.md)
 - [SendMessageTo](docs/SendMessageTo.md)
 - [Skip](docs/Skip.md)
 - [TooManyRecipientsResponse](docs/TooManyRecipientsResponse.md)
 - [UpdatePrivateAddressForwarding](docs/UpdatePrivateAddressForwarding.md)
 - [ValidationsAddressesBody](docs/ValidationsAddressesBody.md)

## Documentation For Authorization


## APIKeyHeader

- **Type**: API key
- **API key parameter name**: Mailsac-Key
- **Location**: HTTP header

## APIKeyQueryParam

- **Type**: API key
- **API key parameter name**: _mailsacKey
- **Location**: URL query string


## Author


