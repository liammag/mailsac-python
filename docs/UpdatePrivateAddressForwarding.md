# UpdatePrivateAddressForwarding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **str** | User configurable metadata about this private address. | [optional] 
**forward** | **str** | email address - SMTP forwarding / standard email forwarding - set to \&quot;\&quot; or null to disable forwarding | [optional] [default to '']
**enablews** | **bool** | boolean, defaults false - set to true to enable web socket forwarding (see Web Socket API) | [optional] [default to False]
**webhook** | **str** | url - set to your public webhook endpoint to receive mail via webhook - set to \&quot;\&quot; or null to disable webhooks | [optional] [default to '']
**webhook_slack** | **str** | Slack webhook URL where messages will be published. | [optional] [default to '']
**webhook_slack_to_from** | **bool** | When webhookSlack is set, controls whether the message includes TO and FROM | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

