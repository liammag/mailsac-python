# client.WebhooksApi

All URIs are relative to *https://mailsac.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_not_use_webhook_docs_only**](WebhooksApi.md#do_not_use_webhook_docs_only) | **POST** /custom_webhooks | Receive a webhook email message on your server

# **do_not_use_webhook_docs_only**
> do_not_use_webhook_docs_only()

Receive a webhook email message on your server

*Note: this does not work in Swagger UI.*  Webhook Forwarding is one of several options available for forwarding private addresses and custom domains (via catch-all addresses enabled under a custom domain).  Forwarding to a Webhook can be configured by selecting Manage Email Addresses from the Dashboard. Select the Settings button next to the email address to manage, then input the URL under Forward To Custom Webhook and select Save Settings.  Troubleshoot webhooks using your account *Audit Logs*. 

### Example
```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.WebhooksApi()

try:
    # Receive a webhook email message on your server
    api_instance.do_not_use_webhook_docs_only()
except ApiException as e:
    print("Exception when calling WebhooksApi->do_not_use_webhook_docs_only: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

