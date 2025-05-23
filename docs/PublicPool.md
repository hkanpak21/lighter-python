# PublicPool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | 
**message** | **str** |  | [optional] 
**account_type** | **int** |  | 
**index** | **int** |  | 
**l1_address** | **str** |  | 
**cancel_all_time** | **int** |  | 
**total_order_count** | **int** |  | 
**pending_order_count** | **int** |  | 
**status** | **int** |  | 
**collateral** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**total_asset_value** | **str** |  | 
**pool_info** | [**PublicPoolInfo**](PublicPoolInfo.md) |  | 
**account_share** | [**PublicPoolShare**](PublicPoolShare.md) |  | 

## Example

```python
from lighter.models.public_pool import PublicPool

# TODO update the JSON string below
json = "{}"
# create an instance of PublicPool from a JSON string
public_pool_instance = PublicPool.from_json(json)
# print the JSON string representation of the object
print(PublicPool.to_json())

# convert the object into a dict
public_pool_dict = public_pool_instance.to_dict()
# create an instance of PublicPool from a dict
public_pool_from_dict = PublicPool.from_dict(public_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


