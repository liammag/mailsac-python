# client.WebSocketsApi

All URIs are relative to *https://mailsac.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_not_use_web_socket_docs_only**](WebSocketsApi.md#do_not_use_web_socket_docs_only) | **POST** /custom_web_sockets | Connect a web socket to wss://sock.mailsac.com/incoming-messages

# **do_not_use_web_socket_docs_only**
> do_not_use_web_socket_docs_only(key=key, addresses=addresses)

Connect a web socket to wss://sock.mailsac.com/incoming-messages

*Note: this does not work in Swagger UI. Visit https://sock.mailsac.com to test.*  You can receive email via web socket for private email addresses and custom domains.  To enable web socket forwarding:  * Addresses: Select *Edit* for the email address you want to forward. Then check the checkbox for web socket forwarding, and save. * Custom Domains: Select *Manage* for the domain and click the *Forwarding* tab. Toggle the *Enable Web Sockets* option.  Note: Web socket forwarding is **not enabled by default.**  ### Web Socket Examples  #### Web Socket Test Page  https://sock.mailsac.com  Receive emails in your web browser.  Experiment with the web socket gateway in realtime.  #### Web Socket Node.js  Listen for Mailsac emails via websocket in this tiny Node.js example app.  https://github.com/ruffrey/mailsac-node-websocket-example  ### Web Socket Connection Endpoint  The web socket endpoint is `wss://sock.mailsac.com/incoming-messages`  Example:  > wss://sock.mailsac.com/incoming-messages?key=k_e9bPnd2adexample&addresses=jeff@mailsac.com,asdf-outbound.mailsac.com  > First frame:  ``` {   \"status\": 200,   \"msg\": \"Listening\",   \"addresses\": [     \"jeff@mailsac.com\"   ],   \"domains\": [     \"asdf-outbound.mailsac.com\"   ] } ```  All web socket messages are JSON. After parsing the JSON, there will be a status field with an HTTP status code (usually 200).  An email coming over the web socket will also have an email property, and its value will be the same as the messages REST API, plus some additional fields. 

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.WebSocketsApi()
key = 'key_example' # str | Mailsac-Key in the `?key=` querystring (optional)
addresses = 'addresses_example' # str | Private addresses or domains which are enabled for web socket messages (optional)

try:
    # Connect a web socket to wss://sock.mailsac.com/incoming-messages
    api_instance.do_not_use_web_socket_docs_only(key=key, addresses=addresses)
except ApiException as e:
    print("Exception when calling WebSocketsApi->do_not_use_web_socket_docs_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Mailsac-Key in the &#x60;?key&#x3D;&#x60; querystring | [optional] 
 **addresses** | **str**| Private addresses or domains which are enabled for web socket messages | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

