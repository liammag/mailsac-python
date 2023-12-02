# SendMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | [**SendMessageTo**](SendMessageTo.md) |  | 
**_from** | [**SendMessageFrom**](SendMessageFrom.md) |  | 
**subject** | [**EmailSubject**](EmailSubject.md) |  | 
**text** | **str** | plaintext email contents | 
**html** | **str** | html email contents | 
**attachments** | [**EmailAttachmentList**](EmailAttachmentList.md) |  | [optional] 
**received** | [**list[ReceivedHeadersList]**](ReceivedHeadersList.md) |  | [optional] 
**raw** | **str** | raw SMTP messsage overrides all other properties | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

