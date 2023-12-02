# EmailMessageWebhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**MessageId**](MessageId.md) |  | [optional] 
**_from** | [**list[EmailRecipient]**](EmailRecipient.md) | The FROM sender, this will always have 1 item in the array unless the email was malformed. | [optional] 
**to** | [**list[EmailRecipient]**](EmailRecipient.md) | The RCPT-TO recipients of the email. | [optional] 
**cc** | [**list[EmailRecipient]**](EmailRecipient.md) | CarbonCopy recipients of the email. | [optional] 
**bcc** | [**list[EmailRecipient]**](EmailRecipient.md) | BlindCarbonCopy recipients of the email. | [optional] 
**subject** | [**EmailSubject**](EmailSubject.md) |  | [optional] 
**saved_by** | **str** | Indicates a starred message by your account Account._id. Otherwise &#x60;null&#x60;. | [optional] 
**original_inbox** | **str** | Same as inbox unless sent to the encryptedInbox, in which case it would be the encryptedInbox. | [optional] 
**inbox** | **str** | Email address to which this message belongs. | [optional] 
**domain** | **str** | hostname domain for the inbox | [optional] 
**received** | [**ModelDate**](ModelDate.md) |  | [optional] 
**size** | **float** | Content length in bytes of the original raw email message | [optional] 
**attachments** | [**list[Md5sum]**](Md5sum.md) | &#x60;null&#x60; or array of MD5 hashes of attachments. Use the Attachments API to get metadata and download attachments. | [optional] 
**ip** | **str** | The remote SMTP server that send the mail to the server at &#x60;via&#x60; | [optional] 
**via** | **str** | IP address of SMTP server that received the message from &#x60;ip&#x60; | [optional] 
**folder** | **str** | Inbox folder that this message has been put into | [optional] [default to 'inbox']
**labels** | **list[str]** | Custom inbox labels created by the end user | [optional] 
**read** | **bool** | Read/uread status. true&#x3D;read, false&#x3D;unread. Only set from the Inbox UI app. | [optional] 
**rtls** | **bool** | When true, indicates the SMTP message was received over TLS (encrypted). | [optional] 
**links** | **list[str]** | List of any URLs that were found in the text and HTML body of the message. | [optional] 
**spam** | **float** | Experimental - result of spam filter scan, between 0.0 and 1.0, where 1.0 indicates a high likelihood of being spam | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

