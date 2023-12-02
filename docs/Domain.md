# Domain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | domain | [optional] 
**created** | **datetime** | Date domain was created | [optional] 
**updated** | **datetime** | Date domain settings were last updated | [optional] 
**enablews** | **bool** | boolean defaulting false indicating whether to publish messages via web socket to any subscribed web socket sessions  | [optional] 
**hosted** | **bool** | boolean defaulting false indicating whether this is managed by mailsac (on msdc.co) | [optional] 
**is_default** | **bool** | boolean defaulting false indicating whether this is the default domain for the account which will show in the sidebar first  | [optional] 
**is_private** | **bool** | boolean defaulting true indicating whether inboxes and messages for this domain will be visible publicly  | [optional] 
**last_verification_errors** | **str** | during custom domain verification, this field indicates dns issues | [optional] 
**owner** | **str** | the account to which this domain is assigned and can be managed | [optional] 
**verification_txt** | **str** | during custom domain verification, this field indicates value of a TXT record that must be added to the domain&#x27;s DNS settings  | [optional] 
**verified** | **bool** | boolean defaulting false indicating whether this domain has been verified via dns TXT record verificationTxt  | [optional] 
**verified_mx** | **bool** | boolean defaulting false indicating whether the domain will receive email successfully at Mailsac. Tthis domain has been verified via dns MX records when true.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

