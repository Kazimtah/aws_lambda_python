 
import json

json_str = '{"id": 234, "brand": "Nike", "qty": 84, "status": {"isForSale": true}}'
sneaker = json.loads(json_str)
for value  in sneaker:
    if value['brand'] == 'Nike':
        print(value)

#print(sneaker)
print(type(sneaker))