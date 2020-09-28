# Launch app

```
bot = Bitzlato(<your_uid>, <secret_key>, <kid>)

list_adds = bot.get_list_adds(
    cryptocurrency='BTC', 
    currency='RUB', 
    is_owner_active=True, 
    limit=20, 
    pay_method='4430', 
    order_type='purchase'
    )

print(list_adds)
```
