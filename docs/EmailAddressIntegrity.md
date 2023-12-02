# EmailAddressIntegrity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Full email address that was checked. | 
**valid_format** | **bool** | Indicates if the format is valid. | 
**local** | **str** | The \&quot;local part\&quot; of the email address, before the @ symbol. | [optional] 
**domain** | **str** | The domain of the email address which was used for evaluating disposable components, after the @ symbol. | [optional] 
**is_disposable** | **bool** | Boolean indicating if this email address is known to resolve to disposable email providers, most likely making it not useful for marketing mailing lists or signups. | [optional] 
**disposable_domains** | **list[str]** | Array of string domains where this email resolves to, which is helpful when the domain is custom, but receives its mail at a disposable email provider. | [optional] 
**aliases** | **list[str]** | Array of string domains and IP addresses which are associated with the domain for this email address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

