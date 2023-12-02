# EmailAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the unique identifier of this email address is the email address itself | [optional] 
**info** | **str** | Allows setting custom information about this email address. | [optional] 
**enabledws** | **bool** | boolean defaulting false indicating whether to publish messages via web socket when the user owning this inbox is subscribed | [optional] 
**forward** | **str** | email address where messages to this inbox will be forwarded | [optional] 
**webhook** | **str** | URL where messages to this inbox will be forwarded | [optional] 
**webhook_slack** | **str** | Slack webhook endpoint where messages should be published | [optional] 
**webhook_slack_to_from** | **bool** | When webhookSlack is set, controls whether the message includes TO and FROM | [optional] 
**owner** | **str** | Account that owns the address (owns the privacy) | [optional] 
**encrypted_inbox** | **str** | An alternate email address that will result in the message being delivered to this inbox. This is not always present. | [optional] 
**catch_all** | **str** | Indicates whether this is a catch-all address, and for which domain. | [optional] 
**implicit** | **bool** | When the user owns the domain but has not reserved the address individually, this field is set to true. | [optional] [default to False]
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

