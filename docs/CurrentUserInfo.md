# CurrentUserInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | username | [optional] 
**email** | [**EmailString**](EmailString.md) |  | [optional] 
**invoice_email** | [**EmailString**](EmailString.md) |  | [optional] 
**capture_private** | **bool** | Setting which will apply a star to all captured emails. | [optional] 
**message_limit** | **int** | Maximum allowed message history (starred messages + all messages on private addresses and domains) | [optional] 
**sends_remaining** | **int** | Number of outbound recipients left to be able to send a message to | [optional] 
**private_domain** | **int** | Number of custom domain that the account is entitled to but has not yet reserved | [optional] 
**private_address_credits** | **int** | Number of private addresses that the account is entitled to but has not yet reserved | [optional] 
**whitelist_access** | **int** | Flag indicating whether account is allowed to request adding IPs to the global allow-list. | [optional] 
**mo_api_count** | **int** | Approximate number of total API calls made by the account this month | [optional] 
**api_monthly_limit** | **int** | Number of API calls allowed monthly | [optional] 
**billing_hold** | **str** | When present, indicates the account has past-due invoices and service is disabled | [optional] 
**disabled** | **str** | When present, indicates a disabled account | [optional] 
**recents** | [**list[EmailStringList]**](EmailStringList.md) | The most recent email addresses viewed by this account in the UI | [optional] 
**labels** | **list[str]** | Inbox labels created by the account | [optional] 
**company** | **str** | Company name associated with account | [optional] 
**address** | **str** | Company address associated with account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

