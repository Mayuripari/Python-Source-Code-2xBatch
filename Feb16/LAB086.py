api_response = {
    "first name": "Mayuri",
    "age": 44,
    "email": "parit.m@gmail.com",
    "password": "12345@mp",
    "address": "MH"
}
print(api_response)
print(type(api_response))
print(api_response.get('password'))

for k, v in api_response.items():
    print(k, "->", v)

for key, value in api_response.items():
    print(key, "->", pair)