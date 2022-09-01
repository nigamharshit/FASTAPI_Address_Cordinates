import requests

response = requests.get('http://127.0.0.1:8000/retrieve_all_address_details')

json_output = response.json()

print(json_output)
print()
print(type(json_output))
print()
for i in json_output:
    print(i.get('address'))
